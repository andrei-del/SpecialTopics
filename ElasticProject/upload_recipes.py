import json
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
from elasticsearch.exceptions import ConnectionTimeout

# Connect to Elasticsearch without explicitly setting timeout
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Define the index name
index_name = "recipes_v2"

# Read recipes from JSON file
with open("recipes_data.json", "r") as file:
    recipes_data = json.load(file)

# Index recipes into Elasticsearch
actions = [
    {
        "_op_type": "index",
        "_index": index_name,
        "_source": recipe
    }
    for recipe in recipes_data
]

try:
    success, failed = bulk(es, actions)
    print(f"Successfully indexed {success} recipes. Failed to index {failed} recipes.")
except ConnectionTimeout as e:
    print(f"Connection Timeout: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
