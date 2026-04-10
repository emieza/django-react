# Projecte d'exemple de Django + React (Biblioteca)

Biblioteca amb llibres i imatges dels llibres

## Instal·lació Django

    $ python3 -m venv env
    (env) $ pip install -r requirements.txt
    (env) $ cp .env.example .env
    (env) $ ./manage.py createsuperuser
    (env) $ ./manage.py runserver

El servidor de desenvolupament estarà a http://localhost:8000

Es pot accedir l'admin panel a http://localhost:8000/admin

## Instal·lació React

    $ cd react
    $ npm install
    $ cp src/config.js.example src/config.js
    $ npm run dev

El servidor de desenvolupament Vite estarà a http://localhost:5173
