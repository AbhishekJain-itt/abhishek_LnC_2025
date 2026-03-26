import requests
from config import Config
 
class GeocoderService:
    BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
 
    def __init__(self):
        Config.validate()
 
    def get_coordinates(self, location: str):
        params = {
            "address": location,
            "key": Config.GOOGLE_API_KEY
        }
 
        response = requests.get(self.BASE_URL, params=params)
 
        if response.status_code != 200:
            raise Exception(f"API request failed with status {response.status_code}")
 
        data = response.json()
 
        if data["status"] != "OK":
            raise Exception(f"API Error: {data['status']}")
 
        return self._parse_results(data["results"])
 
    def _parse_results(self, results):
        output = []
 
        for result in results:
            location = result["geometry"]["location"]
 
            output.append({
                "formatted_address": result["formatted_address"],
                "latitude": location["lat"],
                "longitude": location["lng"]
            })
 
        return output
