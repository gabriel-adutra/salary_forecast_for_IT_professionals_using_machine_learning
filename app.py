import warnings
import logging
from flask import Flask, render_template, request
from utils import load_salary_prediction_models, predict_salary

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)

warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')

salary_scaler, salary_prediction_model = load_salary_prediction_models()

app = Flask(__name__)

#######
@app.route('/')
def home():
    """Main route - displays the form"""
    log.info("HOME endpoint called - no arguments received.")
    result = render_template('home.html')
    log.info("HOME endpoint returning HTML template.")
    return result
    

#######
@app.route('/predict_salary', methods=['POST'])
def predict_salary():

    log.info("PREDICT_SALARY endpoint called - processing form data.")
    
    try:
        data = {
            'Country': request.form['Country'],
            'education': request.form['education'],
            'devtype': request.form['devtype'],
            'experience': float(request.form['experience']),
        }
        log.info(f"PREDICT_SALARY - Input data received: {data}")
    except KeyError as e:
        log.error(f"PREDICT_SALARY - KeyError in form data: {e}")
        result = render_template("home.html", prediction_text=f"Invalid input. Error: {e}")
        log.info("PREDICT_SALARY returning error template")
        return result
    except ValueError:
        log.error("PREDICT_SALARY - ValueError: experience must be a valid number")
        result = render_template("home.html", prediction_text="Experience value must be a valid number.")
        log.info("PREDICT_SALARY returning error template")
        return result
    
    if any(value == '' for value in data.values()): # Validates if all fields are filled
        log.warning("PREDICT_SALARY - Empty fields detected in form data")
        result = render_template("home.html", prediction_text="Please check if all fields are filled.")
        log.info("PREDICT_SALARY returning validation error template")
        return result
    
    formatted_result = predict_salary(data, salary_scaler, salary_prediction_model) # Makes prediction and returns formatted result
    log.info(f"PREDICT_SALARY - Prediction completed: {formatted_result}")
    result = render_template("home.html", prediction_text=formatted_result)
    log.info("PREDICT_SALARY returning prediction result template")
    return result


###################################
if __name__ == "__main__":
    app.run()














