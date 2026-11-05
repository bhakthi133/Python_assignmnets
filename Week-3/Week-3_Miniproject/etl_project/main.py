
import time
import pandas as pd

from extractor import fetch_posts, fetch_users

from transformer import add_word_count,categorize_post,merge_with_users,filter_posts


from loader import save_to_csv


def main():

    start_time = time.time()
    print("ETL PIPELINE STARTED")

    try:
        print("\n1. EXTRACTING DATA...")
        posts_url = "https://jsonplaceholder.typicode.com/posts"
        users_url = "https://jsonplaceholder.typicode.com/users"
        posts_data = fetch_posts(posts_url)
        users_data = fetch_users(users_url)

        if posts_data is None or users_data is None:
            print("Extraction failed. Pipeline stopped.")
            return

        posts_df = pd.DataFrame(posts_data)
        users_df = pd.DataFrame(users_data)

        print(f"Posts extracted: {len(posts_df)}")
        print(f"Users extracted: {len(users_df)}")

        print("==========")
        print("\n2. TRANSFORMING DATA...")
        posts_df = add_word_count(posts_df)
        posts_df = categorize_post(posts_df)
        merged_df = merge_with_users(posts_df, users_df)
        filtered_df = filter_posts(merged_df, min_words=30)

        print("Word count added successfully.")
        print("Post categories assigned successfully.")
        print("Posts merged with user details.")
        print("Posts filtered successfully.")


        print("==========")
        print("\n3. LOADING DATA...")

        save_to_csv(
            merged_df,
            "output/merged_posts.csv"
        )

        save_to_csv(
            filtered_df,
            "output/filtered_posts.csv"
        )

        print("==========")
        print("\n4. ETL SUMMARY")


        print(f"Total posts extracted : {len(posts_df)}")
        print(f"Total users extracted : {len(users_df)}")
        print(f"Total merged records  : {len(merged_df)}")
        print(f"Total filtered posts  : {len(filtered_df)}")
        print(f"Posts removed         : {len(merged_df) - len(filtered_df)}")

        print("\nPipeline completed successfully!")

    except Exception as e:
        print(f"\nETL Pipeline failed: {e}")

    finally:
        end_time = time.time()
        total_time = end_time - start_time
        total_time=round(total_time,2)
        print(f"\nTotal execution time: {total_time} seconds")

if __name__ == "__main__":
    main()
