import pickle


def load_models():
    """Loads the trained machine learning model and scaler"""
    scaler = pickle.load(open('scaler.pkl', 'rb'))  # Loads the scaler
    loaded_model = pickle.load(open('prediction_model.pkl', 'rb')) # Loads the main model
    model = loaded_model["model"]
    return scaler, model


def predict_salary(data, scaler, model):
    """Executes salary prediction using the loaded model"""
    standardized_data = scaler.transform([list(data.values())]) # Applies the scaler
    output = model.predict(standardized_data)[0] # Prediction with the model
    formatted_output = round(output, 2) # Formats the output
    return f"$ {formatted_output} [annual value]" # Returns the formatted result 