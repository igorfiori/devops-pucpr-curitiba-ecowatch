from app.services import buscar_dados_clima
from app.analyzer import classificar_treino
from jinja2 import Environment, FileSystemLoader

def gerar_html(temp, desc, recomendacao, classe_css):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')
    
    html_content = template.render(
        temp=temp,
        desc=desc,
        rec=recomendacao,
        classe=classe_css
    )
    
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    try:
        print("Buscando dados na Open-Meteo...")
        dados = buscar_dados_clima()
        
        temp_atual = dados['current_weather']['temperature']
        descricao, rec, css = classificar_treino(dados)
        
        gerar_html(temp_atual, descricao, rec, css)
        print("Pipeline executado: index.html gerado com sucesso!")
    except Exception as e:
        print(f"Falha no processo: {e}")