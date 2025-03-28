import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_and_save_csv():
    url = "https://exemplo.com"  # Substitui pela URL real
    response = requests.get(url)
    
    if response.status_code != 200:
        raise Exception("Erro ao acessar a página")

    soup = BeautifulSoup(response.text, "html.parser")
    
    # Exemplo: coletar títulos e links de artigos
    data = []
    for article in soup.find_all("article"):
        title = article.find("h2").text.strip()
        link = article.find("a")["href"]
        data.append({"Título": title, "Link": link})

    # Salvar os dados num CSV
    df = pd.DataFrame(data)
    df.to_csv("dados.csv", index=False, encoding="utf-8")

    return "Scraper executado com sucesso!"
