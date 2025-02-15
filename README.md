# Goodreads Clone

A web application that replicates the core functionalities of Goodreads, allowing users to browse, review, and track books.

## Features

- User authentication and profile management
- Book search and filtering
- Adding books to personal shelves (Read, Currently Reading, Want to Read)
- Writing and viewing reviews
- Rating system
- Commenting on reviews
- Admin panel for book and user management

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Database:** PostgreSQL
- **Authentication:** JWT

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/goodreads-clone.git
   cd goodreads-clone
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations and start the server:
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

## Usage

- Register/Login to start tracking books
- Search for books and add them to shelves
- Rate and review books
- Engage with the community through comments

## Contribution

Feel free to open issues and submit pull requests to improve the project.

## License

This project is open-source and available under the MIT License.
