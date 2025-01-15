from datetime import datetime, timezone, timedelta
import pickle

# TODO: This file gets the posts from each subreddit function and saves them in .pkl files ending in the function name.
#   It then creates a combined .pkl file from all of the individual subreddit function .pkl files.


from data_processing import process_posts_to_timeseries
from reddit_connector import fetch_top_posts, fetch_hot_posts, fetch_new_posts, fetch_controversial_posts, \
    fetch_rising_posts
from storage import save_data, load_data
from view_data import view_data, remove_excess_spaces


def convert_to_pst(timestamp):
    # Convert the Unix timestamp to UTC datetime
    utc_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)
    # Convert UTC time to PST (UTC-8 or UTC-7 depending on daylight saving time)
    pst_time = utc_time.astimezone(timezone(timedelta(hours=-8)))
    # Return the PST time as a formatted string
    return pst_time.strftime('%Y-%m-%d %H:%M:%S %Z')


def load_pkl(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)


def save_pkl(data, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(data, file)


def combine_unique_posts(new_file_paths):
    unique_posts = {}

    for file_path in new_file_paths:
        posts = load_pkl(file_path)

        for post in posts:
            # Use the post 'id' as the key to ensure uniqueness
            post_id = post['id']
            if post_id not in unique_posts:
                unique_posts[post_id] = post

    # Convert the dictionary back to a list of posts
    return list(unique_posts.values())


def main():
    # Fetch posts within the date range
    subreddit_name = 'codyko'

    top_posts = fetch_top_posts(subreddit_name)
    hot_posts = fetch_hot_posts(subreddit_name)
    new_posts = fetch_new_posts(subreddit_name)
    controversial_posts = fetch_controversial_posts(subreddit_name)
    rising_posts = fetch_rising_posts(subreddit_name)

    # Process posts to time-series format
    top_timeseries_data = process_posts_to_timeseries(top_posts)
    hot_timeseries_data = process_posts_to_timeseries(hot_posts)
    new_posts_timeseries_data = process_posts_to_timeseries(new_posts)
    controversial_timeseries_data = process_posts_to_timeseries(controversial_posts)
    rising_timeseries_data = process_posts_to_timeseries(rising_posts)

    file_names = [
        ["codyko_subreddit_data_top", top_timeseries_data],
        ["codyko_subreddit_data_hot", hot_timeseries_data],
        ["codyko_subreddit_data_new", new_posts_timeseries_data],
        ["codyko_subreddit_data_controversial", controversial_timeseries_data],
        ["codyko_subreddit_data_rising", rising_timeseries_data],
    ]

    # Create each pickle file for each type of subreddit get function
    for (file_name, timeseries_data) in file_names:
        save_data(timeseries_data, file_name)
        loaded_data = load_data(file_name)
        print("File Name:{}".format(file_name))
        print("Number of posts:{}".format(len(list(loaded_data))))
        print()

    # List of .pkl files to combine
    file_paths = [
        "codyko_subreddit_data_controversial.pkl",
        "codyko_subreddit_data_hot.pkl",
        "codyko_subreddit_data_new.pkl",
        "codyko_subreddit_data_rising.pkl",
        "codyko_subreddit_data_top.pkl"
    ]

    # Combine and remove duplicates
    combined_unique_posts = combine_unique_posts(file_paths)

    # Save the combined unique data to a new .pkl file
    save_pkl(combined_unique_posts, "codyko_subreddit_combined_unique.pkl")

    print(f"Combined unique posts count: {len(combined_unique_posts)}")

    # Replace with the name of your dataset and desired output CSV file
    dataset_name = "codyko_subreddit_combined_unique.pkl"
    output_csv = "codyko_subreddit_data.csv"
    view_data(dataset_name, output_csv)

    input_csv = output_csv  # Replace with your input CSV file name
    cleaned_output_csv = 'cleaned_output.csv'  # Replace with your desired output CSV file name

    remove_excess_spaces(input_csv, cleaned_output_csv)
    print(f"Cleaned CSV saved to {cleaned_output_csv}")


if __name__ == "__main__":
    main()
