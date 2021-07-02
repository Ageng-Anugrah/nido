# nido
## Django REST Sistem Login
Created by PTI 2018. Used by PTI 2019.

## Install Guide
Disclaimer: this instruction guide was run with linux OS, other OS might have slightly diffrent approach.

Clone
```
git clone https://gitlab.com/pti-bemcsui/nido
```

Create environment
```
python3 -m venv env
```

Activate environment
```
source env/bin/activate
```

Install requirement
```
pip3 install -r requirements.txt
```

Run
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

# API Documentation

Don't use `https://` in `next_page` argument please, it did not work anymore.

## Login

**URL** : `/api/auth/login/?next_page={next_page}`

**URL Example** : `/api/auth/login/?next_page=www.google.com`

**Method** : `GET`

## Success Response

`Will redirect to desired next page, with jwt_token in query parameters. Login in backend.`

**Redirect Page** : `{next_page}?token={jwt_token}`

**Redirect Example** : `https://www.google.com?token={the_token}`

---

## Logout

**URL** : `/api/auth/logout/?next_page={next_page}`

**URL Example** : `/api/auth/logout/?next_page=www.google.com`

**Method** : `GET`

## Success Response

`Will redirect to desired next page. Logout in backend`

**Redirect Page** : `{next_page}`

**Redirect Example** : `https://www.google.com`

---

## Fill Form Page
![screenshot](https://i.ibb.co/r3SdLqv/Screenshot-from-2019-09-05-15-21-17.png)

**URL** : `/profile/fill/{next_page}/{jwt_token}`

**URL Example** : `/profile/fill/www.google.com/{the_token}`

**Method** : `GET`
