import requests

url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)
data = response.json()

print("Todo item:")
print(f"Title: {data['title']}")
print(f"Completed: {data['completed']}")