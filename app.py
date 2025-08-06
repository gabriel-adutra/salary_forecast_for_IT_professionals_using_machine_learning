import warnings
import logging
from flask import Flask, render_template, request
from utils import load_salary_prediction_models, make_salary_prediction

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
    result = render_template('home.html')
    log.info("HOME endpoint - HTML template returned")
    return result
    

#######
@app.route('/predict_salary', methods=['POST'])
def predict_salary():
    try:
        data = {
            'Country': request.form['Country'],
            'education': request.form['education'],
            'devtype': request.form['devtype'],
            'experience': float(request.form['experience']),
        }
    except KeyError as e:
        log.error(f"PREDICT_SALARY - Missing form field: {e}")
        return render_template("home.html", prediction_text=f"Invalid input. Error: {e}")
    except ValueError:
        log.error("PREDICT_SALARY - Invalid experience value")
        return render_template("home.html", prediction_text="Experience value must be a valid number.")
    
    # Validate all fields are filled
    if any(value == '' for value in data.values()):
        log.warning("PREDICT_SALARY - Empty fields detected")
        return render_template("home.html", prediction_text="Please check if all fields are filled.")
    
    # Make prediction
    formatted_result = make_salary_prediction(data, salary_scaler, salary_prediction_model)
    
    # Log success and return result
    log.info(f"PREDICT_SALARY - Success: {formatted_result}")
    return render_template("home.html", prediction_text=formatted_result)


###################################
if __name__ == "__main__":
    app.run()














