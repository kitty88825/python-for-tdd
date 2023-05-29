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

## Nginx Virtual Host config

* see nginx.template.conf
* replace DOMAIN with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace DOMAIN with, e.g., staging.my-domain.com

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
