import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix 
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt
import seaborn as sns


 # evaluation metrics

# Load the dataset
data = pd.read_csv('filtered_medals_by_country.csv')

# Selecting the relevant features as mentioned in the PDF
X = data[[ 'Total_medals', 'Number of Athletes', 'Number of events']]  # Replace with actual feature column names if needed
data['target'] = data['isHost']

y = data['target']  # Assuming 'target' is the column indicating host country advantage (0 or 1)

# Splitting the dataset into 70% training, 15% validation, and 15% test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# smote = SMOTE(random_state=42)
# X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

# Initialize the Logistic Regression model
model = LogisticRegression()

# Train the model using the training set
model.fit(X_train, y_train)

# Validate the model on the validation set
y_val_pred = model.predict(X_val)
val_accuracy = accuracy_score(y_val, y_val_pred)
print(f'Validation Accuracy: {val_accuracy}')

# Final evaluation on the test set
y_test_pred = model.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
conf_matrix = confusion_matrix(y_test, y_test_pred)

print(f'Test Accuracy: {test_accuracy}')
print('Confusion Matrix:')
print(conf_matrix)
print(classification_report(y_test, y_test_pred))

ax= plt.subplot()

sns.heatmap(conf_matrix, annot=True, fmt='g', ax=ax)

ax.set_xlabel('Predicted labels',fontsize=15)
ax.set_ylabel('True labels',fontsize=15)
ax.set_title('Confusion Matrix',fontsize=15)
ax.xaxis.set_ticklabels(['isNotHost', 'isHost'],fontsize=15)
ax.yaxis.set_ticklabels(['isNotHost', 'isHost'],fontsize=15)
plt.show()


TP= conf_matrix[1,1]
FP= conf_matrix[0,1]
precision = TP/(TP+FP)




print('The precision of the model is: ',precision)