class SentimentAnalysisCampaign:
    def __init__(self):
        pass

    def sentimentana(self):
        ############### Sentiment Analysis using LSTM #################
        import pandas as pd
        import numpy as np
        from sklearn.model_selection import train_test_split
        from sklearn.preprocessing import LabelEncoder
        import tensorflow as tf
        from tensorflow.keras.preprocessing.text import Tokenizer
        from tensorflow.keras.preprocessing.sequence import pad_sequences
        from tensorflow.keras import layers, models
        import matplotlib.pyplot as plt

        CSV_PATH="/Users/Yuvaan/Downloads/dataset/text_emotion.csv"
        TEXT_COLUMN = "content"
        LABEL_COLUMN = "sentiment"
        BATCH_SIZE = 256
        EPOCHS = 10

        df = pd.read_csv(CSV_PATH)
        df = df.dropna(subset=[TEXT_COLUMN, LABEL_COLUMN])

        #label_counts = df[LABEL_COLUMN].value_counts()
        #top_5_labels = label_counts.index[:5].tolist()
        #print("\nTop 5 labels:", top_5_labels)
        #df = df[df[LABEL_COLUMN].isin(top_5_labels)].reset_index(drop=True)
        #print("Data size after filtering to top 5 labels:", len(df))
        texts = df[TEXT_COLUMN].astype(str).values
        labels = df[LABEL_COLUMN].values

        tokenizer = Tokenizer()
        tokenizer.fit_on_texts(texts)
        sequences = tokenizer.texts_to_sequences(texts)
        vocab_size = len(tokenizer.word_index) + 1
        print("\nVocabulary size:", vocab_size)
        max_seq_len = max(len(seq) for seq in sequences)
        print("Maximum sequence length:", max_seq_len)
        X_padded =pad_sequences(sequences, maxlen=max_seq_len, padding="post", truncating="post") # Pad sequences to the same length
        print(X_padded)

        label_encoder = LabelEncoder()
        y_int = label_encoder.fit_transform(labels)
        num_classes = len(label_encoder.classes_)
        print("Number of classes:", num_classes, " (should be 13 for full dataset)")
        y = tf.keras.utils.to_categorical(y_int, num_classes=num_classes)
        print(y)
        print("y_categorical shape:", y.shape)

        x_train, x_test, y_train, y_test = train_test_split(X_padded, y, test_size=0.3, random_state=42)
        model = models.Sequential([
            layers.Embedding(input_dim=vocab_size, output_dim=13, input_length=max_seq_len),
            # First LSTM with 128 units
            layers.LSTM(128, return_sequences=True),
            # Second LSTM with 64 units
            layers.LSTM(64),
            # Fully connected + dropout
            layers.Dense(100, activation="relu"),
            layers.Dropout(0.5),
            # Output layer: 5 units, softmax
            layers.Dense(num_classes, activation="softmax")
        ])
        model.summary()

        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        #history = model.fit(X_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE, validation_data=(X_val, y_val))
        try:
            history = model.fit(x_train, y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, validation_split=0.1,verbose=1)
        except Exception as e:
            print("Error during model training:", e)

        test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)

        print(f"\nTest accuracy: {test_acc:.4f}")
        # Plot training & validation accuracy values
        plt.plot(history.history['accuracy'], label='train_accuracy')
        plt.plot(history.history['val_accuracy'], label='val_accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.show()



bc=SentimentAnalysisCampaign()
print(bc.sentimentana())
