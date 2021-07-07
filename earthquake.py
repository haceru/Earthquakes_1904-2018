import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd
from geopandas import GeoDataFrame
from shapely.geometry import Point

df=pd.read_csv("earthquake_data.csv")
df.drop(columns=['Date', 'MW'], inplace=True)

geometry = [Point(xy) for xy in zip(df['Lon'], df['Lat'])]
gdf = GeoDataFrame(df, geometry=geometry)
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(18, 12), color='grey', edgecolor='black'), marker='.', color='red', markersize=10);

#df.plot(kind='scatter',x='Lon',y='Lat',color='red')
plt.title('Earthquakes with magnitude greater than 4.5 from 1904 to 2018')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()