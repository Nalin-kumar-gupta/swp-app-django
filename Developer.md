## Root directory of the project
├── DEVELOPER.md                           ## Developer documentation
├── LICENSE                                ## License file for the project
├── README.md                              ## Readme file for the project

## API Shipper module
├── api_shipper
│   ├── admin.py                           ## Admin interface for API Shipper
│   ├── apps.py                            ## Apps configuration for API Shipper
│   ├── management                         ## Management commands for API Shipper
│   │   └── commands
│   │       └── populate_inventory.py      ## Populate inventory command
│   ├── migrations                         ## Database migrations for API Shipper
│   ├── models.py                          ## Data models for API Shipper
│   ├── script.py                          ## Script for API Shipper
│   ├── serializers.py                     ## Serializers for API Shipper
│   ├── tasks.py                           ## Tasks for API Shipper
│   ├── tests.py                           ## Tests for API Shipper
│   ├── urls.py                            ## URL configuration for API Shipper
│   └── views.py                           ## Views for API Shipper

## Base dependencies file
├── base.txt

## Client SWP module
├── client_swp
│   ├── public                             ## Public files for Client SWP
│   │   ├── assets                         ## Assets for Client SWP
│   │   │   └── images                     ## Images for Client SWP
│   │   ├── index.html                     ## Index HTML file for Client SWP
│   │   └── robots.txt                     ## Robots.txt file for Client SWP
│   └── src                                ## Source code for Client SWP
│       ├── App.css                        ## CSS file for App component
│       ├── App.js                         ## JavaScript file for App component
│       ├── components                     ## Components for Client SWP
│       │   ├── appBar.js                  ## App bar component
│       │   ├── plotComponent.js           ## Plot component
│       │   ├── productForm.js             ## Product form component
│       │   ├── productTable.js            ## Product table component
│       │   └── vehicleModal.js            ## Vehicle modal component
│       ├── index.css                      ## CSS file for index page
│       ├── index.js                       ## JavaScript file for index page
│       ├── pages                          ## Pages for Client SWP
│       │   └── ProductPage.js             ## Product page component
│       └── utils                          ## Utilities for Client SWP
│           └── webApi                     ## Web API utilities
│               ├── productApi.js          ## Product API utility
│               ├── vehicleApi.js          ## Vehicle API utility
│               └── visualizeApi.js        ## Visualize API utility

## Compose configuration
├── compose
│   └── local                              ## Local compose configuration
│       ├── django                         ## Django compose configuration
│       │   ├── Dockerfile                 ## Dockerfile for Django
│       │   ├── celery                     ## Celery configuration
│       │   │   ├── beat                   ## Beat configuration
│       │   │   │   └── start.sh           ## Start script for beat
│       │   │   ├── flower                 ## Flower configuration
│       │   │   │   └── start.sh           ## Start script for flower
│       │   │   └── worker                 ## Worker configuration
│       │   │       └── start.sh           ## Start script for worker
│       │   ├── entrypoint.sh              ## Entrypoint script for Django
│       │   ├── flask                      ## Flask configuration
│       │   │   └── start.sh               ## Start script for Flask
│       │   └── start.sh                   ## Start script for Django
│       └── webpack                        ## Webpack configuration
│           ├── Dockerfile                 ## Dockerfile for Webpack
│           └── start.sh                   ## Start script for Webpack

## Local YAML configuration
├── local.yml

## Manage script
├── manage.py

## Server SWP module
├── server_swp
│   ├── asgi.py                            ## ASGI configuration for Server SWP
│   ├── celery.py                          ## Celery configuration for Server SWP
│   ├── settings.py                        ## Settings for Server SWP
│   ├── urls.py                            ## URL configuration for Server SWP
│   └── wsgi.py                            ## WSGI configuration for Server SWP

## Shipper SWP module
└── shipper_swp
    ├── server.py                          ## Server script for Visualizer microservice


## BUILD
docker-compose -f local.yml build --no-cache

## RUN
docker-compose -f local.yml up

## migrations 
docker-compose -f local.yml run web python manage.py makemigrations
docker-compose -f local.yml run web python manage.py migrate

## create super user
docker-compose -f local.yml run web python manage.py createsuperuser

## create data
docker-compose -f local.yml run web python manage.py populate_inventory

## flush database -> populate inventory -> create super user
docker-compose -f local.yml run web python manage.py reset_inventory


## Package Viewset
List Packages: GET /api/packages/
Retrieve a Package: GET /api/packages/{id}/
Create a Package: POST /api/packages/
Update a Package: PUT /api/packages/{id}/ or PATCH /packages/{id}/
Delete a Package: DELETE /api/packages/{id}/

## Truck Viewset 
List Trucks: GET /api/trucks-boarding/
Retrieve a Truck: GET /api/trucks-boarding/{id}/
Create a Truck: POST /api/trucks-boarding/
Update a Truck: PUT /api/trucks-boarding/{id}/ or PATCH /trucks-boarding/{id}/
Delete a Truck: DELETE /api/trucks-boarding/{id}/