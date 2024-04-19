import pandas_gbq

def query_geo_data_by_amenity(lon: list[float], lat: list[float], amenity: str):
    """
    Fetch data from BigQuery given a longitude min & max, latitude min & max and an amenity

    Parameters:
        lon (list[float]): The longitude range.
        lat (list[float]): The latitude range.
        amenity (str): The amenity to filter the data.
    """
    QUERY = (
        f"SELECT id as poi_id, lat, lon "
        f"FROM `carto-ps-bq-developers.data_test.osm_spain_pois` "
        f"WHERE lon BETWEEN {lon[0]} AND {lon[1]} "
        f"AND lat BETWEEN {lat[0]} AND {lat[1]} AND amenity = '{amenity}'"
    )

    df = pandas_gbq.read_gbq(QUERY)

    return df