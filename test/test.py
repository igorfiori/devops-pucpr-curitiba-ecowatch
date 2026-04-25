import pytest
from unittest.mock import patch, mock_open, MagicMock

# Apontando para a pasta certa: backend
from backend.main import gerar_html 

# Teste 1: Agora validamos se ELE GRAVOU o arquivo em algum momento, ignorando a leitura do template
@patch("builtins.open", new_callable=mock_open)
def test_gerar_html_cria_arquivo(mock_file):
    gerar_html(25.5, "Céu limpo", "Treino ao ar livre recomendado", "sol-css")
    mock_file.assert_any_call("index.html", "w", encoding="utf-8")

# Teste 2: Mockamos o open aqui também para ele não tentar criar arquivo de verdade na máquina do GitHub
@patch("builtins.open", new_callable=mock_open)
@patch("backend.main.Environment") 
def test_gerar_html_chama_environment(mock_env, mock_file):
    mock_template = MagicMock()
    mock_env.return_value.get_template.return_value = mock_template
    # Avisamos o mock que o render deve devolver um texto, para evitar o TypeError
    mock_template.render.return_value = "<html>Texto Falso</html>" 
    
    gerar_html(15.0, "Frio", "Agasalhe-se", "frio-css")
    mock_env.return_value.get_template.assert_called_once_with('index.html')

# Teste 3: Mesma correção do open e do texto do render
@patch("builtins.open", new_callable=mock_open)
@patch("backend.main.Environment") 
def test_gerar_html_renderiza_variaveis(mock_env, mock_file):
    mock_template = MagicMock()
    mock_env.return_value.get_template.return_value = mock_template
    mock_template.render.return_value = "<html>Texto Falso</html>"
    
    gerar_html(30.0, "Muito Quente", "Hidrate-se bastante", "quente-css")
    
    mock_template.render.assert_called_once_with(
        temp=30.0,
        desc="Muito Quente",
        rec="Hidrate-se bastante",
        classe="quente-css"
    )