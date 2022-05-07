# resilEyesDjangoTest

## Installation
- Go inside the directory in which you want to install the application:
  - `git clone git@github.com:Melissendra/resilEyesDjangoTest.git`
  - `cd resilEyesDjangoTest`

### Create your python environment:
  - `python3 -m venv .venv`
  - `source .venv/bin/activate`
  - `pip install -r requirements.txt`

### Configuration de l'application
- `python manage.py migrate`

If you want to use the django's admin system:
- `python manage.py createsuperuser`

- To launch the application: `python manage.py runserver`

## Endpoints
- Users list and creation of new one:
  - http://127.0.0.1:8000/api/v1/
- show details, update or delete of the selected user:
  - http://127.0.0.1:8000/api/v1/{pk} => example: http://127.0.0.1:8000/api/v1/1
- Admin page: Here you manage the users' authentication if necessary for other superuser: http://127.0.0.1:8000/admin/