from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Sample data
students = [
    {"name": "Alice", "age": 20, "grade": "A", "subjects": ["Math", "Physics"]},
    {"name": "Bob", "age": 22, "grade": "B", "subjects": ["History", "English"]},
    {"name": "Charlie", "age": 21, "grade": "A", "subjects": ["Biology", "Chemistry"]},
    {"name": "Diana", "age": 23, "grade": "C", "subjects": ["Economics", "Math"]},
    {"name": "Ethan", "age": 20, "grade": "B", "subjects": ["Computer Science", "Math"]},
]

#Load the dotenv file and get mongodb uri
load_dotenv()
mongo_uri = os.getenv('MONGO_URI')

client = MongoClient(mongo_uri)
db = client['school']
collection = db['students']

collection.insert_many(students)