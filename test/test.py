import pytest
from unittest.mock import patch, mock_open, MagicMock

from backend.main import gerar_html 

# Teste 1: test_gerar_html_cria_arquivo
@patch("builtins.open", new_callable=mock_open)
def test_gerar_html_cria_arquivo(mock_file):
    gerar_html(25.5, "Céu limpo", "Treino ao ar livre recomendado", "sol-css")
    mock_file.assert_any_call("index.html", "w", encoding="utf-8")

# Teste 2: test_gerar_html_chama_environment
@patch("builtins.open", new_callable=mock_open)
@patch("backend.main.Environment") 
def test_gerar_html_chama_environment(mock_env, mock_file):
    mock_template = MagicMock()
    mock_env.return_value.get_template.return_value = mock_template
    mock_template.render.return_value = "<html>Texto Falso</html>" 
    
    gerar_html(15.0, "Frio", "Agasalhe-se", "frio-css")
    mock_env.return_value.get_template.assert_called_once_with('index.html')

# Teste 3: test_gerar_html_renderiza_variaveis
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

# Teste 4: test_gerar_html_salva_conteudo_correto
@patch("builtins.open", new_callable=mock_open)
@patch("backend.main.Environment") 
def test_gerar_html_salva_conteudo_correto(mock_env, mock_file):
    mock_template = MagicMock()
    mock_env.return_value.get_template.return_value = mock_template
    html_falso = "<h1>HTML Gerado pelo Jinja2</h1>"
    mock_template.render.return_value = html_falso
    
    gerar_html(20.0, "Nublado", "Fique em casa", "nuvem-css")
    
    mock_file().write.assert_called_once_with(html_falso)

# Teste 5: test_gerar_html_lida_com_valores_vazios
@patch("builtins.open", new_callable=mock_open)
@patch("backend.main.Environment") 
def test_gerar_html_lida_com_valores_vazios(mock_env, mock_file):
    mock_template = MagicMock()
    mock_env.return_value.get_template.return_value = mock_template
    mock_template.render.return_value = "<html>Vazio</html>"
    
    gerar_html(0.0, "", "", "")
    
    mock_template.render.assert_called_once_with(
        temp=0.0,
        desc="",
        rec="",
        classe=""
    )