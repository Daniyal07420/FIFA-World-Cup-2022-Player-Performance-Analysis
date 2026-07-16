# =====================================================
# FIFA World Cup 2022 Player Performance Analysis
# Import, Load Dataset, Data Cleaning & Overview
# =====================================================

# -------------------------------
# 1. Import Required Libraries
# -------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Chart Style
plt.style.use('ggplot')

# -------------------------------
# 2. Load Dataset
# -------------------------------

df = pd.read_csv("Football dataset 2022.csv")

print("="*70)
print(" FIFA WORLD CUP 2022 PLAYER PERFORMANCE ANALYSIS ")
print("="*70)

# -------------------------------
# 3. First Five Rows
# -------------------------------

print("\nFirst Five Rows\n")
print(df.head())

# -------------------------------
# 4. Dataset Information
# -------------------------------

print("\nDataset Shape")
print(df.shape)

print("\nDataset Size")
print(df.size)

print("\nColumn Names")
print(df.columns.tolist())

print("\nData Types")
print(df.dtypes)

print("\nDataset Information")
print(df.info())

# -------------------------------
# 5. Missing Values
# -------------------------------

print("\nMissing Values")
print(df.isnull().sum())

# -------------------------------
# 6. Duplicate Values
# -------------------------------

duplicates = df.duplicated().sum()

print("\nDuplicate Rows :", duplicates)

# Remove Duplicates

df = df.drop_duplicates()

print("Dataset Shape After Removing Duplicates :", df.shape)

# -------------------------------
# 7. Unique Values
# -------------------------------

print("\nUnique Values")

print(df.nunique())

# -------------------------------
# 8. Summary Statistics
# -------------------------------

print("\nSummary Statistics")

print(df.describe())

# -------------------------------
# 9. Mean
# -------------------------------

print("\nMean")

print(df.mean(numeric_only=True))

# -------------------------------
# 10. Median
# -------------------------------

print("\nMedian")

print(df.median(numeric_only=True))

# -------------------------------
# 11. Mode
# -------------------------------

print("\nMode")

print(df.mode())

# =====================================================
# DESCRIPTIVE ANALYSIS
# =====================================================

print("\n")
print("="*70)
print("DESCRIPTIVE ANALYSIS")
print("="*70)

# Total Players

print("\nTotal Players :", df['player'].nunique())

# Total Teams

print("Total Teams :", df['team'].nunique())

# Total Positions

print("Total Positions :", df['position_group'].nunique())

# Average Offensive Value

print("Average Offensive Value :", round(df['offensive_value'].mean(),2))

# Average Defensive Value

print("Average Defensive Value :", round(df['defensive_value'].mean(),2))

# Average VAEP Value

print("Average VAEP Value :", round(df['vaep_value'].mean(),2))

# Average Minutes

print("Average Minutes Played :", round(df['minutes'].mean(),2))

# Average xG per90

print("Average xG per90 :", round(df['xg_per90'].mean(),2))

# =====================================================
# TOP PLAYERS
# =====================================================

print("\nTop 5 Offensive Players")

top_offense = df.sort_values(
    by="offensive_value",
    ascending=False
).head(5)

print(top_offense[['player','team','offensive_value']])

print("\nTop 5 Defensive Players")

top_defense = df.sort_values(
    by="defensive_value",
    ascending=False
).head(5)

print(top_defense[['player','team','defensive_value']])

print("\nTop 5 Overall Players")

top_vaep = df.sort_values(
    by="vaep_value",
    ascending=False
).head(5)

print(top_vaep[['player','team','vaep_value']])

# =====================================================
# BEST PLAYERS
# =====================================================

best_offense = df.loc[df['offensive_value'].idxmax()]

print("\nBest Offensive Player")

print(best_offense[['player','team','offensive_value']])

best_defense = df.loc[df['defensive_value'].idxmax()]

print("\nBest Defensive Player")

print(best_defense[['player','team','defensive_value']])

best_player = df.loc[df['vaep_value'].idxmax()]

print("\nBest Overall Player")

print(best_player[['player','team','vaep_value']])

print("\n")
print("="*70)
print("PART 1 COMPLETED SUCCESSFULLY")
print("="*70)



# =====================================================
# Exploratory Data Analysis (EDA)
# =====================================================

print("\n")
print("="*70)
print("EXPLORATORY DATA ANALYSIS (EDA)")
print("="*70)

# -----------------------------------------------------
# 1. Distribution of Offensive Value
# -----------------------------------------------------

plt.figure(figsize=(10,5))
sns.histplot(df['offensive_value'], bins=20, kde=True, color='blue')

