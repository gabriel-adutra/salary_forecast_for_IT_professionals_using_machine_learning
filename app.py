import warnings
from flask import Flask, render_template, request
from utils import carregar_modelos, fazer_previsao_salario

warnings.filterwarnings('ignore', category=UserWarning, module='sklearn')

app = Flask(__name__)


scaler, modelo = carregar_modelos()


#######
@app.route('/')
def home():
    """Rota principal - exibe o formulário"""
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
        return render_template("home.html", prediction_text=f"Entrada inválida. Erro: {e}")
    except ValueError:
        return render_template("home.html", prediction_text="Valor de experiência deve ser um número válido.")
    
    if any(value == '' for value in data.values()): # Valida se todos os campos estão preenchidos
        return render_template("home.html", prediction_text="Verifique se todos os campos estão preenchidos.")
    
    resultado_formatado = fazer_previsao_salario(data, scaler, modelo) # Faz a previsão e retorna o resultado formatado
    return render_template("home.html", prediction_text=resultado_formatado)





###################################
if __name__ == "__main__":
    app.run()














