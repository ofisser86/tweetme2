# ![Django DRF TweetMe App](logo2.png)

### Example of Twitter-like app with Django DRF, Bootstrap, Javascript, & React.js

## Setup

### Install environment

1. Clone this repository: `git clone https://github.com/ofisser86/tweetme2.git`.
2. `cd` into `tweetme2`.
3. Install [pipenv](https://github.com/pypa/pipenv).
4. Install Python 3.7: `pipenv --pyhon 3.7`.
5. Launching subshell in virtual environment `pipenv shell`. If all went well then your command line prompt should now start with (tweetme2)
6. Generates Pipfile.lock and Installs all packages specified in Pipfile.lock `pipenv ` update.

### Perform database migration:
```bash
python manage.py check
python manage.py makemigrations
python manage.py migrate
```
### Run Development Server

```bash
python manage.py runserver
```
Public endpoint is at http://localhost:8000/

Admin endpoint is at http://127.0.0.1:8000/admin/

### For admin user
```bash
python manage.py createsuperuser
```
