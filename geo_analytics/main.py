from .query import query_geo_data_by_amenity
from .processing import filter_poi_by_proximity_to_group, split_pois_by_clusters
from .export import generate_map_csv

# Madrid coordinates
LON = [-3.93455628, -3.31993445]
LAT = [40.25387182, 40.57085727]
MAX_DISTANCE_FROM_CINEMA = 150 # meters

# This main function is for the sake of the exercise in case user wants to get the .csv
# We don't export this function, and instead replicate it on the Notebook for explaining purposes
def main():
    """
    Main function to execute the data processing pipeline.

    This function purpose is mainly to be used in our API REST service.

    On the cluster analysis we are going to make on Jupyter Notebook we will replicate this
    same logic but explaining each step.
    """
    # Get data from the query module
    restaurants = query_geo_data_by_amenity(LON, LAT, "restaurant")
    cinemas = query_geo_data_by_amenity(LON, LAT, "cinema")

    # We filter the restaurants by proximity to cinemas and then split them by clusters
    restaurants_far_from_cinemas = filter_poi_by_proximity_to_group(restaurants, cinemas, MAX_DISTANCE_FROM_CINEMA)
    restaurants_with_cluster = split_pois_by_clusters(restaurants_far_from_cinemas, 5)

    # We export the data to a CSV file
    generate_map_csv(restaurants_with_cluster, "./data/madrid_restaurants_clusters.csv")

    return restaurants_with_cluster

if __name__ == "__main__":
    main()
