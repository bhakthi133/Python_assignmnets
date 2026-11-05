import pytest
from transformer import add_word_count,categorize_post,merge_with_users,filter_posts
import pandas as pd

#tests/: tests for add_word_count, categorize_post (5+ parametrized), filter_posts, and a shared fixture.

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "body": [
            "Python is easy",
            "Python is easy to learn",
            "I love programming"
        ]
    })

def test_word_count(sample_df):
    result = add_word_count(sample_df)  #returns df
    expected=[3,5,3]
    assert result["word_count"].tolist() == expected

@pytest.mark.parametrize("count, expected", [
    (10, "Short"),
    (20, "Short"),
    (29, "Short"),
    (30, "Medium"),
    (50, "Medium"),
    (70, "Medium"),
    (80, "Long")
])
def test_categorize_post(count, expected):
    df = pd.DataFrame({
        "word_count": [count]
    })

    result = categorize_post(df)

    assert result["category"][0] == expected

def test_filter_posts(sample_df):
    df = add_word_count(sample_df)

    result = filter_posts(df, min_words=4)

    assert len(result) == 1
    assert result["word_count"].tolist() == [5]