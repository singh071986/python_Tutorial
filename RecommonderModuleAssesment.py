import os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_books(path="/Users/Yuvaan/IdeaProjects/Anncnn/books.csv", on_bad_lines="skip"):
    """
    Load the Goodreads books CSV into a DataFrame.
    Uses engine='python' and on_bad_lines='skip' to tolerate malformed rows.
    Reads all columns as strings; downstream functions convert numerics as needed.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found at {path}. Download from Kaggle and place it there.")

    # Try utf-8 first, fallback to latin1 if necessary
    try:
        df = pd.read_csv(path, engine="python", on_bad_lines=on_bad_lines, dtype=str, encoding="utf-8")
    except Exception:
        df = pd.read_csv(path, engine="python", on_bad_lines=on_bad_lines, dtype=str, encoding="latin1")

    # Clean column names (strip whitespace)
    df.columns = df.columns.str.strip()
    return df

def Popularity_Recommender(df, top_n=10, m_quantile=0.90):
    """
    Recommend books by popularity using a weighted rating similar to IMDB:
      weighted_rating = (v/(v+m))*R + (m/(v+m))*C
    where:
      R = average_rating for the book,
      v = ratings_count,
      m = minimum votes required (set as quantile of ratings_count),
      C = mean average rating across all books.
    Returns top_n DataFrame of recommended books.
    """
    # Required columns check
    required = {"title", "authors", "average_rating", "ratings_count"}
    if not required.issubset(df.columns):
        raise ValueError(f"DataFrame must contain columns: {required}")

    books = df.copy()
    books = books.dropna(subset=["average_rating", "ratings_count"])
    books["ratings_count"] = pd.to_numeric(books["ratings_count"], errors="coerce").fillna(0)
    books["average_rating"] = pd.to_numeric(books["average_rating"], errors="coerce").fillna(0)

    C = books["average_rating"].mean()
    m = books["ratings_count"].quantile(m_quantile)

    qualified = books[books["ratings_count"] >= m].copy()
    if qualified.empty:
        # fallback: use top by ratings_count if quantile too strict
        qualified = books.sort_values("ratings_count", ascending=False).head(top_n*5)

    qualified["weighted_rating"] = (
        (qualified["ratings_count"] / (qualified["ratings_count"] + m)) * qualified["average_rating"]
        + (m / (qualified["ratings_count"] + m)) * C
    )
    recommendations = qualified.sort_values("weighted_rating", ascending=False)
    return recommendations[["title", "authors", "average_rating", "ratings_count", "weighted_rating"]].head(top_n)

def Content_based_Recommender(df):
    """
    Build and return a recommender object (function) that, given a book title,
    returns the top-N most similar books based on TF-IDF on the 'authors' column
    and cosine similarity.
    Usage:
      recommender = Content_based_Recommender(df)
      recommender("Some Book Title", top_n=10)
    """
    if "title" not in df.columns or "authors" not in df.columns:
        raise ValueError("DataFrame must contain 'title' and 'authors' columns.")

    books = df.copy()
    books["authors"] = books["authors"].fillna("").astype(str)

    # TF-IDF on authors (as requested). For richer content, extend to other fields.
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(books["authors"])

    # cosine similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # mapping title -> index (first occurrence)
    indices = pd.Series(books.index, index=books["title"]).drop_duplicates()

    def recommend(title, top_n=10):
        """
        Recommend books similar to `title`. Returns DataFrame with columns:
        title, authors, score
        """
        # normalize incoming title
        title_in = str(title).strip()

        # Explicit membership check against the index labels to avoid ambiguous-array error
        if title_in not in indices.index:
            # try exact case-insensitive match
            lower_to_orig = {str(t).strip().lower(): t for t in indices.index}
            key = title_in.lower()
            if key in lower_to_orig:
                title_in = lower_to_orig[key]
            else:
                # try substring match (first match)
                matches = [t for t in indices.index if title_in.lower() in str(t).lower()]
                if matches:
                    title_in = matches[0]
                else:
                    raise ValueError(f"Title '{title}' not found in dataset.")

        # retrieve index and ensure it's a single integer
        idx_val = indices.loc[title_in]
        if isinstance(idx_val, (pd.Series, np.ndarray, list)):
            # take first occurrence
            idx = int(idx_val.iloc[0]) if isinstance(idx_val, pd.Series) else int(idx_val[0])
        else:
            idx = int(idx_val)

        sim_scores = list(enumerate(cosine_sim[idx]))
        # sort by similarity score
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        # skip the first one (the book itself)
        sim_scores = sim_scores[1: top_n + 1]
        book_indices = [i for i, score in sim_scores]
        scores = [float(score) for i, score in sim_scores]
        results = books.iloc[book_indices][["title", "authors"]].copy()
        results["score"] = scores
        results = results.reset_index(drop=True)
        return results

    return recommend

if __name__ == "__main__":
    # Quick demo when running as a script
    try:
        df = load_books()
    except FileNotFoundError as e:
        print(str(e))
    else:
        print("Top 10 Popularity-based recommendations:")
        try:
            pop_rec = Popularity_Recommender(df, top_n=10)
            print(pop_rec.to_string(index=False))
        except Exception as e:
            print("Popularity recommender error:", e)

        print("\nContent-based example for the first title in dataset:")
        try:
            recommender = Content_based_Recommender(df)
            sample_title = df["title"].iloc[0]
            print(f"Sample title: {sample_title}")
            print(recommender(sample_title, top_n=5).to_string(index=False))
        except Exception as e:
            print("Content-based recommender error:", e)
