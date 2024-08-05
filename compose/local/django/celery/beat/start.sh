#!/bin/bash

set -o errexit
set -o nounset

rm -f './celerybeat.pid'
celery -A server_swp beat -l INFO