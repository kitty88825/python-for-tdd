Provisioning a new site
=======================

## Required packages

* nginx
* Python 3.11 (use pyenv)
* poetry
* Git

eg, on Debian:

    sudo apt-get update
    sudo apt-get upgrade
    sudo apt install nginx

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

    ```
    export SITENAME=superlists-staging.ottg.eu
    sudo systemctl start nginx
    sudo ln -s /etc/nginx/sites-available/$SITENAME $SITENAME
    readlink -f $SITENAME
    sudo systemctl reload nginx
    ```

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

    ```
    vim /etc/systemd/system/gunicorn-$SITENAME.service
    sudo systemctl daemon-reload
    sudo systemctl enable gunicorn-$SITENAME
    sudo systemctl start gunicorn-$SITENAME

## poetry venv setting

* Create the virtualenv inside the project’s root directory.

    ```
    poetry config virtualenvs.in-project true
    ```

## Folder structure

Assume we have a user account at /home/username

    /home/username
    └── sites
        ├── DOMAIN1
        │    ├── superlist
        │    │    ├── .env
        │    ├── db.sqlite3
        │    ├── manage.py etc
        │    ├── static
        │    └── .venv
        └── DOMAIN2
            ├── .env
            ├── db.sqlite3
            ├── etc
