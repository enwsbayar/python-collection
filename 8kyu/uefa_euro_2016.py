# Finish the uefaEuro2016() function so it return string just like in the examples below:

# uefa_euro_2016(['Germany', 'Ukraine'],[2, 0]) # "At match Germany - Ukraine, Germany won!"
# uefa_euro_2016(['Belgium', 'Italy'],[0, 2]) # "At match Belgium - Italy, Italy won!"
# uefa_euro_2016(['Portugal', 'Iceland'],[1, 1]) # "At match Portugal - Iceland, teams played draw."

def uefa_euro_2016(teams, scores):
  team1, team2 = teams
  score1, score2 = scores
  
  if score1 > score2:
    return f"At match {team1} - {team2}, {team1} won!"
  elif score2 > score1:
    return f"At match {team1} - {team2}, {team2} won!"
  else:
    return f"At match {team1} - {team2}, teams played draw."