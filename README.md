## Bookie
### Making you want to read more books!

## About Bookie
Bookie is a website made for my django lesson.
A simple website developed using Vs code. This website has 2 features inside that you can use!

## features
- Adding books : Users can add new books to their booklist
- Searching books : Users can search books
- done

## Why bookie?
- Interactive Logout (hmz)
- Cute UI (Pink, cream, yellow, and green color palette)

## made with
Html, css, java script, Python, Django, Google books API, SQlite, Google fonts

## Local Setup & Run Instructions

Follow these steps to run Bookie on your local machine!!

### 1. Clone the Repository

Clone this repository, and then open the project folder:

```bash
git clone <repository-url>
cd Bookie
```

### 2. Create a Virtual Environment

Create a virtual environment:

```bash
python -m venv env
```

Activate it.

### 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Create an `.env` File

Create a file named:

```text
.env
```

Add your own environment variables:

```env
SECRET_KEY=your_django_secret_key
GOOGLE_BOOKS_API_KEY=your_google_books_api_key
```
Follow these tutorial for making google books API : https://developers.google.com/books/docs/v1/getting_started

### 5. Run Database Migrations

Apply the database migrations:

```bash
python manage.py migrate
```

### 6. Create an Admin Account (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

Then open the local address shown in your terminal!

## Environment Variables

Bookie requires these 2 variables :

| Variable               | Description                                                                |
| ---------------------- | -------------------------------------------------------------------------- |
| `SECRET_KEY`           | Secret key used by Django for security                                     |
| `GOOGLE_BOOKS_API_KEY` | API key used to search and retrieve book information from Google Books API |

The Google Books API is used for: titles, authors, genres, descriptions, and book covers.

## Useful Commands

Run the server:

```bash
python manage.py runserver
```

Create migrations:

```bash
python manage.py makemigrations
```

Apply migrations:

```bash
python manage.py migrate
```

Create an admin account:

```bash
python manage.py createsuperuser
```

DONE!!!

