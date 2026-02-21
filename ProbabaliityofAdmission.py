# Example: scripts/quick_admission_ann.py
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

def find_target_column(df):
    df.columns = df.columns.str.strip()
    normalized = {c: c.strip().lower().replace('_',' ').replace('-', ' ') for c in df.columns}
    candidates = ['chance of admit', 'chance_of_admit', 'chance', 'admit', 'chance of admittance']
    for cand in candidates:
        for orig, norm in normalized.items():
            if cand == norm or cand in norm:
                return orig
    raise KeyError(f"Target not found. Available columns: {list(df.columns)}")

# load (use repo-local CSV)
df = pd.read_csv('Admission_Predict_Ver1.1.csv')
df.columns = df.columns.str.strip()

# find target robustly and drop serial/id if present
target = find_target_column(df)
serial_cols = [c for c in df.columns if 'serial' in c.lower() or c.lower() in ('id','serial no.')]
df = df.drop(columns=serial_cols, errors='ignore')

X = df.drop(columns=[target])
y = df[target]

# train/test split and scaling
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

results = {}

# 1) Ridge baseline (uses scaled data)
ridge = Ridge(alpha=1.0).fit(X_train_s, y_train)
y_pred_ridge = ridge.predict(X_test_s)
results['Ridge'] = {
    'MAE': mean_absolute_error(y_test, y_pred_ridge),
    'MSE': mean_squared_error(y_test, y_pred_ridge),
    'R2' : r2_score(y_test, y_pred_ridge),
    'y_pred': y_pred_ridge
}
print('Ridge MAE:', results['Ridge']['MAE'])

# 2) Random Forest (trained on unscaled features)
rf = RandomForestRegressor(n_estimators=200, random_state=42).fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
results['RandomForest'] = {
    'MAE': mean_absolute_error(y_test, y_pred_rf),
    'MSE': mean_squared_error(y_test, y_pred_rf),
    'R2' : r2_score(y_test, y_pred_rf),
    'y_pred': y_pred_rf
}
print('Random Forest MAE:', results['RandomForest']['MAE'])

# 3) Small ANN (uses scaled data)
model = Sequential([
    Dense(32, activation='relu', input_shape=(X_train_s.shape[1],)),
    Dense(16, activation='relu'),
    Dense(1, activation='linear')
])
model.compile(optimizer='adam', loss='mse')
es = EarlyStopping(patience=8, restore_best_weights=True)
model.fit(X_train_s, y_train, validation_split=0.1, epochs=100, batch_size=16, callbacks=[es], verbose=0)
y_pred_ann = model.predict(X_test_s).ravel()
results['ANN'] = {
    'MAE': mean_absolute_error(y_test, y_pred_ann),
    'MSE': mean_squared_error(y_test, y_pred_ann),
    'R2' : r2_score(y_test, y_pred_ann),
    'y_pred': y_pred_ann
}
print('ANN MAE:', results['ANN']['MAE'])

# Compute classification-style accuracy by thresholding at 0.5 (admit if >= 0.5)
y_test_bin = (y_test.values >= 0.5).astype(int)
for name, info in results.items():
    y_pred_bin = (np.array(info['y_pred']) >= 0.5).astype(int)
    acc = accuracy_score(y_test_bin, y_pred_bin)
    results[name]['Accuracy@0.5'] = acc
    print(f"{name} Accuracy@0.5: {acc:.4f}")

# Summary comparison
print("\nSummary (lower MAE better, higher R2/Accuracy better):")
best_mae = min(results.items(), key=lambda kv: kv[1]['MAE'])[0]
best_r2 = max(results.items(), key=lambda kv: kv[1]['R2'])[0]
best_acc = max(results.items(), key=lambda kv: kv[1]['Accuracy@0.5'])[0]

for name, info in results.items():
    print(f"{name}: MAE={info['MAE']:.4f}, MSE={info['MSE']:.4f}, R2={info['R2']:.4f}, Acc@0.5={info['Accuracy@0.5']:.4f}")

print(f"\nBest by MAE: {best_mae}")
print(f"Best by R2: {best_r2}")
print(f"Best by Accuracy@0.5: {best_acc}")
