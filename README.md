# Airbnb-clone

cloning Airbnb with Python, Django, Tailwind and AWS and more..

## Installation

### Pipenv

```bash
$ brew install pipenv
```

```bash
$ pipenv install --python $(which python3.7)
```

### Pillow Prerequisites

https://pillow.readthedocs.io/en/stable/installation.html

### Initialize

```bash
(airbnb_clone) python manage.py createsuperuser
(airbnb_clone) python manage.py makemigrations
(airbnb_clone) python manage.py migrate
```

### Tailwind

```bash
$ install node.js
$ sudo pip install npm
$ npm init
$ npm install gulp gulp-postcss gulp-sass gulp-csso node-sass -D
$ npm install tailwindcss -D
$ sudo npm install -g npx
$ npx tailwind init
$ npm i autoprefixer -D
$ npm run css
```

### AWS Elastic Beanstalk

```bash
$ pipenv install awsebcli --dev
```