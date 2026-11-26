# Q9: Breast Cancer Classification (educational use only)
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

# a) Load and describe
data = load_breast_cancer()
X, y = data.data, data.target
print("Dimensions:", X.shape)
print("Number of features:", len(data.feature_names))
print("First 5 features:", [str(f) for f in data.feature_names[:5]])
print("Classes:", {0: "malignant", 1: "benign"}, "| counts: malignant =", int((y == 0).sum()), ", benign =", int((y == 1).sum()))

# b) Stratified split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# c) Pipeline
pipe = Pipeline([("scaler", StandardScaler()),
                 ("clf", LogisticRegression(max_iter=1000))])
pipe.fit(X_train, y_train)

# d) Evaluation (positive class = 1 = benign)
y_pred = pipe.predict(X_test)
print(f"\nAccuracy : {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred):.4f} (benign as positive class)")
print(f"Recall   : {recall_score(y_test, y_pred):.4f}")
cm = confusion_matrix(y_test, y_pred)
print("Confusion matrix (rows=actual, cols=predicted; order: malignant, benign):\n", cm)
print(f"Malignant tumors missed (predicted benign): {cm[0][1]}")

# e) Explanation
print("\nWhy accuracy alone is insufficient:")
print("Classes are imbalanced and errors have unequal costs. Missing a malignant tumor (false")
print("negative for cancer) is far more dangerous than a false alarm, yet accuracy treats both")
print("equally. Precision, recall and the confusion matrix reveal what kind of errors occur.")
