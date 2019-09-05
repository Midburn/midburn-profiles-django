# Tech Profile/Ticketing POC

## Dev

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