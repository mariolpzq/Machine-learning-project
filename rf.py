from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from imblearn.over_sampling import SMOTE

# Load the dataset
data = pd.read_csv('medals_by_country.csv')


X = data[['Total_medals', 'Number of Athletes', 'Number of events']]
data['target'] = data['isHost']  # Create target variable

y = data['target']  # Target variable indicating host country advantage (0 or 1)

# Splitting the dataset into 70% training, 15% validation, and 15% test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42, stratify=y_temp)

# Apply SMOTE to the training data
smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Set up the Random Forest model with class weights
rf_model = RandomForestClassifier(random_state=42)
# Define a parameter grid for hyperparameter tuning
param_grid = {
    'n_estimators': [100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'class_weight': ['balanced']  # Adjust weights for classes
}

# Set up the grid search
grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=5, scoring='f1', verbose=2)

# Fit the model
grid_search.fit(X_train_resampled, y_train_resampled)

# Print best parameters
print(f'Best parameters: {grid_search.best_params_}')

# Use the best estimator for predictions
best_rf_model = grid_search.best_estimator_

# Validate the model on the validation set
y_val_pred = best_rf_model.predict(X_val)
val_accuracy = accuracy_score(y_val, y_val_pred)
print(f'Validation Accuracy: {val_accuracy}')

# Final evaluation on the test set
y_test_pred = best_rf_model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
conf_matrix = confusion_matrix(y_test, y_test_pred)

print(f'Test Accuracy: {test_accuracy}')
print('Confusion Matrix:')
print(conf_matrix)
print(classification_report(y_test, y_test_pred))
