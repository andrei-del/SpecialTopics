from flask import Flask, jsonify, request
from elasticsearch import Elasticsearch

app = Flask(__name__)


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
index_name = "recipes_v2"

# Route to get all recipes with optional query parameters
@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    ingredient = request.args.get('ingredient')
    name = request.args.get('name')
    cooking_time = request.args.get('cookingTime')

    # Build Elasticsearch query 
    must_queries = []
    if ingredient:
        must_queries.append({"nested": {"path": "ingredients", "query": {"match": {"ingredients.ingredient_name": ingredient}}}})
    if name:
        must_queries.append({"match": {"title": name}})
    if cooking_time:
        must_queries.append({"match": {"cooking_time": cooking_time}})

    if must_queries:
        query = {"query": {"bool": {"must": must_queries}}}
    else:
        query = {"query": {"match_all": {}}}

    # Perform the Elasticsearch search
    result = es.search(index=index_name, body=query)
    recipes = [hit["_source"] for hit in result["hits"]["hits"]]

    return jsonify(recipes)

# Route to get a recipe by ID
@app.route('/api/recipes/<recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    result = es.get(index=index_name, id=recipe_id)
    if result['found']:
        return jsonify(result["_source"])
    else:
        return jsonify({'error': 'Recipe not found'}), 404

@app.route('/api/recipes', methods=['POST'])
def add_recipe():
    try:
        new_recipe = request.json  

        # Specify the document ID using the provided "id" field
        recipe_id = new_recipe.get("id")
        es.index(index=index_name, id=recipe_id, body=new_recipe)

        return jsonify({'message': 'Recipe added successfully.'}), 201
    except Exception as e:
        return jsonify({'error': f'Invalid request body. {str(e)}'}), 400

# Route to update a recipe by ID
@app.route('/api/recipes/<recipe_id>', methods=['PUT'])
def update_recipe(recipe_id):
    try:
        updated_recipe = request.json  
        es.update(index=index_name, id=recipe_id, body={"doc": updated_recipe})
        return jsonify({'message': 'Recipe updated successfully.'})
    except Exception as e:
        return jsonify({'error': f'Invalid request body. {str(e)}'}), 400

# Route to delete a recipe by ID
@app.route('/api/recipes/<recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    try:
        es.delete(index=index_name, id=recipe_id)
        return jsonify({'message': 'Recipe deleted successfully.'}), 204
    except Exception as e:
        return jsonify({'error': f'Error deleting recipe. {str(e)}'}), 500
# 
if __name__ == '__main__':
    app.run(debug=True, port=8000)
