import requests
import csv


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_data():
    """Fetch JSON data from the public API."""

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list):
            print("Error: Unexpected API response format.")
            return []

        return data

    except requests.exceptions.Timeout:
        print("Error: API request timed out.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the API.")

    except requests.exceptions.HTTPError as error:
        print(f"HTTP Error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"API request failed: {error}")

    except ValueError:
        print("Error: API returned invalid JSON.")

    return []


def process_data(data):
    """Extract and clean selected fields from API data."""

    processed_data = []

    for item in data:
        title = str(item.get("title", "")).strip()
        body = str(item.get("body", "")).strip()
        user_id = item.get("userId")

        if not title or not body or user_id is None:
            continue

        title = " ".join(title.split())
        body = " ".join(body.split())

        processed_data.append({
            "id": item.get("id"),
            "user_id": user_id,
            "title": title,
            "body": body
        })

    return processed_data


def calculate_statistics(data):
    """Calculate summary statistics."""

    if not data:
        return {}

    total_records = len(data)

    unique_users = len(set(item["user_id"] for item in data))

    average_title_length = sum(
        len(item["title"]) for item in data
    ) / total_records

    average_body_length = sum(
        len(item["body"]) for item in data
    ) / total_records

    return {
        "total_records": total_records,
        "unique_users": unique_users,
        "average_title_length": round(average_title_length, 2),
        "average_body_length": round(average_body_length, 2)
    }


def export_to_csv(data, filename="output.csv"):
    """Export processed data to CSV."""

    if not data:
        print("No data available for CSV export.")
        return

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "user_id", "title", "body"]

            writer = csv.DictWriter(
                file,
                fieldnames=fieldnames
            )

            writer.writeheader()
            writer.writerows(data)

        print(f"\nData successfully exported to {filename}")

    except OSError as error:
        print(f"Error while creating CSV file: {error}")


def display_statistics(statistics):
    """Display calculated statistics."""

    print("\n" + "=" * 45)
    print("        SUMMARY STATISTICS")
    print("=" * 45)

    print(f"Total Records        : {statistics['total_records']}")
    print(f"Unique Users         : {statistics['unique_users']}")
    print(f"Average Title Length : {statistics['average_title_length']}")
    print(f"Average Body Length  : {statistics['average_body_length']}")

    print("=" * 45)


def main():
    print("=" * 45)
    print("      API DATA PROCESSING SCRIPT")
    print("=" * 45)

    print("\nFetching data from API...")

    data = fetch_data()

    if not data:
        print("No data was retrieved.")
        return

    print(f"Successfully fetched {len(data)} records.")

    processed_data = process_data(data)

    print(f"Processed {len(processed_data)} valid records.")

    if not processed_data:
        print("No valid data available for processing.")
        return

    statistics = calculate_statistics(processed_data)

    display_statistics(statistics)

    export_to_csv(processed_data)


if __name__ == "__main__":
    main()