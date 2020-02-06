# Tech Profiles REST API

## Dev

### PostgreSQL
Install postgresql version 12 
Make sure you remember your password :-) 

Logon into postgres shell (usually psql or postgres)

```sql
CREATE DATABASE midburn;
CREATE USER midburn_admin WITH PASSWORD 'midburn_admin';
ALTER ROLE midburn_admin SET client_encoding TO 'utf8';
ALTER ROLE midburn_admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE midburn_admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE midburn TO midburn_admin;
```

### Python 3.7 

Usage of virtualenv is recommended
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Or using honcho

`honcho start -f profile.dev`

## Usage

http://localhost:7550/api/web-login/login

And then http://localhost:7550/docs