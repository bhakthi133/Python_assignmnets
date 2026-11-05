
import pandas as pd

#posts_df
def add_word_count(df):
    df["word_count"] = df["body"].apply(
        lambda text: len(str(text).split())
    )

    return df

#posts_df
def categorize_post(df):
    def get_category(count):
        if count < 30:
            return "Short"
        elif count <= 70:
            return "Medium"
        else:
            return "Long"

    df["category"] = df["word_count"].apply(get_category)

    return df

#user_df , posts_df
def merge_with_users(posts_df, users_df):
    merged_df = pd.merge(
        posts_df,
        users_df,
        left_on="userId",
        right_on="id",
        how="left",
    )
    return merged_df

#merged_df
def filter_posts(df, min_words=30):
    filtered_df = df[df["word_count"] >= min_words]
    return filtered_df
