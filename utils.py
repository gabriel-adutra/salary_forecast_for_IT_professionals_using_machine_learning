import pickle


def carregar_modelos():
    """Carrega o modelo de machine learning e o scaler treinados"""
    scaler = pickle.load(open('scaler.pkl', 'rb'))  # Carrega o scaler
    modelo_carregado = pickle.load(open('prediction_model.pkl', 'rb')) # Carrega o modelo principal
    modelo = modelo_carregado["model"]
    return scaler, modelo


def fazer_previsao_salario(data, scaler, modelo):
    """Executa a previsão de salário usando o modelo carregado"""
    dados_padronizados = scaler.transform([list(data.values())]) # Aplica o padronizador
    output = modelo.predict(dados_padronizados)[0] # Previsão com o modelo
    formatted_output = round(output, 2) # Formata a saída
    return f"$ {formatted_output} [valor anual]" # Retorna o resultado formatado 