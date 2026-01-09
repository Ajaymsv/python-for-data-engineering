"""
Fetch data from public API
Use case: Ingesting data from external services
"""

import requests

def fetch_api_data(url: str) -> dict:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    api_url = "https://api.publicapis.org/entries"
    data = fetch_api_data(api_url)
    print(f"Total records fetched: {len(data.get('entries', []))}")
