import plotly.figure_factory as ff
import pandas as pd 

df = pd.read_csv("lol.csv")

fig = ff.create_distplot([df["Avg Rating"].tolist()],["Mobile Brand"])
fig.show()