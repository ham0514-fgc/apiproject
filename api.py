import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/posts")

if response.status_code == 200:

    posts = response.json()

    for post in posts:
            print(f"Post ID: {post['id']}")
            print(f"Title: {post['title']}")
            print(f"Body: {post['body']}\n{'-'*40}\n")
else:
    print("Failed to retrieve data:", response.status_code)
