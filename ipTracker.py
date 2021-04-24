import requests

url="http://ip-api.com/json/"

try:
    ip=input("Enter any IP Address (Don't type anything in order to find your current IP Address location)\n")
finally:
    data=requests.get(url+ip).json()
    print(f'IP Address: {data["query"]}')
    print(f"Country: {data['country']}")
    print(f'City: {data["city"]}')
    print(f'Region: {data["regionName"]}')
    print(f'Latitude: {data["lat"]} degrees\nLongitude: {data["lon"]} degrees\nTimezone: {data["timezone"]}')
    print(f'ISP: {data["isp"]}\nOrganisation: {data["org"]}')
