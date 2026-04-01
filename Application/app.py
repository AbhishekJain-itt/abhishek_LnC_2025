from geocoder import GeocoderService
from validator import validate_location
 
def main():
    print("Location to Coordinates Finder")
 
    try:
        location_input = input("Enter location: ")
        location = validate_location(location_input)
 
        service = GeocoderService()
        results = service.get_coordinates(location)
 
        print("\nResults:\n")
 
        for idx, res in enumerate(results, start=1):
            print(f"Result {idx}:")
            print(f"  Address   : {res['formatted_address']}")
            print(f"  Latitude  : {res['latitude']}")
            print(f"  Longitude : {res['longitude']}")
            print("-" * 40)
 
    except Exception as e:
        print(f"\nError: {str(e)}")
 
 
if __name__ == "__main__":
    main()
