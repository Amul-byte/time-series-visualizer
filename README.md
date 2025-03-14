# Time Series Visualizer

This project visualizes time series data of daily page views for the freeCodeCamp forum from May
2016 to December 2019. It includes three types of plots: line plot, bar plot, and box plot.

## Requirements

The following Python libraries are required to run the project:

- numpy
- pandas
- matplotlib
- seaborn

You can install the required libraries using the following command:

```sh
pip install -r REQUIREMENT.txt
```

## Files

- `fcc-forum-pageviews.csv`: The dataset containing daily page views.
- `time_series_visualizer.py`: The main script that generates the visualizations.
- `REQUIREMENT.txt`: A file listing the required Python libraries.

## Usage

To generate the visualizations, run the `time_series_visualizer.py` script:

```sh
python time_series_visualizer.py
```

This will generate three image files:

- `line_plot.png`: A line plot of daily page views.
- `bar_plot.png`: A bar plot of average monthly page views.
- `box_plot.png`: Box plots of page views grouped by year and month.

## Visualizations

### Line Plot

The line plot shows the daily page views from May 2016 to December 2019.

### Bar Plot

The bar plot shows the average monthly page views for each year.

### Box Plot

The box plots show the distribution of page views grouped by year and by month.
