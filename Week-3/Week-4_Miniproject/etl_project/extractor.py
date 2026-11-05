import requests
#user_url="https://jsonplaceholder.typicode.com/users"
#posts_url="https://jsonplaceholder.typicode.com/posts"

def fetch_users(user_url,time):
    try:
        user_r = requests.get(user_url, timeout=time)
        user_r.raise_for_status()
        users_data = user_r.json()
        return users_data
    except requests.exceptions.ConnectionError:
        print("Connection error: Unable to connect to the server.")
    except requests.exceptions.Timeout:
        print("Timeout error: Server took too long to respond.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")


def fetch_posts(posts_url,time):
    try:
        posts_r = requests.get(posts_url, timeout=time)
        posts_r.raise_for_status()
        posts_data = posts_r.json()
        return posts_data
    except requests.exceptions.ConnectionError:
        print("Connection error: Unable to connect to server.")
    except requests.exceptions.Timeout:
        print("Timeout error: Server took much long to respond.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")




