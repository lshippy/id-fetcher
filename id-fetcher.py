import requests
import json
import os

BASE_URL = os.getenv("BASE_URL")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

HEADERS = {
    "Authorization": f"Basic {AUTH_TOKEN}",
    "Content-Type": "application/json"
}

ROWS_PER_PAGE = 1000

def fetch_page(page):
    params = {
        "pagination": json.dumps({
            "idsOnly": True,
            "rowsPerPage": ROWS_PER_PAGE,
            "page": page,
            "sortBy": "id",
        })
    }

    url = f"{BASE_URL}/api/images"
    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code != 200:
        raise Exception(f"Error {response.status_code}: {response.text}")

    return response.json()

def paginate_through_images():
    page = 1
    image_ids = []

    data = fetch_page(page)

    pagination_info = data.get("meta", {}).get("pagination", {})
    total_rows = pagination_info.get("totalRows", 0)
    total_pages = (total_rows + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE

    print(f"Total pages: {total_pages}, Total items: {total_rows}")
    print(f"Fetching page {page}")

    while True:
        images = data.get("data", {}).get("images", [])
        image_ids.extend([img["id"] for img in images])

        if len(images) < ROWS_PER_PAGE:
            break

        page += 1
        print(f"Fetching page {page}")
        data = fetch_page(page)

    print(f"Total image IDs retrieved: {len(image_ids)}")
    return image_ids

image_ids = paginate_through_images()