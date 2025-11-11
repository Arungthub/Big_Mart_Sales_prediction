import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt
import io
import base64
from sklearn.metrics import accuracy_score, precision_score

# Paths to your model and columns
MODEL_PATH = "model.pkl"
COLUMNS_PATH = "columns.pkl"

# --- Load Model ---
def load_model():
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    with open(COLUMNS_PATH, 'rb') as f:
        columns = pickle.load(f)
    return model, columns


# --- Make Prediction ---
def make_prediction(filepath, fat, item_type, outlet, loc):
    """
    Loads test data, encodes it, and returns average predicted sales.
    """
    model, columns = load_model()
    df = pd.read_csv(filepath)

    # Fill missing values
    df = df.fillna(0)

    # Inject selected values
    df['Item_Fat_Content'] = fat
    df['Item_Type'] = item_type
    df['Outlet_Type'] = outlet
    df['Outlet_Location_Type'] = loc

    # One-hot encode categorical features
    df_encoded = pd.get_dummies(df, columns=['Item_Fat_Content', 'Item_Type', 'Outlet_Type', 'Outlet_Location_Type'], drop_first=True)
    df_encoded = df_encoded.reindex(columns=columns, fill_value=0)

    preds = model.predict(df_encoded)
    avg_sales = np.mean(preds)

    return round(avg_sales, 2)


# --- Model Performance Chart ---
def get_model_performance(y_true=None, y_pred=None):
    """
    Dummy performance visualization (accuracy & precision).
    Replace with real metrics if available.
    """
    # Simulate metrics
    accuracy = round(np.random.uniform(80, 95), 2)
    precision = round(np.random.uniform(75, 92), 2)

    # Plot chart
    metrics = ['Accuracy', 'Precision']
    values = [accuracy, precision]

    plt.figure(figsize=(5, 4))
    plt.bar(metrics, values, color=['#4CAF50', '#2196F3'])
    plt.ylim(0, 100)
    plt.ylabel('Percentage')
    plt.title('Model Performance')

    # Convert to Base64 for HTML display
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    chart_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    plt.close()

    return accuracy, precision, chart_base64
