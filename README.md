# NaijaBites API

## Project Overview

NaijaBites API is a robust Recipe Management API built with Django and Django REST Framework. This API provides a complete solution for creating, managing, and sharing recipes with a focus on Nigerian cuisine and culinary traditions. It offers secure user authentication, comprehensive recipe management, and advanced filtering capabilities.

## Key Features

- 🔐 **User Authentication**: Secure user registration and authentication system
- 📝 **CRUD Operations**: Complete Create, Read, Update, Delete functionality for recipes
- 🔍 **Advanced Search**: Search recipes by title, description, and category
- 🏷️ **Category Filtering**: Filter recipes by category (e.g., appetizers, main courses, desserts)
- 🥘 **Ingredient Filtering**: Find recipes based on specific ingredients
- 📄 **Pagination**: Efficient pagination for large recipe collections
- 🔄 **Sorting**: Sort recipes by preparation time, cooking time, creation date, or title
- 👤 **Owner-Based Access Control**: Users can only modify their own recipes
- ✅ **Data Validation**: Comprehensive input validation and error handling

## Tech Stack

- **Backend**: Django 6.0
- **API Framework**: Django REST Framework 3.16.1
- **Database**: SQLite (development)
- **Authentication**: Django's built-in authentication system
- **Additional Packages**:
  - django-cors-headers 4.9.0
  - django-filter 22.1

## Installation & Setup

### Prerequisites

- Python 3.8+
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/naijabites-api.git
cd naijabites-api
```

### Step 2: Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migrations

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Step 5: Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### Step 6: Start the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

| Method | Endpoint | Description | Authentication Required |
|--------|----------|-------------|-------------------------|
| GET | `/api/recipes/` | List all recipes (paginated) | No |
| POST | `/api/recipes/` | Create a new recipe | Yes |
| GET | `/api/recipes/<id>/` | Retrieve a specific recipe | No |
| PUT | `/api/recipes/<id>/` | Update a recipe (owner only) | Yes |
| PATCH | `/api/recipes/<id>/` | Partially update a recipe (owner only) | Yes |
| DELETE | `/api/recipes/<id>/` | Delete a recipe (owner only) | Yes |

### Query Parameters

**Pagination:**
- `page`: Page number (default: 1)
- `page_size`: Number of items per page (default: 10, max: 100)

**Search:**
- `search`: Search in title, description, and category

**Sorting:**
- `ordering`: Sort by field (options: `preparation_time`, `cooking_time`, `created_date`, `title`)
- Use `-` prefix for descending order (e.g., `ordering=-created_date`)

## Authentication

The API uses Django's built-in authentication system. Certain actions require authentication:

- **No Authentication Required**: GET requests to list and retrieve recipes
- **Authentication Required**: POST, PUT, PATCH, DELETE operations

### Authentication Methods

1. **Session Authentication**: Use Django admin login
2. **Token Authentication**: Include `Authorization: Token <your-token>` header

## Data Model

### Recipe Model

```json
{
  "id": "integer",
  "title": "string (max 255 chars)",
  "description": "text",
  "ingredients": "array of strings",
  "instructions": "text",
  "category": "string (max 100 chars)",
  "preparation_time": "integer (minutes)",
  "cooking_time": "integer (minutes)",
  "servings": "integer",
  "created_date": "datetime",
  "owner": "string (username)"
}
```

### Example Recipe

```json
{
  "title": "Jollof Rice",
  "description": "Classic Nigerian jollof rice with perfect flavor",
  "ingredients": ["rice", "tomatoes", "onions", "pepper", "seasoning"],
  "instructions": "Wash rice thoroughly. Blend tomatoes and peppers. Heat oil and sauté onions. Add blended mixture and cook. Add rice and water. Simmer until done.",
  "category": "main_course",
  "preparation_time": 15,
  "cooking_time": 45,
  "servings": 6
}
```

## Project Structure

```
naijabites-api/
├── core/                   # Django project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py
├── recipes/               # Recipe app
│   ├── __init__.py
│   ├── admin.py           # Django admin configuration
│   ├── apps.py            # App configuration
│   ├── migrations/        # Database migrations
│   ├── models.py          # Recipe model
│   ├── serializers.py     # API serializers
│   ├── tests.py           # Test cases
│   └── views.py           # API views
├── venv/                  # Virtual environment
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

## Usage Examples

### Create a New Recipe

```bash
curl -X POST http://127.0.0.1:8000/api/recipes/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token your-auth-token" \
  -d '{
    "title": "Efo Riro",
    "description": "Nigerian spinach stew",
    "ingredients": ["spinach", "palm oil", "assorted meat", "iru", "seasoning"],
    "instructions": "Wash and cut spinach. Heat palm oil and add ingredients. Cook until tender.",
    "category": "soup",
    "preparation_time": 20,
    "cooking_time": 35,
    "servings": 4
  }'
```

### Search Recipes

```bash
# Search for recipes containing "rice"
curl "http://127.0.0.1:8000/api/recipes/?search=rice"

# Filter by category and sort by cooking time
curl "http://127.0.0.1:8000/api/recipes/?category=main_course&ordering=cooking_time"
```

## Error Handling

The API returns appropriate HTTP status codes and error messages:

- `400 Bad Request`: Validation errors
- `401 Unauthorized`: Authentication required
- `403 Forbidden`: Permission denied (trying to modify another user's recipe)
- `404 Not Found`: Recipe not found
- `500 Internal Server Error`: Server error

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

[Your Name] - ALX Software Engineering Student

---

**Note**: This project was developed as part of the ALX Software Engineering curriculum. It demonstrates proficiency in Django REST Framework, API design, and full-stack development principles.