plt.title("Distribution of Offensive Value")
plt.xlabel("Offensive Value")
plt.ylabel("Number of Players")

plt.show()

# -----------------------------------------------------
# 2. Distribution of Defensive Value
# -----------------------------------------------------

plt.figure(figsize=(10,5))
sns.histplot(df['defensive_value'], bins=20, kde=True, color='green')

plt.title("Distribution of Defensive Value")
plt.xlabel("Defensive Value")
plt.ylabel("Number of Players")

plt.show()

# -----------------------------------------------------
# 3. Distribution of VAEP Value
# -----------------------------------------------------

plt.figure(figsize=(10,5))
sns.histplot(df['vaep_value'], bins=20, kde=True, color='orange')

plt.title("Distribution of VAEP Value")
plt.xlabel("VAEP Value")
plt.ylabel("Number of Players")

plt.show()

# -----------------------------------------------------
# 4. Distribution of xG per90
# -----------------------------------------------------

plt.figure(figsize=(10,5))
sns.histplot(df['xg_per90'], bins=20, kde=True, color='red')

plt.title("Distribution of xG per90")
plt.xlabel("xG per90")
plt.ylabel("Number of Players")

plt.show()

# -----------------------------------------------------
# 5. Distribution of Minutes Played
# -----------------------------------------------------

plt.figure(figsize=(10,5))
sns.histplot(df['minutes'], bins=20, kde=True)

plt.title("Distribution of Minutes Played")
plt.xlabel("Minutes")
plt.ylabel("Number of Players")

plt.show()

# =====================================================
# BOXPLOTS (Outlier Detection)
# =====================================================

print("\nChecking Outliers...")

plt.figure(figsize=(8,5))
sns.boxplot(x=df['offensive_value'])
plt.title("Outliers in Offensive Value")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df['defensive_value'])
plt.title("Outliers in Defensive Value")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x=df['vaep_value'])
plt.title("Outliers in VAEP Value")
plt.show()

# =====================================================
# SCATTER PLOTS
# =====================================================

# Offensive vs Defensive

plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x='offensive_value',
    y='defensive_value'
)

plt.title("Offensive Value vs Defensive Value")

plt.show()

# Minutes vs xG

plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x='minutes',
    y='xg_per90'
)

plt.title("Minutes Played vs xG per90")

plt.show()

# Offensive vs VAEP

plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x='offensive_value',
    y='vaep_value'
)

plt.title("Offensive Value vs VAEP")

plt.show()

# =====================================================
# CORRELATION ANALYSIS
# =====================================================

correlation_matrix = df.corr(numeric_only=True)

print("\nCorrelation Matrix")

print(correlation_matrix)

plt.figure(figsize=(10,8))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()

# =====================================================
# PAIRPLOT
# =====================================================

sns.pairplot(
    df[
        [
            'offensive_value',
            'defensive_value',
            'vaep_value',
            'xg_per90'
        ]
    ]
)

plt.show()

# =====================================================
# COUNT PLOT
# =====================================================

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x='position_group'
)

plt.title("Players by Position")

plt.xlabel("Position")

plt.ylabel("Count")

plt.show()

# =====================================================
# KDE Plot
# =====================================================

plt.figure(figsize=(10,5))

sns.kdeplot(
    df['offensive_value'],
    fill=True
)

plt.title("Density Distribution of Offensive Value")

plt.show()

# =====================================================
# TOP 10 xG Players
# =====================================================

top_xg = df.sort_values(
    'xg_per90',
    ascending=False
).head(10)

plt.figure(figsize=(12,5))

sns.barplot(
    data=top_xg,
    x='player',
    y='xg_per90'
)

plt.xticks(rotation=45)

plt.title("Top 10 Players by xG per90")

plt.show()

print("\n")
print("="*70)
print("PART 2 COMPLETED SUCCESSFULLY")
print("="*70)




# =====================================================
# Trend Analysis & Performance Analysis
# =====================================================

print("\n")
print("="*70)
print("TREND ANALYSIS")
print("="*70)

# =====================================================
# 1. Average Offensive Value by Team
# =====================================================

team_offense = (
    df.groupby("team")["offensive_value"]
      .mean()
      .sort_values(ascending=False)
)

print("\nTop Teams by Offensive Value")
print(team_offense)

plt.figure(figsize=(12,6))
sns.barplot(x=team_offense.index,
            y=team_offense.values)

plt.xticks(rotation=90)

plt.title("Average Offensive Value by Team")
plt.xlabel("Team")
plt.ylabel("Average Offensive Value")

plt.show()

# =====================================================
# 2. Average Defensive Value by Team
# =====================================================

