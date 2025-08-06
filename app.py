import warnings
from flask import Flask, render_template, request
from utils import load_models, predict_salary

warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')

scaler, model = load_models()

app = Flask(__name__)

#######
@app.route('/')
def home():
    """Main route - displays the form"""
    return render_template('home.html')
    

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
        return render_template("home.html", prediction_text=f"Invalid input. Error: {e}")
    except ValueError:
        return render_template("home.html", prediction_text="Experience value must be a valid number.")
    
    if any(value == '' for value in data.values()): # Validates if all fields are filled
        return render_template("home.html", prediction_text="Please check if all fields are filled.")
    
    formatted_result = predict_salary(data, scaler, model) # Makes prediction and returns formatted result
    return render_template("home.html", prediction_text=formatted_result)


###################################
if __name__ == "__main__":
    app.run()














