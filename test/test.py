import json

books = {
    'a': 1,
    'b': []
}

du = json.dumps(books, default=lambda o: o.__dict__)
print(du)  # {"a": 1, "b": []}
