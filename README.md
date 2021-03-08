Provisioning a new site
===
## 需要的套件

* Nginx
* Python 3.8.5
* Django 3.1.7
* Git
* pip + pipenv
* pyenv

eg, on Ubuntu:
```
sudo apt update
sudo apt-get install git
```
## Install pyenv
```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
exec "$SHELL"
sudo apt-get update; sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
pyenv install 3.8.5
```

## Nginx 虛擬主機的設定
* see nginx.template.conf
* replace SITENAME with e.g., staging.my-domain.com

## Upstart 工作
* see gunicorn-upstart.template.conf
* replace SITENAME with e.g., staging.my-domain.com

## 資料夾結構
Assume we have a user account at /home/username
```
sites/
└── SITENAME
    ├── Pipfile
    ├── Pipfile.lock
    └── src
        ├── core
        ├── database
        ├── functional_test
        ├── app
        ├── static
```
