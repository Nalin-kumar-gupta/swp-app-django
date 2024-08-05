#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

function migrate() {
    echo "Running database migrations..."
    python manage.py migrate
    if [ $? -eq 0 ]; then
        echo "Database ready"
    else
        echo "Database migration failed"
        exit 1
    fi
}

# Run migrations
migrate

# Start the Django development server
python manage.py runserver 0.0.0.0:8000