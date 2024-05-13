# Storefront v3.0

The Django Store Application is a powerful backend API designed to facilitate the management of e-commerce operations such as products, collections, customers, orders, and reviews. Built on the Django framework and powered by the Django REST Framework, this application offers a robust backend infrastructure coupled with a flexible and scalable API for seamless integration with frontend applications.

## Installation and Setup

1. Clone the repository to your local machine:

```
git clone https://github.com/NipunChamika/storefront-v3.0.git
```

2. Navigate to the project directory:

```
cd storefront-v3.0
```

3. Install Pipenv (if not already installed):

```
pip install pipenv
```

4. Configure the database settings in `storefront/settings/dev.py` file before applying migrations:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Change this to your database engine
        'NAME': 'storefront3',  # Change this to your database name
        'HOST': 'localhost',  # Change this to your database host
        'USER': os.getenv('DATABASE_USER'),  # Change this to your database user
        'PASSWORD': os.getenv('DATABASE_PASSWORD')  # Change this to your database password
    }
}
```

5. Install dependencies using Pipenv:

```
pipenv install
```

6. Activate the virtual environment:

```
pipenv shell
```

7. Apply database migrations:

```
python manage.py migrate
```

8. Populate the database with seed data:

```
python manage.py seed_db
```

9. Create a superuser to access the admin interface:

```
python manage.py createsuperuser
```

10. Start the development server:

```
python manage.py runserver
```

## API Endpoints

- `/admin/`
- `/store/products/`
- `/store/products/{id}/`
- `/store/collections/`
- `/store/collections/{id}/`
- `/store/carts/`
- `/store/carts/{id}/`
- `/store/carts/{id}/items/`
- `/store/carts/{id}/items/{id}`
- `/store/customers/`
- `/store/customers/{id}/`
- `/store/orders/`
- `/store/orders/{id}/`
- `/auth/jwt/create/`
- `/auth/jwt/refresh/`
