import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_goals_by_round(df_round_goals):
    plt.figure(figsize=(20,15))
    sns.barplot(data=df_round_goals, x="rodada_num", y="total_goals")
    plt.title("Total de Gols por Rodada - Brasileirão 2023", fontsize=16)
    plt.xlabel("Rodada")
    plt.ylabel("Total de Gols")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.5)
    plt.tight_layout()
    return plt.show()

def plot_goals_scored_conceded(df_teams, team_name):
    df_grouped = df_teams.groupby(["team", "round"])[["goals_scored", "goals_conceded"]].sum().reset_index()

    # Filtra os dados só para esse time
    df_time = df_grouped[df_grouped["team"] == team_name]

    # Cria o gráfico
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df_time, x="round", y="goals_scored", label="Gols Marcados", marker="o")
    sns.lineplot(data=df_time, x="round", y="goals_conceded", label="Gols Sofridos", marker="o")

    plt.title(f"Gols por Rodada - {team_name}")
    plt.xlabel("Rodada")
    plt.ylabel("Gols")
    plt.xticks(range(1, df_time["round"].max()+1))
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_comparation(df_round_points, team1, team2):
    teams = [team1, team2]
    df_comparation = df_round_points[df_round_points["team"].isin(teams)]

    plt.figure(figsize=(10,6))
    sns.lineplot(data=df_comparation, x="round", y="accumulated", hue="team", marker="o")
    plt.title("Pontuação acumulada por rodada")
    plt.xlabel("Rodada")
    plt.ylabel("Pontos")
    plt.grid(True)
    plt.tight_layout()
    plt.show()