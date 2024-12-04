# How do delivery fees vary across platforms and locations?

import sqlite3
import pandas as pd
import geopandas as gpd
import geodatasets
import matplotlib.pyplot as plt
import folium

def find_polygon():
    postal_codes = gpd.read_file('../Databases/georef-belgium-postal-codes@public.geojson')

    postal_code_df = pd.DataFrame({'postal_code': postal_codes.postcode, 'geometry': postal_codes.geometry})
    postal_code_df['postal_code'] = postal_code_df['postal_code'].str.strip()

    return postal_code_df

def create_df(db, platform, sql_code):
    connexion = sqlite3.connect(db)
    cursor = connexion.cursor()

    print(f'{platform}: ')

    locs = cursor.execute(sql_code)

    df = pd.DataFrame(locs.fetchall())
    df.columns = ['postal_code', 'fee']

    df['postal_code'] = df['postal_code'].astype(str)

    polygons = find_polygon()

    extended_df = pd.merge(df, polygons, left_on=["postal_code"], right_on=["postal_code"], how="left")

    extended_df.dropna(inplace=True)

    return extended_df

def heatmap(df):
    geometry = gpd.points_from_xy(df.longitude, df.latitude)

    df = gpd.GeoDataFrame(
    df[["fee", 'latitude', 'longitude']], geometry=geometry
    )

    from folium import plugins

    map = folium.Map(location=[51, 3.5], tiles="Cartodb dark_matter", zoom_start=8)

    heat_data = [[point.xy[1][0], point.xy[0][0]] for point in df.geometry]

    plugins.HeatMap(heat_data).add_to(map)

    return map


def get_map(df, column, name, location=[51, 4], zoom_start = 9, bins=8, fill_opacity=0.7, fill_color="RdYlGn_r", show_legend=True, map_title=""):
    """
    Will return a map. It will always compare with 'sr_geounit'.
    Compulsary Inputs: dataframe name, column to compare with and legend name.
    Other inputs: center of map (location), zoom_start, bins, fill_opacity and fill_color, show legend
    """
    df = gpd.GeoDataFrame(df, geometry=df['geometry'])

    df = df[(df[column] >= 0) & (df[column] <= 7)]


    map = folium.Map(location=location, zoom_start = zoom_start, tiles="Cartodb Positron", width="100%", height="100%")

    choropleth = folium.Choropleth(
        name = name,
        geo_data=df,
        data=df,
        fill_color=fill_color,
        fill_opacity=fill_opacity,
        bins=bins,
        columns=['postal_code', column],
        legend_name= name,
        key_on='feature.properties.postal_code',
        line_opacity = 0.1,
        )

    if show_legend == False:
        for key in choropleth._children:
            if key.startswith('color_map'):
                del(choropleth._children[key])

    choropleth.add_to(map)

    title_html = f'<h1 style="position:absolute;z-index:100000;left:40vw" >{map_title}</h1>'
    map.get_root().html.add_child(folium.Element(title_html))

    return map

def modify_to_geo(df):
    df = gpd.GeoDataFrame(df, geometry=df['geometry'])
    df = df.set_crs(4326, allow_override=True)

    return df
