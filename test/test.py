import os
from src.main import gerar_html

def test_gerar_html():
    gerar_html(22.5, "Céu limpo", "Ótimo dia para atividades ao ar livre", "ensolarado")
    
    assert os.path.exists("index.html")
    
    # Limpando o arquivo gerado pelo teste
    if os.path.exists("index.html"):
        os.remove("index.html")
