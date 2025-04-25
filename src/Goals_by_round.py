from process_data import process_goals_by_round
from plot_stats import plot_goals_by_round
import json
import pandas as pd

#abrindo o json (Data) e transformando em um objeto pyhton
with open("data/fixtures.json") as f:
    raw_data = json.load(f)

fixtures = raw_data["response"]
df = pd.json_normalize(fixtures)

goals_round = process_goals_by_round(df)
plot_goals_by_round(goals_round)