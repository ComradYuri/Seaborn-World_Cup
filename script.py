from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

desired_width = 360
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 20)

# inspect data
df = pd.read_csv("WorldCupMatches.csv")
df_goals = pd.read_csv("goals.csv")
# print(df_goals.head())

# add column with the total goals
df["Total Goals"] = df["Home Team Goals"] + df["Away Team Goals"]
# print(df.head())

sns.set_style("whitegrid")
sns.set_context("poster", 0.5)

f, ax = plt.subplots(figsize=[12, 7])
ax = sns.barplot(data=df, x="Year", y="Total Goals")
ax.set_title("average total goals per match in the World Cup")

plt.show()
plt.close("all")

# New graph------------------------------------------------------------------------------
sns.set_context("notebook", 1.25)
f, ax2 = plt.subplots(figsize=[12, 7])
ax2 = sns.boxplot(x="year", y="goals", data=df_goals, palette="Spectral")
ax.set_title("Goals visualisation")

plt.show()

