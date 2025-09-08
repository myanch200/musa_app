# Musa writing app

Probably one of my first websites ever.
Done during my first years of university.
Using sqlite and django.

To see the glory of this project.

- Create python virtual environment:
   `python -m venv .env`
- Activate it:
   `source .env/bin/activate`
- Make sure you have db.sqlite3 in your root directory.
- Create `musa_app/secret_settings.py` and put an app secret key in there
  `python
    MUSA_APP_SECRET_KEY = ')!1=gdahq2z5r_4tc=s67cm22z8ll$ci&4+j1(3up8t!8jwv-0'
  `

Run

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`
- `python manage.py runserver`
