def interpretar_codigo_clima(codigo):
    """Traduz o código WMO da Open-Meteo para texto"""
    if codigo == 0:
        return "Céu limpo"
    elif 1 <= codigo <= 3:
        return "Nublado ou parcialmente nublado"
    elif 51 <= codigo <= 99:
        return "Chuva ou tempestade"
    else:
        return "Clima instável"

def classificar_treino(dados):
    """Analisa se o clima permite treinar na Black Trainer ou no Barigui"""
    clima_atual = dados.get('current_weather', {})
    temp = clima_atual.get('temperature', 0)
    codigo_clima = clima_atual.get('weathercode', 0)
    
    descricao = interpretar_codigo_clima(codigo_clima)
    
    if codigo_clima >= 51 or temp < 10:
        return descricao, " Treino Indoor (Vá para a Black Trainer!)", "danger"
    elif 15 <= temp <= 26:
        return descricao, " Treino Outdoor (Parque Barigui liberado!)", "success"
    else:
        return descricao, " Atenção (Clima instável, prepare o casaco)", "warning"