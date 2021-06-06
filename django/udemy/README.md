py -m venv venv
django-admin startproject nombre
pip install -r requirements.txt
py manage.py migrate
dentro de la carpeta applications-- django-admin startapp nombre


#commandos para el tutorial rest
docker-compose run app sh -c "python manage.py test"
docker-compose run app sh -c "python manage.py test && flake8"