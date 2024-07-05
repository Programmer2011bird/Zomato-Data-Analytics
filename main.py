import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(palette="dark", style="dark")

def HandelRating(Value) -> float:
    VAL: list[str] = str(Value).split("/")
    VALUE: str = VAL[0]
    return float(VALUE)

dataframe: pd.DataFrame = pd.read_csv("Zomato data .csv")
dataframe["rate"] = dataframe["rate"].apply(HandelRating)

LISTED_IN: pd.Series = dataframe["listed_in(type)"]
VOTES: pd.Series = dataframe["votes"]
RATINGS: pd.Series = dataframe["rate"]
ONLINE_ORDER: pd.Series = dataframe["online_order"]
APPROX_COST: pd.Series = dataframe["approx_cost(for two people)"]

fig, axes = plt.subplots(1, 3, figsize=(12, 10))
fig.set_tight_layout(tight= True)
# Seeing The Distribution Of Every Type
sns.histplot(data=LISTED_IN, ax=axes[0])

# Seeing The Number Of Votes For Every "type"
VOTES_PER_TYPE: pd.Series = dataframe.groupby("listed_in(type)")["votes"].sum()
GROUP = pd.DataFrame({"votes":VOTES_PER_TYPE})
sns.lineplot(GROUP, ax=axes[1])

# Seeing How Many "types" Do Online Orders
sns.countplot(x = ONLINE_ORDER, ax=axes[2])

fig1, axes1 = plt.subplots(1, 3, figsize=(12, 10))
fig1.set_tight_layout(tight= True)
# See The Rating Distribution
sns.distributions.displot(RATINGS, ax=axes1[0])

# See The "approx_cost" plot
sns.countplot(x = APPROX_COST, ax=axes1[1])

# See The Heatmap For How Much Every "type" Accept Online Orders Or Not 
Pivot_Table: pd.DataFrame = dataframe.pivot_table(index="listed_in(type)", columns="online_order", aggfunc="size")
sns.heatmap(Pivot_Table, annot= True, cmap= "jet", ax=axes1[2])

plt.show()
