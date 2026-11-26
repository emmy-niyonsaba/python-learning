# Q10: Machine Learning Model Comparison (Iris)
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# a) Load
iris = load_iris()
X, y = iris.data, iris.target
print("Features:", list(iris.feature_names))
print("Classes :", [str(c) for c in iris.target_names])

# b) Stratified split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# c) Models: scale for distance/gradient-based models (KNN, LogReg); trees don't need scaling
models = {
    "KNN (scaled)": make_pipeline(StandardScaler(), KNeighborsClassifier()),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Logistic Regression (scaled)": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
}

# d) Accuracy on the same test set
results = {}
for name, m in models.items():
    m.fit(X_train, y_train)
    results[name] = accuracy_score(y_test, m.predict(X_test))
    print(f"{name:32s}: {results[name]:.4f}")

# e) Best result and limitation
best_acc = max(results.values())
best = [n for n, a in results.items() if a == best_acc]
print(f"\nBest test accuracy: {best_acc:.4f} -> {', '.join(best)}")
print("Limitation: a single split gives only 30 test samples, so one misclassification changes accuracy by ~3.3%;")
print("the result depends on which samples fell in the test set. Cross-validation gives a more reliable estimate.")
