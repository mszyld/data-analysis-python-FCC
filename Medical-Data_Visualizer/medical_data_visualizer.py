import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
BMI = df['weight'] / (df['height']/100*df['height']/100)
df['overweight'] = 0
df.loc[BMI > 25, 'overweight'] = 1

# Normalize data by making 0 always good and 1 always bad.
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars =['cardio'], value_vars =['active', 'alco', 'cholesterol','gluc', 'overweight', 'smoke'])
    
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # Draw the catplot with 'sns.catplot()'
    graph = sns.catplot(data=df_cat, x="variable", hue='value', col="cardio", kind="count", height=4, aspect=1.2)
    graph.set_axis_labels("variable", "total")
    
    # Get the figure for the output
    fig = graph.fig

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig

# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[df['ap_lo'] <= df['ap_hi']]
    df_heat = df_heat.loc[df['height'].quantile(0.975) >= df['height']]
    df_heat = df_heat.loc[df['height'] >= df['height'].quantile(0.025)]
    df_heat = df_heat.loc[df['weight'].quantile(0.975) >= df['weight']]
    df_heat = df_heat.loc[df['weight'] >= df['weight'].quantile(0.025)]

    # Calculate the correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize = (10, 12))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, robust=True, annot=True, mask=mask, vmax = 0.3, vmin=-0.15, fmt='.1f', square = True, linewidths=0.5, cbar_kws={"shrink": 0.5})

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
