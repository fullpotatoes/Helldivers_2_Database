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
