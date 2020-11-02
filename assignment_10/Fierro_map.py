
# %% Importa libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import geopandas as gpd
import os
from shapely.geometry import Point
import contextily as ctx

# %% Download Data to used
# Rivers and streams information
# https://www.weather.gov/gis/AWIPSShapefiles

file = os.path.join('../../data', 'rs16my07.shp')
rivers_us = gpd.read_file(file)

# River Forecast Center Boundaries
# https://www.weather.gov/gis/RFCBounds
file_st = os.path.join('../../data', 'rf12ja05.shp')
stat_ref = gpd.read_file(file_st)

# Gauges II USGS stream gauge dataset:
# https://water.usgs.gov/GIS/metadata/usgswrd/XML/gagesII_Sept2011.xml#stdorder

file_ga = os.path.join('../../data', 'gagesII_9322_sept30_2011.shp')
gages = gpd.read_file(file_ga)

# %% Check whats inside data files and CRS :(
# Rivers

type(rivers_us)
var_names = rivers_us.head()
rivers_us.columns  # Variables name
rivers_us.shape  # no. of gages and no. of varaibles

rivers_us.geom_type  # geometry
rivers_us.crs  # check our CRS - coordinate reference system
rivers_us.total_bounds  # Check the spatial extent

# %% Gages information
# Take only AZ
gages.columns
gages.STATE.unique()
gages_AZ = gages[gages['STATE'] == 'AZ']
gages_AZ.shape

# %% Add specific points
# UA:  32.22877495, -110.97688412
# STream gauge:  34.44833333, -111.7891667
point_list = np.array([[-111.7891667, 34.44833333]])
point_geom = [Point(xy) for xy in point_list]
point_df = gpd.GeoDataFrame(point_geom, columns=['geometry'],
                            crs=gages_AZ.crs)  # project into gages_az GEOMETRY
# %% Look at one region in rivers
# Zoom  in and just look at AZ/UTAH
stat_ref.columns
stat_ref.STATE.unique()
stat_ref_AZ = stat_ref[stat_ref['STATE'] == 'UT']  # Utah and Arizona
stat_ref_AZ.shape
test = pd.DataFrame(stat_ref['STATE'])  # aux to see regions name
# super CRUCIAL step!!!
# Project points into stat_ref CRS
points_project = gages_AZ.to_crs(stat_ref_AZ.crs)

# %% Plot map :D

fig, ax = plt.subplots(figsize=(10, 10))
rivers_us.plot(figsize=(10, 10), alpha=0.5, edgecolor='b',
               ax=ax, label='Rivers', zorder=1)
stat_ref_AZ.boundary.plot(figsize=(10, 10), alpha=0.5, edgecolor='k',
                          ax=ax, label='River Forecast Center Boundaries')
points_project.plot(column='DRAIN_SQKM', categorical=True,
                    legend=False, markersize=45, cmap='OrRd',
                    ax=ax, label='Arizona Gages')
point_df.plot(ax=ax, color='k', marker='*', markersize=45,
              label='Verde River Gage')
plt.ylim(ymax=45, ymin=30)
plt.xlim(xmax=-105, xmin=-120)
ax.set_title('Hydrologic Information')
ax.set_xlabel('Longitude [°]')
ax.set_ylabel('Latitude [°]')
ax.legend()
ctx.add_basemap(ax, crs='EPSG:4326')
fig.savefig("Hydr_map.png")
# %% Run above