import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print(f"{todos[1]} -- {todos[1]['userId']}")