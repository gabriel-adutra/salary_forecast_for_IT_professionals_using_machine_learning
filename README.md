# Salary Forecast for IT Professionals using Machine Learning

## 📊 Overview

This project implements a machine learning-based salary prediction system for IT professionals. It combines data science techniques with web application development to provide an interactive platform where users can input their professional characteristics and receive salary predictions.

## 🚀 Features

- **Machine Learning Model**: Trained on IT professional salary data
- **Web Application**: Interactive Flask-based web interface
- **Real-time Predictions**: Instant salary forecasts based on user input
- **Responsive Design**: Modern and user-friendly interface
- **Data Visualization**: Insights into salary trends and factors

## 🛠️ Technology Stack

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Gunicorn
- **Data Processing**: Jupyter Notebook

## 📁 Project Structure

```
salary_forecast_for_IT_professionals_using_machine_learning/
├── app.py                          # Main Flask application
├── data_science_and_ML_model_creation.ipynb  # Jupyter notebook for model development
├── dataset.csv                     # Training dataset
├── prediction_model.pkl            # Trained ML model
├── scaler.pkl                      # Data scaler for preprocessing
├── requirements.txt                # Python dependencies
├── static/
│   └── styles.css                  # CSS styles
└── templates/
    └── home.html                   # Main HTML template
```

## 🚀 Quick Start

### Prerequisites

- Python 3.12 or higher
- Conda (recommended) or pip

### Installation

1. **Create and activate virtual environment**
   ```bash
   conda create --name salary-forecast python=3.12
   conda activate salary-forecast
   ```

2. **Install dependencies**
   ```bash
   conda install pip
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   gunicorn -w 4 app:app
   ```

4. **Access the application**
   Open your browser and navigate to `http://localhost:8000`

## 📊 Model Information

The machine learning model is trained on comprehensive IT professional salary data and considers the following factors:

- **Country**: Geographic location (15 countries including US, UK, Germany, Brazil, etc.)
- **Education Level**: Academic background (Bachelor's, Master's, Post grad, etc.)
- **Developer Type**: Professional role (Back-end, Full-stack, Data Scientist, DevOps, etc.)
- **Years of Professional Experience**: Time in the field

## 🎯 Usage

1. Navigate to the web application
2. Fill in your professional information
3. Submit the form to receive your salary prediction
4. View detailed insights and recommendations

## 🔧 Development

### Model Development
The machine learning model was developed in the Jupyter notebook `data_science_and_ML_model_creation.ipynb`, which includes:
- Data exploration and preprocessing
- Feature engineering
- Model training and validation
- Performance evaluation

### Web Application
The Flask application (`app.py`) provides:
- Web interface with form handling
- Input validation and preprocessing
- Model integration for predictions
- HTML template rendering