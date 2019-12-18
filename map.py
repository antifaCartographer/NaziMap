import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point, Polygon


#data
county = gpd.read_file('tl_2017_us_county.shp')

#ask name

def name():
    state_name = input("which state: ")
    return state_name.title()

#work here
def data(state_name):
    df = pd.read_csv('dataWithStateFP.csv', dtype={'STATEFP':str})
    df = df[["name","email","city", "province","latitude","longitude", "STATEFP"]]
    df =df.sort_values(by=['province'])
    dfu = df.province == state_name
    df = df[dfu]
    df.index = range(len(df))
    df.to_csv(r'naziData.csv')
    return df

def fixShape(df,county):
    State = (df.STATEFP.iloc[0])
    stateMap = county['STATEFP']== State
    new_county = county[stateMap]
    return new_county

def plot(df,new_county):
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude,df.latitude))
    fig , ax = plt.subplots(1)
    base = new_county.plot(ax=ax)

    for i in range(len(df)):
        s = str(i)
        plt.text(df.longitude.iloc[i],df.latitude.iloc[i], s, color="red")


    plt.show()

x = name()
y = data(x)
z = fixShape(y,county)
q = plot(y,z)
