import pandas as pd

df = pd.read_csv('data/movies.csv')

# Check for target movies
matrix = df[df['title'].str.contains('Matrix', case=False, na=False)]
fight = df[df['title'].str.contains('Fight Club', case=False, na=False)]

print("The Matrix:")
if len(matrix) > 0:
    print(matrix[['id', 'title', 'industry']].to_string())
else:
    print("NOT FOUND")

print("\nFight Club:")
if len(fight) > 0:
    print(fight[['id', 'title', 'industry']].to_string())
else:
    print("NOT FOUND")

print(f"\nDuplicate IDs in dataset: {df['id'].duplicated().sum()}")
print(f"Total movies: {len(df)}")

# Check if movie 1327862 exists
if 1327862 in df['id'].values:
    print(f"\nMovie ID 1327862: {df[df['id']==1327862]['title'].values[0]}")
