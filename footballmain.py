from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Initialize Spark Session
spark = SparkSession.builder.appName("Football Player Performance Analysis").getOrCreate()

# Sample DataFrame with 20 football players
data = [
    ('Lionel Messi', 'Paris Saint-Germain', 'Forward', 25, 18, 30),
    ('Cristiano Ronaldo', 'Al Nassr', 'Forward', 22, 10, 28),
    ('Neymar Jr', 'Al Hilal', 'Forward', 15, 12, 25),
    ('Kevin De Bruyne', 'Manchester City', 'Midfielder', 10, 25, 27),
    ('Robert Lewandowski', 'Barcelona', 'Forward', 30, 5, 29),
    ('Luka Modric', 'Real Madrid', 'Midfielder', 8, 18, 32),
    ('Kylian Mbappe', 'Paris Saint-Germain', 'Forward', 28, 7, 26),
    ('Erling Haaland', 'Manchester City', 'Forward', 35, 4, 30),
    ('Mohamed Salah', 'Liverpool', 'Forward', 20, 15, 30),
    ('Virgil van Dijk', 'Liverpool', 'Defender', 4, 2, 32),
    ('Sergio Ramos', 'Paris Saint-Germain', 'Defender', 3, 1, 29),
    ('Jude Bellingham', 'Real Madrid', 'Midfielder', 11, 7, 31),
    ('Bruno Fernandes', 'Manchester United', 'Midfielder', 9, 10, 30),
    ('Harry Kane', 'Bayern Munich', 'Forward', 24, 6, 28),
    ('Raheem Sterling', 'Chelsea', 'Forward', 12, 9, 27),
    ('Karim Benzema', 'Al Ittihad', 'Forward', 18, 6, 26),
    ('Thiago Silva', 'Chelsea', 'Defender', 2, 1, 28),
    ('Gerard Pique', 'Retired', 'Defender', 1, 0, 30),
    ('Paul Pogba', 'Juventus', 'Midfielder', 5, 8, 25),
    ('Andrew Robertson', 'Liverpool', 'Defender', 1, 9, 31)
]

columns = ['player_name', 'team', 'position', 'goals_scored', 'assists', 'matches_played']
df = spark.createDataFrame(data, columns)

# Function 1: Get the top goal scorer
def get_top_goal_scorer(df):
    return df.orderBy(F.desc('goals_scored')).limit(1).collect()[0]['player_name']

# Function 2: Get the player with the most assists
def get_top_assist_provider(df):
    return df.orderBy(F.desc('assists')).limit(1).collect()[0]['player_name']

# Function 3: Get the player with the highest goal-to-match ratio
def get_best_goal_per_match_ratio(df):
    df = df.withColumn('goal_per_match_ratio', F.col('goals_scored') / F.col('matches_played'))
    return df.orderBy(F.desc('goal_per_match_ratio')).limit(1).collect()[0]['player_name']

# Function 4: Get the total goals scored by all players
def get_total_goals(df):
    return df.agg(F.sum('goals_scored').alias('total_goals')).collect()[0]['total_goals']

# Function 5: Get the total assists provided by all players
def get_total_assists(df):
    return df.agg(F.sum('assists').alias('total_assists')).collect()[0]['total_assists']

# Function 6: Get the team with the most goals
def get_team_with_most_goals(df):
    return df.groupBy('team').agg(F.sum('goals_scored').alias('team_goals')).orderBy(F.desc('team_goals')).limit(1).collect()[0]['team']


# Calling the functions and displaying results
print("Top Goal Scorer:", get_top_goal_scorer(df))
print("Top Assist Provider:", get_top_assist_provider(df))
print("Player with Best Goal-to-Match Ratio:", get_best_goal_per_match_ratio(df))
print("Total Goals Scored:", get_total_goals(df))
print("Total Assists Provided:", get_total_assists(df))
print("Team with Most Goals:", get_team_with_most_goals(df))
