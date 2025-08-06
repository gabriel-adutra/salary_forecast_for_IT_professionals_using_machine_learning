import pickle


def load_salary_prediction_models():
    """Loads the trained machine learning model and scaler for salary prediction"""
    salary_scaler = pickle.load(open('scaler.pkl', 'rb'))  # Loads the scaler
    loaded_model = pickle.load(open('prediction_model.pkl', 'rb')) # Loads the main model
    salary_prediction_model = loaded_model["model"]
    return salary_scaler, salary_prediction_model


def predict_salary(data, salary_scaler, salary_prediction_model):
    """Executes salary prediction using the loaded model"""
    standardized_data = salary_scaler.transform([list(data.values())]) # Applies the scaler
    output = salary_prediction_model.predict(standardized_data)[0] # Prediction with the model
    formatted_output = round(output, 2) # Formats the output
    return f"$ {formatted_output} [annual value]" # Returns the formatted result 