team_defense = (
    df.groupby("team")["defensive_value"]
      .mean()
      .sort_values(ascending=False)
)

print("\nTop Teams by Defensive Value")
print(team_defense)

plt.figure(figsize=(12,6))

sns.barplot(
    x=team_defense.index,
    y=team_defense.values
)

plt.xticks(rotation=90)

plt.title("Average Defensive Value by Team")
plt.xlabel("Team")
plt.ylabel("Average Defensive Value")

plt.show()

# =====================================================
# 3. Average VAEP by Team
# =====================================================

team_vaep = (
    df.groupby("team")["vaep_value"]
      .mean()
      .sort_values(ascending=False)
)

print("\nTop Teams by VAEP")
print(team_vaep)

plt.figure(figsize=(12,6))

sns.barplot(
    x=team_vaep.index,
    y=team_vaep.values
)

plt.xticks(rotation=90)

plt.title("Average VAEP Value by Team")
plt.xlabel("Team")
plt.ylabel("Average VAEP")

plt.show()

# =====================================================
# 4. Position Analysis
# =====================================================

position_analysis = (
    df.groupby("position_group")
      [["offensive_value",
        "defensive_value",
        "vaep_value"]]
      .mean()
      .round(2)
)

print("\nPosition Analysis")
print(position_analysis)

# Offensive

plt.figure(figsize=(8,5))

sns.barplot(
    x=position_analysis.index,
    y=position_analysis["offensive_value"]
)

plt.title("Average Offensive Value by Position")

plt.show()

# Defensive

plt.figure(figsize=(8,5))

sns.barplot(
    x=position_analysis.index,
    y=position_analysis["defensive_value"]
)

plt.title("Average Defensive Value by Position")

plt.show()

# VAEP

plt.figure(figsize=(8,5))

sns.barplot(
    x=position_analysis.index,
    y=position_analysis["vaep_value"]
)

plt.title("Average VAEP by Position")

plt.show()

# =====================================================
# 5. Top 10 Offensive Players
# =====================================================

top_offense = (
    df.sort_values(
        "offensive_value",
        ascending=False
    )
    .head(10)
)

print("\nTop 10 Offensive Players")
print(top_offense[["player",
                   "team",
                   "offensive_value"]])

plt.figure(figsize=(12,5))

sns.barplot(
    data=top_offense,
    x="player",
    y="offensive_value"
)

plt.xticks(rotation=45)

plt.title("Top 10 Offensive Players")

plt.show()

# =====================================================
# 6. Top 10 Defensive Players
# =====================================================

top_defense = (
    df.sort_values(
        "defensive_value",
        ascending=False
    )
    .head(10)
)

print("\nTop 10 Defensive Players")

print(top_defense[
    [
        "player",
        "team",
        "defensive_value"
    ]
])

plt.figure(figsize=(12,5))

sns.barplot(
    data=top_defense,
    x="player",
    y="defensive_value"
)

plt.xticks(rotation=45)

plt.title("Top 10 Defensive Players")

plt.show()

# =====================================================
# 7. Top 10 Overall Players
# =====================================================

top_vaep = (
    df.sort_values(
        "vaep_value",
        ascending=False
    )
    .head(10)
)

print("\nTop 10 Overall Players")

print(top_vaep[
    [
        "player",
        "team",
        "vaep_value"
    ]
])

plt.figure(figsize=(12,5))

sns.barplot(
    data=top_vaep,
    x="player",
    y="vaep_value"
)

plt.xticks(rotation=45)

plt.title("Top 10 Overall Players")

plt.show()

# =====================================================
# 8. Minutes vs Offensive Value
# =====================================================

plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x="minutes",
    y="offensive_value",
    hue="position_group"
)

plt.title("Minutes Played vs Offensive Value")

plt.show()

# =====================================================
# 9. Minutes vs Defensive Value
# =====================================================

plt.figure(figsize=(8,6))

sns.scatterplot(
    data=df,
    x="minutes",
    y="defensive_value",
    hue="position_group"
)

plt.title("Minutes Played vs Defensive Value")

plt.show()

# =====================================================
# 10. Top 10 Teams by Overall Performance
# =====================================================

overall_team = (
    df.groupby("team")["vaep_value"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,5))

sns.barplot(
    x=overall_team.index,
    y=overall_team.values
)

plt.xticks(rotation=45)

plt.title("Top 10 Teams by Overall Performance")

plt.show()

print("\n")
print("="*70)
print("PART 3 COMPLETED SUCCESSFULLY")
print("="*70)




# =====================================================
# FINAL INSIGHTS & REPORT
# =====================================================

print("\n")
print("="*70)
print("FINAL INSIGHTS")
print("="*70)

