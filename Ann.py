from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt

# 1. Load Dataset (Handwritten digits 0-9)
digits = load_digits()
X = digits.data
y = digits.target

# Show few sample images
plt.gray()
for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(digits.images[i], interpolation='nearest')
    plt.title(f"Label: {digits.target[i]}")
plt.show()

# 2. Split into train & test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Normalize data (important for ANN)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Build ANN Model
model = MLPClassifier(
    hidden_layer_sizes=(128, 64),   # two hidden layers: 128 + 64 neurons
    activation='relu',
    solver='adam',
    max_iter=50,
    random_state=42
)

# 5. Train Model
model.fit(X_train, y_train)

# 6. Predict
y_pred = model.predict(X_test)

# 7. Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 8. Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
plt.imshow(cm, cmap="Blues")
plt.title("Confusion Matrix")
plt.colorbar()
plt.xlabel("Predicted")
plt.ylabel("True")
plt.show()


