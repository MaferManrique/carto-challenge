# Madrid Restaurants Delivery Zone Analysis

This project addresses the Carto Code Challenge and aims to identify delivery zones for restaurants in the Metropolitan Area of Madrid. By analyzing restaurant locations and clustering them into distinct zones.

## Setup

This project is best utilized with Docker for ease of use and configuration simplicity. Just follow these instructions to run the project:

1. Obtain Google Cloud Credentials and place the `credentials.json` file in the `config` directory. Ensure the file is named `credentials.json` and located in the `config` folder. You can follow the steps in this [tutorial](https://developers.google.com/workspace/guides/create-credentials#service-account). If not, adjust the path to the credentials file in the `docker-compose.yml` configuration and the Jupyter Notebook accordingly. Make sure the credentials are linked to a project with BigQuery API enabled.
2. Run the following command to build the Docker image:

```
docker-compose build && docker-compose up
```

### Running the Notebook.

If everything is configured correctly, access the Notebook by navigating to [http://localhost:8001/notebooks/MadridRestaurantsNotebook.ipynb](http://localhost:8001/notebooks/MadridRestaurantsNotebook.ipynb)

### Running API Rest

If Docker Compose runs without issues, the REST API is operational. Test it at the following endpoint:

```
GET http://localhost:8000/restaurants/<restaurant_id>`
```

Give it a try with [http://localhost:8000/restaurants/2024903805](http://localhost:8000/restaurants/2024903805)

## `geo_analytics` module.

All the code related to extract, process and export geo data from the dataset is inside the `geo_analytics` module, this is made from the following files:

* `query.py`
    1. **query_geo_data_by_amenity**: This function fetch data from the dataset using BigQuery. I decided to use pandas_gbq library here to directly have a DataFrame to work with the data. This function also receives the lon (min, max) and lat (min, max) as well as the amenity to filter by them. 
* `processing.py`
    1. **filter_poi_by_proximity_to_group**: This function filter the first dataframe its receive based on the second. We are using here the geodesic function from geopy.distance to calculate the distance en meters between two points.
    2. **split_pois_by_clusters**: This function receive a dataFrame of POIs and group them by clusters based on their coordinates.
* `export.py`
    1. **generate_map_csv**: This function receive the dataFrame and creates a .csv file with it in the path you pass to the function.
* `main.py`
    1. Here we expose a main function that makes all the process we are doing in the Notebook but directly, we used it on the `app.py` to populate the database with the initial information.

## API REST

The API REST has only one endpoint as explained above. The server that control this was made using Flask.

I decided to use SQLAlchemy to create and query the database, when you init the server it creates the database in the case it doesn't exist yet and populate it. 

Please noticed that the database is populate every time you start the server, replacing duplicates one to keep the data the more up-to-date as possible. 

## Author

This project was authored by Mafer Manrique, leveraging documentation and examples from the libraries utilized in the project.
