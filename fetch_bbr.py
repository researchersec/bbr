import os
import requests

# Fetch credentials from environment variables
username = os.getenv('BBR_USERNAME')
password = os.getenv('BBR_PASSWORD')

def fetch_data(registration_from, registration_to, effect_from, effect_to):
    url = f"https://services.datafordeler.dk/BBR/BBRPublic/1/rest/grund?RegistreringFra={registration_from}&RegistreringTil={registration_to}&VirkningFra={effect_from}&VirkningTil={effect_to}&username={username}&password={password}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return None

if __name__ == "__main__":
    data = fetch_data("2024-01-01", "2024-01-31", "2024-01-01", "2024-01-31")
    print(data)
