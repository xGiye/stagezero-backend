# Stage Zero Backend Task

## Overview
A Django REST API endpoint `/me` that returns profile info and a random cat fact.

---

## Endpoint
**GET** `/me`

### Example Response
```json
{
  "status": "success",
  "user": {
    "email": "email@example.com",
    "name": "Full name",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-18T11:25:44.789Z",
  "fact": "Cats have five toes on their front paws, but only four on the back."
}
```
## Running Locally

```
git clone https://github.com/<your-username>/stagezero_backend.git
cd stagezero_backend
pip install -r requirements.txt
```
###  Create .env file 
```
USER_EMAIL=youremail@hostname.com
USER_NAME=Your full name
USER_STACK=Your stack
```
###  Run
```
python manage.py runserver
```
```Visit: http://127.0.0.1:8000/me ```


## Deployment
```
Deployed on: Railway
Endpoint: https://your-deployed-url/me
```
