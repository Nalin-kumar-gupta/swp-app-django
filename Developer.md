# BUILD
docker-compose -f local.yml build --no-cache

# RUN
docker-compose -f local.yml up

# migrations 
docker-compose -f local.yml run web python manage.py makemigrations
docker-compose -f local.yml run web python manage.py migrate

# create super user
docker-compose -f local.yml run web python manage.py createsuperuser
