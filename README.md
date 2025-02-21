# Image IDs Pagination Script

## Overview

This Python script retrieves image IDs from a paginated API endpoint.

## Requirements

- Python 3.x
- `requests` library

## Environment Variables

- `BASE_URL`: Base URL of the API endpoint.
- `AUTH_TOKEN`: Authorization token for API access.

Ensure these variables are set in your environment before running the script.

## Configuration

- `ROWS_PER_PAGE`: Defines how many image IDs are fetched per API request. Adjust as needed (default is `1000`).

## Usage

Run the script using Python:

```bash
python script_name.py
```

## Functionality

- Fetches paginated image IDs from the API.
- Prints total number of pages and total items before beginning pagination.
- Prints a message each time a new page of data is fetched.
- Finally, prints the total number of image IDs retrieved.

## Output

The script outputs:

```
Total pages: X, Total items: Y
Fetching page 1
Fetching page 2
...
Total image IDs retrieved: Z
```