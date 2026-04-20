import requests

# 1. Define the URL for JPMC (CIK: 0000019617)
url = "https://data.sec.gov/submissions/CIK0000019617.json"

# 2. Set the REQUIRED User-Agent header
headers = {
    "User-Agent": "Personal Test (vardhanv227@gmail.com)", # Use your actual info
    "Accept-Encoding": "gzip, deflate",            # Recommended by SEC
    "Host": "data.sec.gov"
}

# 3. Make the request
response = requests.get(url, headers=headers)

# 4. Check and parse
if response.status_code == 200:
    data = response.json()
    print(f"Company Name: {data['name']}")
    # Print the most recent filing
    print(f"Latest Filing: {data['filings']['recent']['accessionNumber'][0]}")
else:
    print(f"Error: {response.status_code}")