# -----------------------------------------------------
# Best Offensive Team
# -----------------------------------------------------

best_offensive_team = team_offense.idxmax()
best_offensive_value = team_offense.max()

print(f"\nBest Offensive Team : {best_offensive_team}")
print(f"Average Offensive Value : {best_offensive_value:.2f}")

# -----------------------------------------------------
# Best Defensive Team
# -----------------------------------------------------

best_defensive_team = team_defense.idxmax()
best_defensive_value = team_defense.max()

print(f"\nBest Defensive Team : {best_defensive_team}")
print(f"Average Defensive Value : {best_defensive_value:.2f}")

# -----------------------------------------------------
# Best Overall Team
# -----------------------------------------------------

best_overall_team = team_vaep.idxmax()
best_overall_value = team_vaep.max()

print(f"\nBest Overall Team : {best_overall_team}")
print(f"Average VAEP : {best_overall_value:.2f}")

# -----------------------------------------------------
# Best Offensive Player
# -----------------------------------------------------

best_offensive_player = df.loc[df['offensive_value'].idxmax()]

print("\nBest Offensive Player")

print(best_offensive_player[
    [
        'player',
        'team',
        'offensive_value'
    ]
])

# -----------------------------------------------------
# Best Defensive Player
# -----------------------------------------------------

best_defensive_player = df.loc[df['defensive_value'].idxmax()]

print("\nBest Defensive Player")

print(best_defensive_player[
    [
        'player',
        'team',
        'defensive_value'
    ]
])

# -----------------------------------------------------
# Best Overall Player
# -----------------------------------------------------

best_player = df.loc[df['vaep_value'].idxmax()]

print("\nBest Overall Player")

print(best_player[
    [
        'player',
        'team',
        'vaep_value'
    ]
])

# -----------------------------------------------------
# Best Position
# -----------------------------------------------------

best_position = position_analysis["vaep_value"].idxmax()

print("\nBest Performing Position :", best_position)

# -----------------------------------------------------
# Correlation
# -----------------------------------------------------

correlation = df[['minutes','xg_per90']].corr().iloc[0,1]

print(f"\nCorrelation between Minutes & xG per90 : {correlation:.2f}")

# =====================================================
# EXPORT RESULTS
# =====================================================

top_offense.to_csv(
    "Top_10_Offensive_Players.csv",
    index=False,
    encoding="utf-8-sig"
)

top_defense.to_csv(
    "Top_10_Defensive_Players.csv",
    index=False,
    encoding="utf-8-sig"
)

top_vaep.to_csv(
    "Top_10_Overall_Players.csv",
    index=False,
    encoding="utf-8-sig"
)

team_offense.to_csv(
    "Team_Offensive_Analysis.csv",
    encoding="utf-8-sig"
)

team_defense.to_csv(
    "Team_Defensive_Analysis.csv",
    encoding="utf-8-sig"
)

team_vaep.to_csv(
    "Team_VAEP_Analysis.csv",
    encoding="utf-8-sig"
)

print("\nCSV Files Exported Successfully!")

# =====================================================
# SAVE IMPORTANT CHARTS
# =====================================================

# Top Offensive Players

plt.figure(figsize=(10,5))

sns.barplot(
    data=top_offense,
    x='player',
    y='offensive_value'
)

plt.xticks(rotation=45)

plt.title("Top 10 Offensive Players")

plt.tight_layout()

plt.savefig("Top_10_Offensive_Players.png")

plt.close()

# Top Defensive Players

plt.figure(figsize=(10,5))

sns.barplot(
    data=top_defense,
    x='player',
    y='defensive_value'
)

plt.xticks(rotation=45)

plt.title("Top 10 Defensive Players")

plt.tight_layout()

plt.savefig("Top_10_Defensive_Players.png")

plt.close()

# Heatmap

plt.figure(figsize=(10,5))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("Correlation_Heatmap.png")

plt.close()

print("Charts Saved Successfully!")

# =====================================================
# PROJECT CONCLUSION
# =====================================================

print("\n")
print("="*70)
print("PROJECT CONCLUSION")
print("="*70)

print("""
1. The dataset was cleaned successfully.

2. Missing values and duplicate records were checked.

3. Descriptive statistics were calculated.

4. Exploratory Data Analysis (EDA) was performed.

5. Team-wise and player-wise performance was analyzed.

6. Offensive, Defensive and Overall VAEP values were compared.

7. Correlation analysis was performed between numerical features.

8. Top players and top teams were identified.

9. Visualizations were created to support findings.

10. Analysis results were exported as CSV files and charts.

Project Completed Successfully.
""")

print("="*70)
print("THANK YOU")
print("="*70)