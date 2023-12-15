import googlemaps
from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables from API_KEYS.env file
load_dotenv("API_KEYS.env")

# Get your API key from the environment variables
api_key = os.getenv("GOOGLE_API_KEY")

# Create a client instance for the Google Maps API
gmaps = googlemaps.Client(key=api_key)

# Function to get places data
def get_places_data(query):
    try:
        places_result = gmaps.places(query)
        return places_result.get('results', [])
    except Exception as e:
        print("Error:", e)
        return []

# Function to get place details including reviews
def get_place_details(place_id):
    try:
        place_details = gmaps.place(place_id=place_id, fields=['reviews'])
        return place_details.get('result', {}).get('reviews', [])
    except Exception as e:
        print("Error:", e)
        return []

# Main function to fetch data and save as CSV

def main():
    cities = ["New York", "Los Angeles", "Chicago", "Miami", "Houston"]
    all_reviews = []

    for city in cities:
        query = f"restaurants in {city}"
        places = get_places_data(query)

        for place in places:
            place_id = place['place_id']
            reviews = get_place_details(place_id)
            for review in reviews:
                review_data = {
                    'place_id': place_id,
                    'author_name': review.get('author_name'),
                    'rating': review.get('rating'),
                    'text': review.get('text'),
                    'city': city
                }
                all_reviews.append(review_data)

    df = pd.DataFrame(all_reviews)
    df.to_csv('google_places_reviews_across_cities.csv', index=False)
    print("Data exported to CSV file.")

if __name__ == "__main__":
    main()

