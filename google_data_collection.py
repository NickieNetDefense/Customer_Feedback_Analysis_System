import googlemaps
from dotenv import load_dotenv
import os
import pandas as pd
import datetime

# Load environment variables
load_dotenv("API_KEYS.env")
api_key = os.getenv("GOOGLE_API_KEY")

# Create a Google Maps client instance
gmaps = googlemaps.Client(key=api_key)

# Define the function to get places data
def get_places_data(query):
    try:
        places_result = gmaps.places(query)
        return places_result.get('results', [])
    except Exception as e:
        print("Error:", e)
        return []

# Define the function to get place details including reviews
def get_place_details(place_id):
    try:
        place_details = gmaps.place(place_id=place_id, fields=['reviews'])
        return place_details.get('result', {}).get('reviews', [])
    except Exception as e:
        print("Error:", e)
        return []

# Main function
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
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    output_filename = f'google_places_raw_{current_date}.csv'
    df.to_csv(output_filename, index=False)
    print(f"Data exported to CSV file: {output_filename}")

if __name__ == "__main__":
    main()