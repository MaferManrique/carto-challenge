# Madrid Restaurants Delivery Zone Analysis

This project addresses the Carto Code Challenge and aims to identify delivery zones for restaurants in the Metropolitan Area of Madrid. By analyzing restaurant locations and clustering them into distinct zones.

## Setup

This project is best utilized with Docker for ease of use and configuration simplicity. Just follow these instructions to run the project:

1. Obtain Google Cloud Credentials and place the `credentials.json` file in the `config` directory. Ensure the file is named `credentials.json` and located in the `config` folder. You can follow the steps in this [tutorial](https://developers.google.com/workspace/guides/create-credentials#service-account). If not, adjust the path to the credentials file in the `docker-compose.yml` configuration and the Jupyter Notebook accordingly.
2. Run the following command to build the Docker image:

```
docker-compose build && docker-compose up
```

### Running the Notebook.

If everything is configured correctly, access the Notebook by navigating to [http://localhost:8888/lab/tree/MadridRestaurantsNotebook.ipynb](http://localhost:8888/lab/tree/MadridRestaurantsNotebook.ipynb)

### API Rest

If Docker Compose runs without issues, the REST API is operational. Test it at the following endpoint:

```
GET http://localhost:8000/restaurants/<restaurant_id>`
```

Give it a try with [http://localhost:8000/restaurants/2024903805](http://localhost:8000/restaurants/2024903805)

## Author

This project was authored by Mafer Manrique, leveraging documentation and examples from the libraries utilized in the project.
