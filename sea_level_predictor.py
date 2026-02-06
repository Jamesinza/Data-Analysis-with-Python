import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

    # Create first line of best fit (all data)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    # Extend x values to 2050
    x_all = pd.Series(range(df['Year'].min(), 2051))
    y_all = res_all.slope * x_all + res_all.intercept
    plt.plot(x_all, y_all, color='red', label='Fit: all data')

    # Create second line of best fit (from 2000 onward)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_recent = pd.Series(range(2000, 2051))
    y_recent = res_recent.slope * x_recent + res_recent.intercept
    plt.plot(x_recent, y_recent, color='green', label='Fit: 2000 onward')

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
