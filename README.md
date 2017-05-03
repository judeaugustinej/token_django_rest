# token-django-rest
Trying out outh and jwt token authorization for django-rest-framework

### Jwt-token based authentication

* clone repo and switch to jwt-token branch

* Install the required libraries
```
cd token_django_rest/
pip install -r requirements.txt
```

* Create Admin user
```
python manange createsuper
```

* Generate jwt token.. use the username and password from previous step.
```
curl -X POST -d "username=<username>&password=<password>" http://localhost:8000/api/token/auth/

{"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imp1ZGUiLCJ1c2VyX2lkIjoxLCJlbWFpbCI6Imp1ZGVAZ21haWwuY29tIiwiZXhwIjoxNDkzODI3NzAx"}
```

* Access the protected endpoints
```
curl -H "Authorization: JWT <token>" http://127.0.0.1:8000/api/activity/?format=json
```

### Heroku deployment

* Edit setting.py for postgresdb support

* Run the migrations
```
heroku run python manage.py migrate
```

* Attach postgresDB
```
heroku addons:create heroku-postgresql:hobby-dev
```

* Public URL
```
https://dj-rest-demo.herokuapp.com/api/activity/
```

### Reference
* [How to make a full fledged REST API with Django OAuth Toolkit](https://www.youtube.com/watch?v=M6Ud3qC2tTk)
