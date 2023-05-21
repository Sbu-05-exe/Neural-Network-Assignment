import pandas as pd
import numpy as np

def clean_data(df):
	feature_columns = ["attendance", "home_team_name", "away_team_name", "Pre-Match PPG (Home)", "Pre-Match PPG (Away)"
	                ,"home_ppg", "away_ppg","home_team_goal_count", "away_team_goal_count", "home_team_goal_count_half_time", "away_team_goal_count_half_time"
	                ,"home_team_corner_count","away_team_corner_count","home_team_yellow_cards", "away_team_yellow_cards"
	                ,"home_team_red_cards", "away_team_red_cards", "home_team_shots", "away_team_shots", "home_team_shots_on_target", "away_team_shots_on_target"
	                ,"home_team_fouls", "away_team_fouls", "home_team_possession","away_team_possession"]
	n_features = len(feature_columns) # should equal to 26 when we add the result feature vector
	# print(n_features)
	cleaned_data = df[feature_columns]
	return cleaned_data


df = pd.read_csv("england-premier-league-matches-2018-to-2019-stats.csv");

df = clean_data(df);

print(df.info())

team_names = df.home_team_name.unique()

team_data = {}


for team in team_names:
	team_data[team] = { 
		"games_played" : 0,
		"goals_scored" : 0,
		"total_shots" : 0,
		"total_shots_on_target" : 0,
		"total_shots_saved" : 0,
		"goals_conceded": 0,
		"average_possession": 0,
		"total_fouls": 0,
		"total_yellow_cards": 0,
		"total_red_cards": 0,
		"total_wins": 0,
		"total_draws": 0,
		"total_losses": 0 
	}

print()
print(df.loc[0])
# for i in range(len(df)):
# 	if (team_data) = 
	
	# print()
	# print(f"{i} {df.loc[]}")
	# print(df["status"][index])
# print(data["home_team_name"])

