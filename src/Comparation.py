from plot_stats import plot_comparation
from process_data import comparing_goals
import json
import pandas as pd

def calc_comparation(df, x, y):
    final_positions = {
    1:"Palmeiras",2:"Gremio",3:"Atletico-MG",
    4:"Flamengo",5:"Botafogo",6:"RB Bragantino",
    7:"Fluminense",8:"Atletico Paranaense",
    9:"Internacional",10:"Fortaleza",11:"Sao Paulo",
    12:"Cuiaba",13:"Corinthians",14:"Cruzeiro",
    15:"Vasco DA Gama",16:"Bahia",17:"Santos",
    18:"Goias",19:"Coritiba",20:"America Mineiro"
    }

    plot_comparation(df, final_positions[x], final_positions[y])

#abrindo o json (Data) e transformando em um objeto pyhton
with open("data/fixtures.json") as f:
    raw_data = json.load(f)

fixtures = raw_data["response"]
df = pd.json_normalize(fixtures)
round_points = comparing_goals(df)


print("--- Análise de Dados Brasileirão 2023 ---\n")
print("Comparando pontuação entre 2 equipes")

while True:
    print("Selecione a primeira equipe que gostaria de analisar:\n")
    print("1 - Palmeiras\n2 - Grêmio\n3 - Atlético-MG\n4 - Flamengo\n5 - Botafogo\n6 - RB Bragantino\n7 - Fluminense\n8 - Athletico-PR\n9 - Internacional\n10 - Fortaleza\n" \
    "11 - São Paulo\n12 - Cuiaba\n13 - Corinthians\n14 - Cruzeiro\n15 - Vasco da Gama\n16 - Bahia\n17 - Santos\n18 - Goias\n19 - Coritiba\n20 - América-MG\n")
    valor1 = int(input("Posição:"))
    if 0 < valor1 < 21:
        break
    else:
        print("Valor inválido, tente novamente")

while True:
    print("Selecione a segunda equipe que gostaria de analisar:\n")
    print("1 - Palmeiras\n2 - Grêmio\n3 - Atlético-MG\n4 - Flamengo\n5 - Botafogo\n6 - RB Bragantino\n7 - Fluminense\n8 - Athletico-PR\n9 - Internacional\n10 - Fortaleza\n" \
    "11 - São Paulo\n12 - Cuiaba\n13 - Corinthians\n14 - Cruzeiro\n15 - Vasco da Gama\n16 - Bahia\n17 - Santos\n18 - Goias\n19 - Coritiba\n20 - América-MG\n")
    valor2 = int(input("Posição:"))
    if valor1 == valor2:
        print("As equipes devem ser diferentes.")
        continue
    if 0 < valor2 < 21:
        break
    else:
        print("Valor inválido, tente novamente")

calc_comparation(round_points, valor1, valor2)

print("Fim")