from plot_stats import plot_goals_scored_conceded
from process_data import process_efficiency
import json
import pandas as pd

def calc_efficiency(games, position):
    final_positions = {
    1:"Palmeiras",2:"Gremio",3:"Atletico-MG",
    4:"Flamengo",5:"Botafogo",6:"RB Bragantino",
    7:"Fluminense",8:"Atletico Paranaense",
    9:"Internacional",10:"Fortaleza",11:"Sao Paulo",
    12:"Cuiaba",13:"Corinthians",14:"Cruzeiro",
    15:"Vasco DA Gama",16:"Bahia",17:"Santos",
    18:"Goias",19:"Coritiba",20:"America Mineiro"
    }

    plot_goals_scored_conceded(games, final_positions[position])

#abrindo o json (Data) e transformando em um objeto pyhton
with open("data/fixtures.json") as f:
    raw_data = json.load(f)

fixtures = raw_data["response"]
df = pd.json_normalize(fixtures)

matchs = process_efficiency(df)


sentinela = -1

while sentinela != "0":
    print("--- Análise de Dados Brasileirão 2023 ---\n")
    print("Gols pró e contra")
    print("Selecione a equipe que gostaria de analisar com base na posição final:\n")
    print("1 - Palmeiras\n2 - Grêmio\n3 - Atlético-MG\n4 - Flamengo\n5 - Botafogo\n6 - RB Bragantino\n7 - Fluminense\n8 - Athletico-PR\n9 - Internacional\n10 - Fortaleza\n" \
    "11 - São Paulo\n12 - Cuiaba\n13 - Corinthians\n14 - Cruzeiro\n15 - Vasco da Gama\n16 - Bahia\n17 - Santos\n18 - Goias\n19 - Coritiba\n20 - América-MG\n")
    valor = int(input("Posição:"))
    calc_efficiency(matchs, valor)
    sentinela = input("Deseja fazer uma nova análise?\nQualquer tecla - Sim\n0 - Não\n:")

print("Fim")