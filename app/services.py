import requests

def buscar_dados_clima():
    """Busca os dados do clima atual em Curitiba usando Open-Meteo (Sem API Key)"""
    url = "https://api.open-meteo.com/v1/forecast?latitude=-25.4284&longitude=-49.2733&current_weather=true"
    
    response = requests.get(url)
    response.raise_for_status()
    return response.json()