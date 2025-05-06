# Helldivers_2_Database
A Helldivers 2 web app based on the famous video game made by Arrowhead Game Studios

## Setup

### Prerequisites
- Python 3.x
- PostgreSQL database (or Neon database)

### Installation
1. Clone the repository
```bash
git clone https://github.com/yourusername/Helldivers_2_database.git
cd Helldivers_2_database
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up environment variables
Copy the `.env.example` file to `.env` and update the values:
```bash
cp .env.example .env
```

Edit the `.env` file with your database credentials and other settings:
- `DATABASE_URL`: Your PostgreSQL connection string
- `SECRET_KEY`: A secret key for Django
- `DEBUG`: Set to 'True' for development, 'False' for production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts

5. Run migrations
```bash
python manage.py migrate
```

6. Start the development server
```bash
python manage.py runserver
```

## Testing
To test the database connection:
```bash
python test_db_connection.py
```

## CI/CD Pipeline

This project uses GitHub Actions for continuous integration and deployment. The CI/CD pipeline includes:

- Automated testing
- Code linting
- Security scanning
- Code coverage tracking
- Docker image building
- Automated deployment to staging and production environments

For more details about the CI/CD setup, see the [CI/CD documentation](.github/workflows/README.md).

### Running the CI/CD Pipeline Locally

You can test parts of the CI/CD pipeline locally:

1. Run tests:
```bash
python manage.py test
```

2. Run linting:
```bash
pip install flake8
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

3. Run security scanning:
```bash
pip install bandit safety
bandit -r . -x ./tests,./venv
safety check -r requirements.txt
```

4. Run tests with coverage:
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
```
