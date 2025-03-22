# Online Restaurant API

A fully featured REST API backend for an online restaurant application built with Django and Django Rest Framework.

**Live API:** [https://online-restaurant-back-45jv9mohz-hexaalifs-projects.vercel.app/](https://online-restaurant-back-45jv9mohz-hexaalifs-projects.vercel.app/)

## Features

- User authentication with JWT
- Menu management system
- Food item categories
- Online ordering system
- Order tracking
- User profile and order history
- Admin dashboard API endpoints

## API Endpoints

### Authentication

- `POST /api/users/login` - Login User
- `POST /api/users` - Register new user

### User Profile

- `GET /api/users/${id}` - Get user profile
- `PUT /api/users/${id}` - Update user profile

### Restaurants

- `GET /api/restaurants` - List all Restaurants
- `GET /api/restaurants/{id}` - Retrieve specific menu item
- `POST /api/restaurants` - Add new menu item (Admin only)
- `PUT /api/restaurants/{id}` - Update menu item (Admin only)
- `DELETE /api/restaurants/{id}` - Delete menu item (Admin only)

### Menu

- `GET /api/restaurants/{restu_id}/menu` - List all menu items
- `GET /api/restaurants/{restu_id}/menu/{id}` - Retrieve specific menu item
- `POST /api/restaurants/{restu_id}menu/` - Add new menu item (Admin only)
- `PUT /api/restaurants/{restu_id}/menu/{id}` - Update menu item (Admin only)
- `DELETE /api/restaurants/{restu_id}/menu/{id}` - Delete menu item (Admin only)

### Orders

- `GET /api/orders/` - List user's orders (or all orders for Admin)
- `GET /api/orders/{id}/` - Retrieve specific order
- `POST /api/orders/` - Create new order
- `PUT /api/orders/{id}/` - Update order status (Admin only)

## Tech Stack

- **Django** - Web framework
- **Django Rest Framework** - API toolkit
- **PostgreSQL** - Database (in production)
- **SimpleJWT** - JWT authentication
- **Gunicorn** - WSGI HTTP Server
- **Vercel** - Deployment

## Installation & Setup

1. Clone the repository

```bash
git clone https://github.com/yourusername/online-restaurant-api.git
cd online-restaurant-api
```

2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Setup environment variables by creaeting .env file

```bash
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=postgres link
ALLOWED_HOSTS=['*']
```

5. Run migrations

```bash
python manage.py migrate
```

6. Create superuser|

```bash
python manage.py createsuperuser
```

7. Run the server

```bash
python manage.py runserver
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

Your Name - @Shad Ullah Sakib - hexaalif2020@gmail.com

Project Github Link: https://github.com/shadullah/online-restaurant-back
