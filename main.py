import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

csv_path = '.../'
example_data = pd.read_csv(csv_path,index_col='date')

# line chart
def linechart(example_data):
    plt.figure(figsize=(14,6))
    plt.title("Daily Global Streams of Popular Songs in 2017-2018")
    sns.lineplot(data=example_data)
    # we can show some of the cols
    # plt.figure(figsize=(14,6))
    # plt.title("title_example")
    # sns.lineplot(data=example_data['col1'], label="name1")
    # sns.lineplot(data=example_data['col2'], label="name2")
    # plt.xlabel("Date")

# bar chart
def barchart(example_data):
    plt.figure(figsize=(10,6))
    plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")
    sns.barplot(x=example_data.index, y=example_data['NK'])
    # Add label for vertical axis
    plt.ylabel("Arrival delay (in minutes)")

# heat map
def heatmap(example_data):
    plt.figure(figsize=(14,7))
    plt.title("Average Arrival Delay for Each Airline, by Month")
    sns.heatmap(data=example_data, annot=True)
    plt.xlabel("Airline")

# scatter plot
def scaterplot(example_data):
    sns.scatterplot(x=example_data['col_m'], y=example_data['col_n'])
    # with color: will be color follow the col_k class
    # sns.scatterplot(x=example_data['col_m'], y=example_data['col_n'],hue=insurance_data['col_k'])
    # or
    # sns.lmplot(x="col_m", y="col_n", hue="smoker", data=example_data)

# scatter with regression:
def lmplot(example_data):
    sns.lmplot(x="col_m", y="col_n", hue="col_k", data=example_data)
    # or
    # sns.swarmplot(x='col_m', y='col_n')

# distribution,Histograms
def histograms(example_data):
    sns.histplot(example_data['col_x'])
    # or with color
    # sns.histplot(data=example_data, x='col_x', hue='col_h')
    # plt.title("Histogram of Petal Lengths, by Species")

# Density plots
def density(example_data):
    sns.kdeplot(data=example_data['col_x'], shade=True)
    # or with color
    # sns.kdeplot(data=example_data, x='col_x', hue='col_h', shade=True)

# 2d kde
def twoDkde(example_data):
    sns.jointplot(x=example_data['col_x'], y=example_data['col_y'], kind="kde")
