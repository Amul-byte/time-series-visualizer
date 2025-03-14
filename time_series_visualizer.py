import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",index_col="date",parse_dates=True)

# Clean data
df = df[(df["value"]>=df["value"].quantile(0.025)) & (df["value"]<=df["value"].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig,ax=plt.subplots(figsize=(12,6))
    ax.plot(df.index,df["value"],color="green",linewidth=0.5)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month
    # Draw bar plot
    df_gp=df_bar.groupby(["year","month"])["value"].mean().unstack()

    fig,ax=plt.subplots(figsize=(12,6))

    df_gp.plot(kind="bar",ax=ax)
    ax.set_title("plot")
    ax.set_xlabel("Years")
    ax.set_ylabel("Average Page Views")
    ax.legend()




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
    month_order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # Convert to Jan, Feb, etc.
    df_box["month"] = pd.Categorical(df_box["month"], categories=month_order, ordered=True)  # Ensure correct order

    # Create the box plots
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    sns.boxplot(data=df_box, x="year", y="value", ax=ax[0])
    sns.boxplot(data=df_box, x="month", y="value", ax=ax[1])



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

draw_line_plot()
draw_bar_plot()
draw_box_plot()
