#!/usr/bin/env bash

set -e

# TODO: Set to URL of git repo.
PROJECT_GIT_URL='https://github.com/nandastraadi/deploycapstone.git'

PROJECT_BASE_PATH='/usr/local/apps/deploycapstone'

echo "Installing dependencies..."
apt-get update


####################
apt-get -y remove docker docker.io 
####################

apt-get install -y build-essential python3-dev libssl-dev libffi-dev libpq-dev
apt-get install -y python3-dev python3-venv sqlite python3-pip supervisor nginx git docker.io

####################
systemctl start docker
systemctl enable docker
sudo chmod 666 /var/run/docker.sock
docker run -p 6379:6379 -d redis:2.8
####################


# Create project directory
mkdir -p $PROJECT_BASE_PATH
git clone $PROJECT_GIT_URL $PROJECT_BASE_PATH

# Create virtual environment
mkdir -p $PROJECT_BASE_PATH/env
python3 -m venv $PROJECT_BASE_PATH/env

# Install python packages
$PROJECT_BASE_PATH/env/bin/pip install --upgrade pip
$PROJECT_BASE_PATH/env/bin/pip install -r $PROJECT_BASE_PATH/requirements.txt
$PROJECT_BASE_PATH/env/bin/pip install uwsgi==2.0.18

# Run migrations and collectstatic
cd $PROJECT_BASE_PATH
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
$PROJECT_BASE_PATH/env/bin/python manage.py collectstatic --noinput

#############################
# cd kualitasairapi
# $PROJECT_BASE_PATH/env/bin/chasgimqtt -H test.mosquitto.org -p 1883 --topic=capstone_kualitas_air:2 kualitasairapi.asgi:channel_layer -n mqtt.sub -v &
# sudo $PROJECT_BASE_PATH/env/bin/python manage.py runworker mqtt.sub &
#############################


# Configure supervisor
cp $PROJECT_BASE_PATH/deploy/supervisor_deploycapstone.conf /etc/supervisor/conf.d/deploycapstone.conf
supervisorctl reread
supervisorctl update
supervisorctl restart deploycapstone

# Configure nginx
cp $PROJECT_BASE_PATH/deploy/nginx_deploycapstone.conf /etc/nginx/sites-available/deploycapstone.conf
rm /etc/nginx/sites-enabled/default
ln -s /etc/nginx/sites-available/deploycapstone.conf /etc/nginx/sites-enabled/deploycapstone.conf
systemctl restart nginx.service

echo "DONE! :)"
