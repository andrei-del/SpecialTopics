


from elasticsearch import Elasticsearch



from elasticsearch.exceptions import ConnectionTimeout

# Connect to Elasticsearch 
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

# Define the new index name
new_index_name = "recipes_v2"


try:
    es.indices.create(index=new_index_name, ignore=400, body={
       mappings": {
            "properties": {
                "id": {"type": "keyword"},  # Change to keyword
                "title": {"type": "text"},
                "cooking_time": {"type": "integer"},
                "ingredients": {
                    "type": "nested",
                    "properties": {
                        "ingredient_name": {"type": "text"},
                        "quantity": {"type": "integer"}
                    }
                }, "
                "description": {"type": "text"}
            }
        }
    })
    print(f"Index '{new_index_name}' created successfully.")
except ConnectionTimeout as e:
    print(f"Connection Timeout: {e}")
except Exception as e:
    print(f"An error occurred: {e}")


