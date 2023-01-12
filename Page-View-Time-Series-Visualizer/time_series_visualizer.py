import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
df = df.loc[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    df['date'] = pd.to_datetime(df['date'])
    fig = df.plot(kind='line',x='date',y='value', color='red', legend=None, figsize=(16,8)).get_figure()
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby(pd.PeriodIndex(df['date'], freq="M"))['value'].mean().to_frame().reset_index()
    df_bar[['year','month']]=df_bar['date'].astype(str).str.split('-',expand=True)
    
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(8, 8))
    sns.barplot(data=df_bar, x='year', hue='month', y='value', palette=sns.color_palette("tab10"))
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    current_handles, current_labels = plt.gca().get_legend_handles_labels()
    current_labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    plt.legend(current_handles, current_labels, title="Months", loc='upper left')
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2, figsize=(16, 8))
    sns.boxplot(data=df_box, x="year", y="value", ax=ax[0])
    ax[0].set_title('Year-wise Box Plot (Trend)') 
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")
  
    Months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, x="month", y="value", order=Months, ax=ax[1])
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")
    
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
