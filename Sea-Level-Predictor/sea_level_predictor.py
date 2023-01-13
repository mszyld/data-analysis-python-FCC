import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Note: use with numpy version 1.19.5 to avoid error messages, see for example
# https://github.com/numpy/numpy/issues/18355
# https://stackoverflow.com/questions/74893742/how-to-solve-attributeerror-module-numpy-has-no-attribute-bool
# print(pd.__version__)

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    
    # Create scatter plot
    df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level')

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    res = linregress(x, y)

    x = x.append(pd.Series(range(2014,2051)))
    plt.plot(x, res.intercept + res.slope*x, label='fitted line')

    # Create second line of best fit
    df = df[df['Year'] >= 2000]
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    res = linregress(x, y)
    
    x = x.append(pd.Series(range(2014,2051)))
    plt.plot(x, res.intercept + res.slope*x, label='second fitted line')
    
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()