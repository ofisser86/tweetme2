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
## Testing

### Run tests:
```bash
python manage.py test
```

```bash
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..........
----------------------------------------------------------------------
Ran 10 tests in 0.025s

OK
Destroying test database for alias 'default'...
```

### Run tests with coverage:
```bash
pip install coverage
coverage run --source='.' manage.py test
```

### Check coverage report:
```bash
coverage report
```

```bash
Name                                             Stmts   Miss  Cover
--------------------------------------------------------------------
accounts/__init__.py                                 0      0   100%
accounts/admin.py                                    1      0   100%
accounts/apps.py                                     3      3     0%
accounts/migrations/__init__.py                      0      0   100%
accounts/models.py                                   1      0   100%
accounts/tests.py                                    1      0   100%
accounts/views.py                                   26     20    23%
manage.py                                           12      2    83%
profiles/__init__.py                                 0      0   100%
profiles/admin.py                                    3      0   100%
profiles/api/__init__.py                             0      0   100%
profiles/api/urls.py                                 3      0   100%
profiles/api/views.py                               30      1    97%
profiles/apps.py                                     3      3     0%
profiles/forms.py                                   23      0   100%
profiles/migrations/0001_initial.py                  7      0   100%
profiles/migrations/0002_auto_20200718_1301.py       7      0   100%
profiles/migrations/__init__.py                      0      0   100%
profiles/models.py                                  22      1    95%
profiles/serializers.py                             30      0   100%
profiles/tests.py                                   46      0   100%
profiles/urls.py                                     3      0   100%
profiles/views.py                                   34     28    18%
tweetme2/__init__.py                                 0      0   100%
tweetme2/rest_api/__init__.py                        0      0   100%
tweetme2/rest_api/dev.py                             8      3    62%
tweetme2/settings.py                                32      0   100%
tweetme2/urls.py                                    11      1    91%
tweetme2/wsgi.py                                     4      4     0%
tweets/__init__.py                                   0      0   100%
tweets/admin.py                                     11      0   100%
tweets/api/__init__.py                               0      0   100%
tweets/api/urls.py                                   3      0   100%
tweets/api/views.py                                118     42    64%
tweets/apps.py                                       3      3     0%
tweets/forms.py                                     12      4    67%
tweets/migrations/0001_initial.py                    5      0   100%
tweets/migrations/0002_auto_20200518_0737.py         4      0   100%
tweets/migrations/0003_tweet_user.py                 6      0   100%
tweets/migrations/0004_auto_20200519_1355.py         7      0   100%
tweets/migrations/0005_tweet_parent.py               5      0   100%
tweets/migrations/0006_auto_20200717_1212.py         6      0   100%
tweets/migrations/__init__.py                        0      0   100%
tweets/models.py                                    37      8    78%
tweets/serializers.py                               36      2    94%
tweets/tests.py                                     85      4    95%
tweets/views.py                                     12      3    75%
--------------------------------------------------------------------
TOTAL                                 162     19    88%
```

