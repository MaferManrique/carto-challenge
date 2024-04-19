import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from geo_analytics import get_madrid_clustered_restaurants

app = Flask(__name__)

DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_DB = os.getenv("DATABASE_DB")

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_DB}'
db = SQLAlchemy(app)

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    poi_id = db.Column(db.BigInteger, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    cluster_id = db.Column(db.Integer, nullable=False)

with app.app_context():
    db.create_all()

    restaurants = get_madrid_clustered_restaurants()
    filtered_restaurants = restaurants[['poi_id', 'lat', 'lon', 'cluster_id']]
    db.session.bulk_insert_mappings(Restaurant, filtered_restaurants.to_dict(orient='records'))
    db.session.commit()

@app.route("/restaurants/<int:id>", methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.filter_by(poi_id=id).first()

    if restaurant:
        return jsonify({
            'restaurant_id': restaurant.poi_id,
            'cluster_id': restaurant.cluster_id
        }), 200
    else:
        return jsonify({'message': 'Restaurant not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)