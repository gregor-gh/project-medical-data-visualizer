import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df["bmi"] = df["weight"] / (df["height"]/100) ** 2

df.loc[df["bmi"] > 25, "overweight"] = 1
df.loc[df["bmi"] <= 25, "overweight"] = 0
df["overweight"] = df["overweight"].astype("int8")


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholestorol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.loc[df["cholesterol"] == 1, "cholesterol"] = 0
df.loc[df["cholesterol"] > 1, "cholesterol"] = 1

df.loc[df["gluc"] == 1, "gluc"] = 0
df.loc[df["gluc"] > 1, "gluc"] = 1

# Draw Categorical Plot


def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=[
                     "active", "alco", "cholesterol", "gluc", "overweight", "smoke"])
    #print(df_cat)

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    #df_cat = df_cat.groupby(["variable"]).count()
    # print(df_cat)
    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(data=df_cat, kind="count",
                x="variable", hue="value", col="cardio")
    g.set_axis_labels("variable","total")
    
    #sns.catplot(data=df_cat, kind="count", x="variable", hue="value", col="cardio")
    fig = g.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig
draw_cat_plot()

# # Draw Heat Map
# def draw_heat_map():
#     # Clean the data
#     df_heat = None

#     # Calculate the correlation matrix
#     corr = None

#     # Generate a mask for the upper triangle
#     mask = None


#     # Set up the matplotlib figure
#     fig, ax = None

#     # Draw the heatmap with 'sns.heatmap()'


#     # Do not modify the next two lines
#     fig.savefig('heatmap.png')
#     return fig
