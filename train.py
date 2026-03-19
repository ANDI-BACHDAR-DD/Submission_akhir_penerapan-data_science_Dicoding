import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score, classification_report
import joblib

# 1. Load Data
df = pd.read_csv('data.csv', sep=';')

# 2. Data Preparation
# Drop 'Enrolled' from target for binary classification (Graduate vs Dropout)
df = df[df['Status'] != 'Enrolled'].copy()

# Binary Target: Dropout = 1, Graduate = 0
df['Target'] = df['Status'].apply(lambda x: 1 if x == 'Dropout' else 0)
df = df.drop('Status', axis=1)

# Feature engineering: Academic Success Rate (Approved / Enrolled)
# adding small epsilon to avoid division by zero
df['approved_ratio_1st_sem'] = df['Curricular_units_1st_sem_approved'] / (df['Curricular_units_1st_sem_enrolled'] + 1e-5)
df['approved_ratio_2nd_sem'] = df['Curricular_units_2nd_sem_approved'] / (df['Curricular_units_2nd_sem_enrolled'] + 1e-5)
# Cap ratio at 1.0 just in case
df['approved_ratio_1st_sem'] = df['approved_ratio_1st_sem'].clip(upper=1.0)
df['approved_ratio_2nd_sem'] = df['approved_ratio_2nd_sem'].clip(upper=1.0)

X = df.drop('Target', axis=1)
y = df['Target']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Standardize
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Modeling
print("--- Logistic Regression ---")
lr = LogisticRegression(class_weight='balanced', random_state=42, max_iter=1000)
lr.fit(X_train_scaled, y_train)
y_pred_lr = lr.predict(X_test_scaled)
print(f"Accuracy: {accuracy_score(y_test, y_pred_lr):.4f}")
print(f"Recall: {recall_score(y_test, y_pred_lr):.4f}")
print(f"F1: {f1_score(y_test, y_pred_lr):.4f}")

print("\n--- Random Forest ---")
rf = RandomForestClassifier(class_weight='balanced', random_state=42, n_estimators=100)
rf.fit(X_train_scaled, y_train)
y_pred_rf = rf.predict(X_test_scaled)
print(f"Accuracy: {accuracy_score(y_test, y_pred_rf):.4f}")
print(f"Recall: {recall_score(y_test, y_pred_rf):.4f}")
print(f"F1: {f1_score(y_test, y_pred_rf):.4f}")

# Feature Importance from Random Forest
print("\n--- Feature Importance (Top 10) ---")
importances = pd.DataFrame({
    'Feature': X.columns,
    'Importance': rf.feature_importances_
}).sort_values('Importance', ascending=False)
print(importances.head(10))

# Custom Insight logic to find hidden correlations
# e.g., tuition fees up to date vs dropout
dropout_rate_debtor = df[df['Debtor'] == 1]['Target'].mean()
dropout_rate_no_debtor = df[df['Debtor'] == 0]['Target'].mean()
print(f"\nDropout rate for Debtors: {dropout_rate_debtor:.2f}")
print(f"Dropout rate for Non-Debtors: {dropout_rate_no_debtor:.2f}")

dropout_rate_tuition = df[df['Tuition_fees_up_to_date'] == 0]['Target'].mean()
dropout_rate_no_tuition = df[df['Tuition_fees_up_to_date'] == 1]['Target'].mean()
print(f"Dropout rate for Tuition NOT up to date: {dropout_rate_tuition:.2f}")
print(f"Dropout rate for Tuition UP to date: {dropout_rate_no_tuition:.2f}")

# Save the best model (Random Forest is usually better at capturing non-linearities, but let's save the pipeline)
pipeline = {
    'scaler': scaler,
    'model': rf,
    'features': list(X.columns)
}
joblib.dump(pipeline, 'model.pkl')
print("\nModel saved to model.pkl")
