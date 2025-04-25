import requests
import os
import json

URL = "https://v3.football.api-sports.io/fixtures?league=71&season=2023"

headers = {
    "x-apisports-key": os.getenv("API_FOOTBALL_KEY")
}

# Função que busca os dados das partidas do Brasileirao 2023
def search_data():
    response = requests.get(URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Erro durante a busca de dados: {response.status_code}")
        return None
    
# Função que salva os dados em JSON
def save_json(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as arquivo:
        json.dump(data, arquivo, indent=2, ensure_ascii=False)
    print(f"Dados salvos em {path}")

if __name__ == "__main__":
    data = search_data()
    if data:
        save_json(data, "data/fixtures.json")