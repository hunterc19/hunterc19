import requests
import csv
import time
from urllib.parse import quote

# ---------- CONFIG ----------
API_KEY = "[Get your API key from Overseerr settings]"
BASE_URL = "http://100.92.92.66:5055/api/v1"
INPUT_CSV = "C:/Users/Admin/Documents/GitHub/hunterc19/overseerr/libfliks.csv"   # CSV with a column 'title'
OUTPUT_CSV = "libfliks_ids.csv"
DELAY = 0.5  # seconds between requests to avoid overwhelming the server

# ---------- FUNCTION ----------
def get_movie_id(title):
    url = f"{BASE_URL}/search?query={quote(title)}"
    headers = {"X-Api-Key": API_KEY}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
        if results:
            return results[0]["id"]
        else:
            return None
    else:
        print(f"Error searching for '{title}': {response.status_code} {response.text}")
        return None

# ---------- MAIN SCRIPT ----------
with open(INPUT_CSV, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    rows = []
    for row in reader:
        title = row["title"]
        movie_id = get_movie_id(title)
        print(f"{title} -> {movie_id}")
        row["movie_id"] = movie_id
        rows.append(row)
        time.sleep(DELAY)

# Write results to new CSV
with open(OUTPUT_CSV, "w", newline="") as csvfile:
    fieldnames = list(rows[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Done! Output saved to {OUTPUT_CSV}")
