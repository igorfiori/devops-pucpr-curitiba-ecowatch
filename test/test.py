import pytest
from unittest.mock import patch, mock_open, MagicMock

# Apontando para a pasta certa: backend
from backend.main import gerar_html 

@patch("builtins.open", new_callable=mock_open)
def test_gerar_html_cria_arquivo(mock_file):
    gerar_html(25.5, "Céu limpo", "Treino ao ar livre recomendado", "sol-css")
    mock_file.assert_called_once_with("index.html", "w", encoding="utf-8")

# Apontando o patch para o backend também
@patch("backend.main.Environment") 
def test_gerar_html_chama_environment(mock_env):
    mock_template = MagicMock()
    mock_env.return_value.get_template.return_value = mock_template
    
    gerar_html(15.0, "Frio", "Agasalhe-se", "frio-css")
    mock_env.return_value.get_template.assert_called_once_with('index.html')

@patch("backend.main.Environment") 
def test_gerar_html_renderiza_variaveis(mock_env):
    mock_template = MagicMock()
    mock_env.return_value.get_template.return_value = mock_template
    
    gerar_html(30.0, "Muito Quente", "Hidrate-se bastante", "quente-css")
    
    mock_template.render.assert_called_once_with(
        temp=30.0,
        desc="Muito Quente",
        rec="Hidrate-se bastante",
        classe="quente-css"
    )