# Q7: Student Pass/Fail Classification
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

df = pd.DataFrame({
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 9, 3, 8],
    "Attendance":  [50, 55, 60, 65, 70, 75, 80, 85, 60, 90],
    "Result":      ["Fail", "Fail", "Fail", "Fail", "Pass", "Pass", "Pass", "Pass", "Fail", "Pass"]})

# a) Encode Fail = 0, Pass = 1
df["Result"] = df["Result"].map({"Fail": 0, "Pass": 1})

# b) Features and target
X = df[["Study_Hours", "Attendance"]]
y = df["Result"]

# c) Stratified 80/20 split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# d) Train and evaluate
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
acc = accuracy_score(y_test, clf.predict(X_test))
print(f"Test size: {len(X_test)} samples")
print(f"Test accuracy: {acc:.2f}")

# e) Predict for 6 hours, 78% attendance
new = pd.DataFrame({"Study_Hours": [6], "Attendance": [78]})
pred = clf.predict(new)[0]
print(f"Prediction for 6 hrs, 78% attendance: {'Pass' if pred == 1 else 'Fail'} ({pred})")
print("Note: with only 10 records, the 2-sample test set makes accuracy very coarse (0, 0.5 or 1).")
