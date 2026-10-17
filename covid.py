import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import plotly
import plotly.express as px 
import plotly.graph_objects  as go 
from plotly.subplots import make_subplots
data = pd.read_csv("covid_data.csv")
print(data.info())
data = data[["Province_State","Country_Region","Last_Update","Lat","Long_","Confirmed","Recovered","Deaths","Active"]]
data.columns = ("State","Country","LastUpdate","Lat","Long","Confirmed","Recovered","Deaths","Active")
data["State"].fillna(value = "",inplace = True)
TopTenConfirmed = pd.DataFrame(data.groupby("Country")["Confirmed"].sum().nlargest(10).sort_values(ascending = False))
print(TopTenConfirmed)
fig1=px.scatter(TopTenConfirmed,x=TopTenConfirmed.index, y = "Confirmed",size = "Confirmed",size_max=120,color=TopTenConfirmed.index,title="TopTenCountriesbyConfirmedCases")
fig1.write_html("TopTenConfirmedCases")

TopTenDeaths = pd.DataFrame(data.groupby("Country")["Deaths"].sum().nlargest(10).sort_values(ascending = False))
print(TopTenDeaths)
#fig1=px.scatter(TopTenDeaths,x="Deaths", y = TopTenDeaths.index,size = "Confirmed",size_max=120,color=TopTenConfirmed.index,title="TopTenCountriesbyConfirmedCases")
#fig1.write_html("TopTenConfirmedCases",auto_open=True)
fig1.show()