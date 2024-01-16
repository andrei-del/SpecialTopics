from elasticsearch import Elasticsearch

# Initialize Elasticsearch connection
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
index_name = "recipes_v2"

#query to get all documents
query = {"query": {"match_all": {}}}
result = es.search(index=index_name, body=query, size=10000)  # Adjust 'size' accordingly

# Extract data and IDs from the result
data_with_ids = [{"_id": hit["_id"], "_source": hit["_source"]} for hit in result["hits"]["hits"]]


for item in data_with_ids:
    print(f"ID: {item['_id']}, Data: {item['_source']}")
