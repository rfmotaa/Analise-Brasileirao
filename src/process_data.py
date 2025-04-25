import pandas as pd

def process_goals_by_round(df):
    df_goals = df[["league.round","goals.home","goals.away"]].copy()

    df_goals["total_goals"] = df["goals.home"] + df["goals.away"]

    df_round_goals = df_goals.groupby("league.round")["total_goals"].sum().reset_index()

    df_round_goals["rodada_num"] = df_round_goals["league.round"].str.extract(r"(\d+)").astype(int)
    df_round_goals = df_round_goals.sort_values("rodada_num")

    return df_round_goals

def process_efficiency(df):
    df_matchs = df[["teams.home.name", "teams.away.name", "goals.home", "goals.away", "league.round"]].copy()
    df_matchs["round"] = df_matchs["league.round"].str.extract(r"(\d+)").astype(int)

    teams_list = {}

    for _, row in df_matchs.iterrows():
        home = row["teams.home.name"]
        away = row["teams.away.name"]
        g_home = row["goals.home"]
        g_away = row["goals.away"]
        round_ = row["round"]

        for team, scored, conceded in [
            (home, g_home, g_away),
            (away, g_away, g_home)
        ]:
            if team not in teams_list:
                teams_list[team] = []
            teams_list[team].append({
                "team": team,
                "round": round_,
                "goals_scored": scored,
                "goals_conceded": conceded
            })

    # Transforma corretamente em DataFrame
    df_teams = pd.DataFrame([item for sublist in teams_list.values() for item in sublist])
    return df_teams

def comparing_goals(df):
    df_games = df[["league.round","teams.home.name","teams.away.name","teams.home.winner","teams.away.winner"]].copy()
    df_games["round"] = df_games["league.round"].str.extract(r"(\d+)").astype(int)

    scores = []

    for _, row in df_games.iterrows():
        round = row["round"]
        home_team = row["teams.home.name"]
        home_result = row["teams.home.winner"]
        away_team = row["teams.away.name"]
        away_result = row["teams.away.winner"]

        home_point = 1
        away_point = 1

        if home_result == True:
            home_point = 3
            away_point = 0
        elif home_result == False:
            home_point = 0
            away_point = 3

        scores.append({"team":home_team,"round":round,"result":home_point})
        scores.append({"team":away_team,"round":round,"result":away_point})

    df_round_points = pd.DataFrame(scores)
    df_round_points = df_round_points.sort_values(by=["team","round"])

    df_round_points["accumulated"] = df_round_points.groupby("team")["result"].cumsum()

    return df_round_points