import pickle
from flask import Flask, render_template, request


app = Flask(__name__)

scaler, modelo  = carregar_modelos() # Carrega os modelos padronizador e preditor.


#############
@app.route('/')
def home():
    """Rota principal - exibe o formulário"""
    return render_template('home.html')
    

#############
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



########################
def carregar_modelos():
    scaler = pickle.load(open('scaler.pkl', 'rb'))  # Carrega o scaler
    modelo_carregado = pickle.load(open('prediction_model.pkl', 'rb')) # Carrega o modelo principal
    modelo = modelo_carregado["model"]
    return scaler, modelo


########################
def fazer_previsao_salario(data, scaler, modelo):
    dados_padronizados = scaler.transform([list(data.values())]) # Aplica o padronizador
    output = modelo.predict(dados_padronizados)[0] # Previsão com o modelo
    formatted_output = round(output, 2) # Formata a saída
    return f"$ {formatted_output} [valor anual]" # Retorna o resultado formatado


if __name__ == "__main__":
    app.run()














