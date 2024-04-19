from shapely.geometry import Point, MultiPoint
from shapely.ops import nearest_points
from geopy.distance import geodesic
from sklearn.cluster import KMeans
import pandas as pd

def filter_poi_by_proximity_to_group(df: pd.DataFrame, filter_group: pd.DataFrame, filter_distance: float):
    """
    Filter the first dataframe based on the distance to the second. 
    To pass the filter, the element should be more than <filter_distance> away 
    from the nearest POIs in the second dataframe

    Parameters:
        df (pd.DataFrame): Dataframe to filter
        filter_group (pd.DataFrame): Dataframe that is going to be used for filtering
        filter_distance (float): Distance in meters to filter
    """
    filter_pois = MultiPoint(filter_group.apply(lambda row: Point(row['lon'], row['lat']), axis=1))

    df['geometry'] = df.apply(lambda row: Point(row['lon'], row['lat']), axis=1)
    df['nearest_poi'] = df['geometry'].apply(lambda geometry: nearest_points(geometry, filter_pois)[1])
    df['distance_to_nearest_poi'] = df.apply(
        lambda row: geodesic(
            (row['geometry'].y, row['geometry'].x), 
            (row['nearest_poi'].y, row['nearest_poi'].x)
        ).meters
    , axis=1)

    filtered_df = df[df['distance_to_nearest_poi'] >= filter_distance]
    
    return filtered_df

def split_pois_by_clusters(df: pd.DataFrame, n_clusters: int):
    """
    This function receive a dataFrame of POIs and group them by clusters using kMeans algorithm

    Parameters:
        df (pd.DataFrame): Dataframe
        n_clusters (int): Number of clusters
    """
    kmeans = KMeans(n_clusters=n_clusters, random_state=0).fit(df[['lon', 'lat']])
    df.loc[:, 'cluster_id'] = kmeans.labels_

    return df
