# Q6: Student Examination Performance Prediction
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

study_hours = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
exam_marks = [35, 40, 45, 55, 60, 65, 75, 80, 85, 95]

# a) Initialize model
model = LinearRegression()

# b) 80/20 split
X_train, X_test, y_train, y_test = train_test_split(
    study_hours, exam_marks, test_size=0.2, random_state=42)

# c) Train and predict
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Test hours :", np.array(X_test).ravel())
print("Actual     :", y_test)
print("Predicted  :", np.round(y_pred, 2))
print(f"Slope = {model.coef_[0]:.3f}, Intercept = {model.intercept_:.3f}")

# d) MAE
mae = mean_absolute_error(y_test, y_pred)
print(f"\nMAE = {mae:.3f} marks")
print(f"Interpretation: on average, predictions are off by about {mae:.1f} marks, which is small on a 0-100 scale.")

# e) Predict for 6.5 hours
pred = model.predict([[6.5]])[0]
print(f"Predicted marks for 6.5 study hours: {pred:.2f}")
