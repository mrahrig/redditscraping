def process_posts_to_timeseries(posts):
    data = []
    for post in posts:
        # Only include posts that have a non-empty body
        if post.selftext:
            data_point = {
                'id': post.id,
                'timestamp': post.created_utc,  # Unix timestamp of the post
                'title': post.title,             # Title of the post
                'score': post.score,             # Score (up votes - down votes)
                'body': post.selftext            # Text body of the post
            }
            data.append(data_point)
    return data
