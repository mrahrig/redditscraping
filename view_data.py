import csv
import pickle
from datetime import datetime, timezone, timedelta


# TODO: Run this file to convert the previously combined .pkl file into a
#  cleaned .csv file of CodyKo Subreddit posts after running 'main.py'.

def remove_excess_spaces(input_csv_file, output_csv_file):
    with open(input_csv_file, 'r', newline='') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    cleaned_rows = []
    for row in rows:
        cleaned_row = [clean_value(cell) for cell in row]
        cleaned_rows.append(cleaned_row)

    with open(output_csv_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(cleaned_rows)


def clean_value(value):
    # Strip leading and trailing spaces, and reduce multiple spaces to a single space
    return ' '.join(value.split())


def convert_to_pst(timestamp):
    # Convert the Unix timestamp to UTC datetime
    utc_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    # Convert UTC time to PST (UTC-8 or UTC-7 depending on daylight saving time)
    pst_time = utc_time.astimezone(timezone(timedelta(hours=-8)))
    # Return the PST time as a formatted string
    return pst_time.strftime('%Y-%m-%d %H:%M:%S %Z')


def view_data(file_path, output_csv_file):
    # Load the .pkl file
    with open(file_path, 'rb') as file:
        data = pickle.load(file)

    # Sort the data by timestamp
    if isinstance(data, list):
        data.sort(key=lambda x: x['timestamp'])

        # Open the CSV file for writing with correct newline handling
        with open(output_csv_file, 'w', newline='') as csvfile:
            fieldnames = ['id', 'timestamp', 'title', 'score', 'num_comments', 'url', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for item in data:
                # Convert the timestamp to PST
                item['timestamp'] = convert_to_pst(item['timestamp'])
                writer.writerow(item)

    elif isinstance(data, dict):
        # Open the CSV file for writing with correct newline handling
        with open(output_csv_file, 'w', newline='') as csvfile:
            fieldnames = ['timestamp', 'title', 'score', 'num_comments', 'url', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            # Convert the timestamp to PST
            data['timestamp'] = convert_to_pst(data['timestamp'])
            writer.writerow(data)


if __name__ == "__main__":
    # Replace with the name of your dataset and desired output CSV file
    dataset_name = "codyko_subreddit_combined_unique.pkl"
    output_csv = "codyko_subreddit_data.csv"
    view_data(dataset_name, output_csv)

    input_csv = output_csv  # Replace with your input CSV file name
    cleaned_output_csv = 'cleaned_output.csv'  # Replace with your desired output CSV file name

    remove_excess_spaces(input_csv, cleaned_output_csv)
    print(f"Cleaned CSV saved to {cleaned_output_csv}")
