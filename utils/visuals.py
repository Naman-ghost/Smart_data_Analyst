import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_visuals(df, filename):
    plt.figure(figsize=(10, 6))
    numeric_cols = df.select_dtypes(include='number').columns

    if len(numeric_cols) < 2:
        raise Exception("Need at least 2 numeric columns for plot")

    sns.scatterplot(data=df, x=numeric_cols[0], y=numeric_cols[1])
    plt.title(f"{numeric_cols[0]} vs {numeric_cols[1]}")

    out_path = os.path.join("uploads", f"{filename}_plot.png")
    plt.savefig(out_path)
    plt.close()
    return out_path
