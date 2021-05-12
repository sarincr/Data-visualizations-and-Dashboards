from bokeh.plotting import figure, output_file, show
import pandas as pd
Data = pd.read_csv("file.csv");

colormap = {'Mumbai': 'red', 'Chennai': 'green', 'Delhi': 'blue', 'Kolkatha': 'grey' }
colors = [colormap[x] for x in Data['City']]

bok = figure(title = "House Price Data")
bok.xaxis.axis_label = 'Area'
bok.yaxis.axis_label = 'Price'

bok.circle(Data["Area"], Data["Price"],
         color=colors, fill_alpha=0.2, size=10)

output_file("Data.html", title="House Price Data")

show(bok)
