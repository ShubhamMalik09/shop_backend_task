# Shop Registration and Search System

This is a Django-based application that allows users to register shops with their details (name, latitude, and longitude) and search for nearby shops based on their location using latitude and longitude. The project uses Django REST Framework (DRF) for API handling and returns shop information along with the calculated distance from the user's location.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Register Shop](#register-shop)
  - [Search Shops](#search-shops)
- [API Endpoints](#api-endpoints)
  - [Register Shop](#register-shop)
  - [Search Shops](#search-shops)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [License](#license)

---

## Installation

### Prerequisites

Ensure that Python 3.x and `pip` are installed on your system.

###Create and activate a virtual environment:
  ```bash
  python3 -m venv env
  source `env\Scripts\activate`
  ```
###Install the dependencies:
```bash
  pip install -r requirements.txt
```

###Apply database migrations:
```bash
python manage.py migrate
```

###Run the Django development server:
```bash
python manage.py runserver
```

##Usage
###Register a Shop
To register a shop with latitude and longitude, you can send a POST request to the /api/shops/register/ endpoint.

####Example request using cURL:
```bash
curl -X POST http://127.0.0.1:8000/api/shops/register/ \
-H "Content-Type: application/json" \
-d '{
  "name": "Shop Name",
  "latitude": "40.712776",
  "longitude": "-74.005974"
}'
```
###Search Shops
To search for shops near a given location (latitude and longitude), send a POST request to the /api/shops/search/ endpoint. The response will return the list of shops sorted by distance from the user's location.

####Example request using cURL:
```bash
curl -X POST http://127.0.0.1:8000/api/shops/search/ \
-H "Content-Type: application/json" \
-d '{
  "latitude": "40.730610",
  "longitude": "-73.935242"
}'
```

##API Endpoints
###Register Shop
URL: /api/shops/register/
Method: POST
Description: Registers a new shop with name, latitude, and longitude.
Request Body:

Field	Type	Description
name	String	Name of the shop
latitude	Float	Latitude of the shop location
longitude	Float	Longitude of the shop location
Response Example:

json
Copy code
{
    "id": 1,
    "name": "Shop 1",
    "latitude": "40.712776",
    "longitude": "-74.005974"
}

###Search Shops
URL: /api/shops/search/
Method: POST
Description: Returns the list of shops sorted by their distance from the user's current location.
Request Body:

Field	Type	Description
latitude	Float	User's current latitude
longitude	Float	User's current longitude
Response Example:

json
Copy code
[
  {
    "id": 1,
    "name": "Shop 1",
    "latitude": "40.712776",
    "longitude": "-74.005974",
    "distance": 2.3  # Distance in kilometers
  },
  {
    "id": 2,
    "name": "Shop 2",
    "latitude": "40.758896",
    "longitude": "-73.985130",
    "distance": 4.6
  }
]

##Technologies Used
Django: Backend framework.
Django REST Framework (DRF): API development.
MySQL: Database
Python: Core programming language.

##Project Structure

├── Shops/                     # Django app for shop-related functionalities
│   ├── migrations/            # Database migrations
│   ├── models.py              # Shop model definition
│   ├── serializers.py         # DRF serializers for shop model
│   ├── views.py               # View logic for registering and searching shops
│   ├── urls.py                # URL configuration for the Shops app
│
├── shop/              # Main project folder
│   ├── settings.py            # Project settings
│   ├── urls.py                # Project-wide URL configurations
│
├── manage.py                  # Django's management script
├── README.md                  # This file
