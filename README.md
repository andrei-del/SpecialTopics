# SpecialTopics
RecipeSearchApplication 


# Recipe Management System

## Overview

The Recipe System is an application that allows users to explore, search, and manage a collection of recipes. The system provides two main interfaces: one for regular users to search for recipes based on keywords, and another for administrators to perform CRUD (Create, Read, Update, Delete) operations on the recipes.

## Features

### User Interface

The user interface provides the following features:

- **Search Recipes**: Users can input keywords in the search bar to find recipes containing specific terms. The system retrieves and displays relevant recipes.

### Admin Interface

The admin interface, accessible via a web-based GUI, offers the following capabilities:

- **Add New Recipe**: Admins can add new recipes to the collection. Each recipe includes details such as title, cooking time, ingredients, and description.

- **Update Recipe**: Admins can modify existing recipes by updating their details. This includes changes to the title, cooking time, ingredients, and description.

- **Delete Recipe**: Admins can delete recipes from the collection based on their unique identifiers.

- **View All Recipes**: Admins can view a list of all recipes present in the system.

### Technologies Used

- **Flask**: The backend of the application is built using Flask.

- **Elasticsearch**: The recipes are stored and indexed in Elasticsearch, a distributed search and analytics engine. Elasticsearch is used to efficiently search for recipes based on user queries.

- **Python**: The primary programming language I used for both the backend logic and scripting tasks.

- **RESTful APIs**: The communication between the frontend and backend is facilitated through RESTful APIs, allowing for seamless integration and data retrieval.

## API Endpoints

| Endpoint               | Method | Parameters                           | Request Body | Response                      | Description                                           |
|------------------------|--------|--------------------------------------|--------------|-------------------------------|-------------------------------------------------------|
| `/recipes`             | GET    | `ingredient` (optional)<br>`name` (optional)<br>`cookingTime` (optional) | -            | Array of [Recipe](#recipe)    | Retrieve recipes based on optional parameters like ingredient, name, and cooking time. |
| `/recipes`             | POST   | -                                    | [Recipe](#recipe) | `201`: Recipe added successfully.<br>`400`: Invalid request body | Add a new recipe to the database.                      |
| `/recipes/{recipeId}`  | GET    | `recipeId` (required)                | -            | `200`: [Recipe](#recipe)      | Retrieve a specific recipe by its ID.                  |
| `/recipes/{recipeId}`  | PUT    | `recipeId` (required)                | [Recipe](#recipe) | `200`: Recipe updated successfully.<br>`404`: Recipe not found | Update a specific recipe by its ID.                    |
| `/recipes/{recipeId}`  | DELETE | `recipeId` (required)                | -            | `204`: Recipe deleted successfully.<br>`404`: Recipe not found | Delete a specific recipe by its ID.                    |

## Data Model

### Recipe

- **Properties**:
  - `id` (string)
  - `name` (string)
  - `ingredients` (array of strings)
  - `description` (string)
  - `cookingTime` (string)

## Index-Mapping:
{
  "mappings": {
    "properties": {
      "id": {
        "type": "keyword"
      },
      "title": {
        "type": "text"
      },
      "cooking_time": {
        "type": "integer"
      },
      "ingredients": {
        "type": "nested",
        "properties": {
          "ingredient_name": {
            "type": "text"
          },
          "quantity": {
            "type": "integer"
          }
        }
      },
      "description": {
        "type": "text"
      }
    }
  }
}

