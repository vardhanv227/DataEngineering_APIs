import requests

url = "https://data.sec.gov/submissions/CIK0000019617.json"
headers = {
    "User-Agent": "Personal Test (vardhanv227@gmail.com)",
    "Accept-Encoding": "gzip, deflate",            # Recommended by SEC
    "Host": "data.sec.gov"
} # Keep your working email here

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    
    print(f"--- Company Metadata ---")
    print(f"Name: {data.get('name')}")
    print(f"Tickers: {data.get('tickers')}") # This is a list
    print(f"Exchanges: {data.get('exchanges')}")
    print(f"SIC: {data.get('sic')}") # Standard Industrial Classification
    print(f"Business Address: {data.get('addresses', {}).get('business', {})}")
    
    # If there are former names, they are listed here:
    former_names = data.get('formerNames', [])
    if former_names:
        print(f"Former Names: {former_names}")
    
else:
    print(f"Error: {response.status_code}")