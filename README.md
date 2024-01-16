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

### Get all recipes

- **Endpoint**: `/recipes`
- **Method**: `GET`
- **Parameters**:
  - `ingredient` (query, optional): Search by ingredient
  - `name` (query, optional): Search by name
  - `cookingTime` (query, optional): Search by cooking time
- **Response**: Array of [Recipe](#recipe) objects

### Add a new recipe

- **Endpoint**: `/recipes`
- **Method**: `POST`
- **Request Body**: [Recipe](#recipe) object
- **Response**:
  - `201`: Recipe added successfully.
  - `400`: Invalid request body

### Get a recipe by ID

- **Endpoint**: `/recipes/{recipeId}`
- **Method**: `GET`
- **Parameters**:
  - `recipeId` (path, required): ID of the recipe
- **Response**:
  - `200`: [Recipe](#recipe) object
  - `404`: Recipe not found

### Update a recipe by ID

- **Endpoint**: `/recipes/{recipeId}`
- **Method**: `PUT`
- **Parameters**:
  - `recipeId` (path, required): ID of the recipe
- **Request Body**: [Recipe](#recipe) object
- **Response**:
  - `200`: Recipe updated successfully.
  - `404`: Recipe not found

### Delete a recipe by ID

- **Endpoint**: `/recipes/{recipeId}`
- **Method**: `DELETE`
- **Parameters**:
  - `recipeId` (path, required): ID of the recipe
- **Response**:
  - `204`: Recipe deleted successfully.
  - `404`: Recipe not found

## Data Model

### Recipe

- **Properties**:
  - `id` (string)
  - `name` (string)
  - `ingredients` (array of strings)
  - `description` (string)
  - `cookingTime` (string)


