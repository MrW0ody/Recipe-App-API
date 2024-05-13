# Recipe-App-API

**This application is an advanced API project based on the Python language and Django REST
framework. The main purpose of the application is to enable users to authenticate, create,
update, and filter culinary recipes. Users can also upload and view images associated with the
recipes. Additionally, the application utilizes Docker containers for project management and a
Postgres database for data storage. An important aspect of the project is the implementation of
Test Driven Development approach and customization of the Django admin interface.**

# Installation

## Clone repository and build docker image:

    docker-compose build

## After this create migrations to database:

    dokcer-compose run --rm app sh -c "python manage.py makemigrations"

## After migrations run docker image:

    docker-compose up

## To run tests:

    docker-compose run --rm app sh -c "python manage.py test"

## Go to address url:

    127.0.0.1:8000/api/docs

## To create user go to address:

    127.0.0.1:8000/api/user/create

## After creating user create token to authorize user, go to address:

    127.0.0.1/8000/api/user/token

# Endpoints Recipes API:

## Recipes:

### List Recipes

    Description: View all recipes or filter by ingredients and tags.
    Method: GET
    URL: /api/recipe/recipes/
    Parameters:
    ingredients: Comma-separated list of ingredient IDs to filter.
    tags: Comma-separated list of tag IDs to filter.
    Security: Token-based authentication
    Response: Array of recipe objects

### Create Recipe

    Description: Create a new recipe.
    Method: POST
    URL: /api/recipe/recipes/
    Body: Recipe details
    Security: Token-based authentication
    Response: Newly created recipe object

### Retrieve Recipe

    Description: Get details of a specific recipe by ID.
    Method: GET
    URL: /api/recipe/recipes/{id}/
    Parameters: Recipe ID
    Security: Token-based authentication
    Response: Recipe object

### Update Recipe

    Description: Update details of a specific recipe by ID.
    Method: PUT
    URL: /api/recipe/recipes/{id}/
    Parameters: Recipe ID
    Body: Updated recipe details
    Security: Token-based authentication
    Response: Updated recipe object

### Partial Update Recipe

    Description: Partially update details of a specific recipe by ID.
    Method: PATCH
    URL: /api/recipe/recipes/{id}/
    Parameters: Recipe ID
    Body: Partially updated recipe details
    Security: Token-based authentication
    Response: Updated recipe object

### Delete Recipe

    Description: Delete a specific recipe by ID.
    Method: DELETE
    URL: /api/recipe/recipes/{id}/
    Parameters: Recipe ID
    Security: Token-based authentication
    Response: No content

### Upload Recipe Image

    Description: Upload an image for a specific recipe by ID.
    Method: POST
    URL: /api/recipe/recipes/{id}/upload-image/
    Parameters: Recipe ID
    Body: Image file
    Security: Token-based authentication
    Response: Uploaded image object

## Ingredients:

### List Ingredients

    Description: View all ingredients or filter by assigned status.
    Method: GET
    URL: /api/recipe/ingredients/
    Parameters:
    assigned_only: Filter by items assigned to a recipe.
    Security: Token-based authentication
    Response: Array of ingredient objects

### Create Ingredient

    Description: Create a new ingredient.
    Method: POST
    URL: /api/recipe/ingredients/
    Body: Ingredient details
    Security: Token-based authentication
    Response: Newly created ingredient object

### Retrieve Ingredient

    Description: Get details of a specific ingredient by ID.
    Method: GET
    URL: /api/recipe/ingredients/{id}/
    Parameters: Ingredient ID
    Security: Token-based authentication
    Response: Ingredient object

### Update Ingredient

    Description: Update details of a specific ingredient by ID.
    Method: PUT
    URL: /api/recipe/ingredients/{id}/
    Parameters: Ingredient ID
    Body: Updated ingredient details
    Security: Token-based authentication
    Response: Updated ingredient object

### Partial Update Ingredient

    Description: Partially update details of a specific ingredient by ID.
    Method: PATCH
    URL: /api/recipe/ingredients/{id}/
    Parameters: Ingredient ID
    Body: Partially updated ingredient details
    Security: Token-based authentication
    Response: Updated ingredient object

### Delete Ingredient

    Description: Delete a specific ingredient by ID.
    Method: DELETE
    URL: /api/recipe/ingredients/{id}/
    Parameters: Ingredient ID
    Security: Token-based authentication
    Response: No content

## Tags

### List Tags

    Description: View all tags or filter by assigned status.
    Method: GET
    URL: /api/recipe/tags/
    Parameters:
    assigned_only: Filter by items assigned to a recipe.
    Security: Token-based authentication
    Response: Array of tag objects

### Create Tag

    Description: Create a new tag.
    Method: POST
    URL: /api/recipe/tags/
    Body: Tag details
    Security: Token-based authentication
    Response: Newly created tag object

### Retrieve Tag

    Description: Get details of a specific tag by ID.
    Method: GET
    URL: /api/recipe/tags/{id}/
    Parameters: Tag ID
    Security: Token-based authentication
    Response: Tag object

### Update Tag

    Description: Update details of a specific tag by ID.
    Method: PUT
    URL: /api/recipe/tags/{id}/
    Parameters: Tag ID
    Body: Updated tag details
    Security: Token-based authentication
    Response: Updated tag object

### Partial Update Tag

    Description: Partially update details of a specific tag by ID.
    Method: PATCH
    URL: /api/recipe/tags/{id}/
    Parameters: Tag ID
    Body: Partially updated tag details
    Security: Token-based authentication
    Response: Updated tag object

### Delete Tag

    Description: Delete a specific tag by ID.
    Method: DELETE
    URL: /api/recipe/tags/{id}/
    Parameters: Tag ID
    Security: Token-based authentication
    Response: No content

## User:

### Create User

    Description: Create a new user.
    Method: POST
    URL: /api/user/create/
    Body: User details
    Security: Basic or Cookie-based authentication
    Response: Newly created user object

### Retrieve Authenticated User

    Description: Get details of the authenticated user.
    Method: GET
    URL: /api/user/me/
    Security: Token-based authentication
    Response: User object

## Get Auth Token

    Description: Obtain an authentication token.
    Method: POST
    URL: /api/user/token/
    Body: Username and password
    Security: Basic authentication
    Response: Authentication token
