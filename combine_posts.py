# import pickle
#
#
# def load_pkl(file_path):
#     with open(file_path, 'rb') as file:
#         return pickle.load(file)
#
#
# def save_pkl(data, file_path):
#     with open(file_path, 'wb') as file:
#         pickle.dump(data, file)
#
#
# def combine_unique_posts(new_file_paths):
#     unique_posts = {}
#
#     for file_path in new_file_paths:
#         posts = load_pkl(file_path)
#
#         for post in posts:
#             # Use the post 'id' as the key to ensure uniqueness
#             post_id = post['id']
#             if post_id not in unique_posts:
#                 unique_posts[post_id] = post
#
#     # Convert the dictionary back to a list of posts
#     return list(unique_posts.values())
#
#
# if __name__ == "__main__":
#     # List of .pkl files to combine
#     file_paths = [
#         "codyko_subreddit_data_controversial.pkl",
#         "codyko_subreddit_data_hot.pkl",
#         "codyko_subreddit_data_new.pkl",
#         "codyko_subreddit_data_rising.pkl",
#         "codyko_subreddit_data_top.pkl"
#     ]
#
#     # Combine and remove duplicates
#     combined_unique_posts = combine_unique_posts(file_paths)
#
#     # Save the combined unique data to a new .pkl file
#     save_pkl(combined_unique_posts, "codyko_subreddit_combined_unique.pkl")
#
#     print(f"Combined unique posts count: {len(combined_unique_posts)}")
