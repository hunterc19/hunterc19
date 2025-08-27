import requests
import csv
import time

# ---------- CONFIG ----------
API_KEY = "[Get your API key from Overseerr settings]"
BASE_URL = "http://100.92.92.66:5055/api/v1"
INPUT_CSV = "C:/Users/Admin/Documents/GitHub/hunterc19/overseerr/libfliks_ids.csv"   # CSV with columns 'title' and 'movie_id'
TAG_NAME = "DCL (Blu-ray)"
DELAY = 0.5  # seconds between requests

# ---------- FUNCTION TO ADD TAG ----------
def add_tag(movie_id, tag_name):
    """Add a tag to a movie by ID."""
    url = f"{BASE_URL}/movie/{movie_id}"
    headers = {"X-Api-Key": API_KEY, "Content-Type": "application/json"}
    payload = {"tags": [tag_name]}
    
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code in [200, 201]:
        print(f"Tagged movie {movie_id} with '{tag_name}'")
    else:
        print(f"Failed to tag movie {movie_id}: {response.status_code} {response.text}")

# ---------- MAIN SCRIPT ----------
with open(INPUT_CSV, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        movie_id = row.get("movie_id")  # Adjust if your column header is different
        if movie_id:
            add_tag(movie_id, TAG_NAME)
            time.sleep(DELAY)
