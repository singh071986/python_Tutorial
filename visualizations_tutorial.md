# Beginner's Guide to Box Plots, Violin Plots, and Heat Maps

Welcome! This guide introduces three essential data visualizations for beginners: Box plots, Violin plots, and Heat maps. Each section includes a simple explanation, example code, and a visual sketch.

---

## 1. Box Plots

**What is a Box Plot?**
A box plot (or box-and-whisker plot) shows the distribution of data based on five summary statistics: minimum, first quartile (Q1), median, third quartile (Q3), and maximum. It helps you see the spread and identify outliers.

**Example Code:**
```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data
np.random.seed(0)
data = np.random.normal(size=100)

# Create box plot
sns.boxplot(x=data)
plt.title('Box Plot Example')
plt.show()
```

**Visual Representation:**
```
|-----|=======|-----|
 min  Q1 med Q3 max
```
- The box shows Q1 to Q3 (the interquartile range).
- The line inside the box is the median.
- Whiskers extend to min and max (or outliers).

---

## 2. Violin Plots

**What is a Violin Plot?**
A violin plot combines a box plot with a density plot. It shows the distribution's shape, spread, and probability density.

**Example Code:**
```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data
np.random.seed(1)
data = np.random.normal(size=100)

# Create violin plot
sns.violinplot(x=data)
plt.title('Violin Plot Example')
plt.show()
```

**Visual Representation:**
```
   ()
  (  )
  |  |
  |  |
  (  )
   ()
```
- The width shows the frequency of data values.
- The center line is the median.

---

## 3. Heat Maps

**What is a Heat Map?**
A heat map displays data in a matrix format, using colors to represent values. It's great for visualizing correlations or patterns in tabular data.

**Example Code:**
```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Sample data
np.random.seed(2)
data = np.random.rand(5, 5)

# Create heat map
sns.heatmap(data, annot=True, cmap='coolwarm')
plt.title('Heat Map Example')
plt.show()
```

**Visual Representation:**
```
+-----+-----+-----+
|  1  |  2  |  3  |
+-----+-----+-----+
|  4  |  5  |  6  |
+-----+-----+-----+
```
- Each cell's color shows its value.
- Useful for comparing many values at once.

---

## Tips for Beginners
- Try changing the data to see how the plots change.
- Use `seaborn` for easy and beautiful visualizations.
- Explore plot options like colors, labels, and annotations.
- Practice with your own datasets!

---

Happy visualizing! 🎨

