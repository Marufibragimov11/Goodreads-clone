# Goodreads Clone

This repository hosts a clone of Goodreads, developed to explore and implement backend functionalities using Django. The project focuses on managing books, reviews, and user interactions, aiming to replicate the core features of Goodreads.

## Features

- User authentication and authorization
- Adding, updating, and deleting books
- User reviews and ratings for books
- Searching for books
- User profiles

## Technologies Used

- Django
- PostgreSQL
- HTML/CSS/JavaScript for the frontend
- Django Rest Framework

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- Python 3.9 or higher
- Django 4.0
- PostgreSQL

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Marufibragimov11/Goodreads-clone.git
    cd Goodreads-clone
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    - Update the `DATABASES` setting in `settings.py` to configure your database.
    - Run the migrations:

    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    Open your browser and navigate to `http://127.0.0.1:8000/` to see the application running.

## Usage

- **Register and Login:** Create an account and log in.
- **Add Books:** Add new books to the database.
- **Review Books:** Leave reviews and ratings for books.
- **Search:** Use the search functionality to find books by title, author, or genre.
- **Profile:** View and update your user profile.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or suggestions, feel free to contact me at [your email address] or create an issue in this repository.

---

*Note: This project is for educational purposes. The implementation details may not fully replicate the original Goodreads website.*
