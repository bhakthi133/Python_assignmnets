"""
Topic: ETL Pipeline: API -> pandas -> File Output 
Build a complete ETL pipeline in etl_pipeline.py: 
Extract: Fetch from /users and /posts at jsonplaceholder.typicode.com. 
Transform: 
(a) Create users DataFrame. 
(b) Add word_count column to posts. 
(c) Merge on userId/id. (d) Filter word_count > 30. (e) Add category: Short/Medium/Long. 
Load: Save to output/etl_result.csv. Create directory if missing. 
Add main() and print a summary line with counts. 
(e) Predict the output: import pandas as pd posts = [{'userId':1,'body':'hello world foo bar'},{'userId':1,'body':'hi'},{'userId':2,'body':'a b c d e f g h'}] df = pd.DataFrame(posts) df['wc'] = df['body'].apply(lambda x: len(x.split())) print(df['wc'].tolist()) print(len(df[df['wc'] > 3])) 

"""

import requests
import pandas as pd
import os

def get_category(count):
    if count <= 40:
        return "Short"
    elif count <= 60:
        return "Medium"
    else:
        return "Long"

def main():
    r = requests.get("https://jsonplaceholder.typicode.com/users", timeout=5)
    r.raise_for_status()
    users_data = r.json()
    posts_r = requests.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
    posts_r.raise_for_status()
    posts_data = posts_r.json()
    print(type(users_data))
    print(type(posts_data))

    users_df = pd.DataFrame(users_data)
    posts_df = pd.DataFrame(posts_data)
    print(users_df)
    print(posts_df)

    posts_df["word_count"] = posts_df["body"].apply(lambda body: len(body.split()))

    merged_df = pd.merge(
        posts_df,
        users_df,
        left_on="userId",
        right_on="id"
    )

    filtered_df = merged_df[merged_df["word_count"] > 30].copy()

    filtered_df["category"] = filtered_df["word_count"].apply(get_category)

    os.makedirs("output", exist_ok=True)

    filtered_df.to_csv("output/etl_result.csv", index=False)


if __name__ == "__main__":
    main()