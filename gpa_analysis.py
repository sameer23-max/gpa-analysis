"""gpa_analysis.py

Small script that demonstrates basic pandas operations on a students dataset.
"""

import pandas as pd


def create_dataset():
    data = {
        "Names": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "Ages": [20, 21, 19, 22, 20],
        "Majors": ["CSE", "Math", "CSE", "Physics", "CSE"],
        "GPAs": [3.8, 3.2, 3.9, 3.5, 3.7],
    }
    return pd.DataFrame(data)


def main():
    df = create_dataset()

    print("Students majoring in CSE:")
    print(df[df["Majors"] == "CSE"], end="\n\n")

    print("Average GPA:", df["GPAs"].mean())
    print("Top student:", df.loc[df["GPAs"].idxmax(), "Names"], end="\n\n")

    # Add a new student and sort by GPA
    new = pd.DataFrame({"Names": ["Frank"], "Ages": [21], "Majors": ["Math"], "GPAs": [3.4]})
    df = pd.concat([df, new], axis=0, ignore_index=True)
    df = df.sort_values(by="GPAs", ascending=False)

    print("Average GPA by major:")
    print(df.groupby("Majors")["GPAs"].mean(), end="\n\n")

    print("Full dataset (sorted by GPA):")
    print(df.to_string(index=False))


if __name__ == "__main__":
    main()
