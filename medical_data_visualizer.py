import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Load and clean the data
df = pd.read_csv("medical_examination.csv")

# Remove outliers for height and weight
df = df[(df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]

# 2. Add 'overweight' column (BMI > 25)
df['overweight'] = (df['weight'] / ((df['height']/100) ** 2) > 25).astype(int)

# 3. Normalize data: make 0 always good, 1 always bad for certain columns
for col in ['cholesterol', 'gluc']:
    df[col] = (df[col] > 1).astype(int)


# 4. Draw categorical plot
def draw_cat_plot():
    # 5. Create DataFrame for categorical plot using `pd.melt`
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Group and reformat the data to split it by 'cardio'
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'])['value'].count().reset_index(name='total')

    # 7. Draw the catplot with 'sns.catplot()'
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio',
                      data=df_cat, kind='bar').fig

    # 9. Save figure and return
    fig.savefig('catplot.png')
    return fig


# 10. Draw heatmap
def draw_heat_map():
    # 11. Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Calculate the correlation matrix
    corr = df_heat.corr()

    # 13. Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15. Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', center=0, vmax=.3, vmin=-.1,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)

    # 16. Save figure and return
    fig.savefig('heatmap.png')
    return fig
