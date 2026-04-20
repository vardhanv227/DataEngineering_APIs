import requests

# CIK for JPMC padded to 10 digits
cik = "0000019617"
# Taxonomy tag for Net Income
concept = "NetIncomeLoss"

url = f"https://data.sec.gov/api/xbrl/companyconcept/CIK{cik}/us-gaap/{concept}.json"
headers = {"User-Agent": "Vardh Vishnu vardh@example.com"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # The 'units' key contains the currency (usually 'USD')
    # and a list of yearly/quarterly values.
    recent_val = data['units']['USD'][-1]
    print(f"Concept: {data['tag']}")
    print(f"Latest Value: ${recent_val['val']:,}")
    print(f"Period: {recent_val['end']}")