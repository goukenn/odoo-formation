# installation 
- install requirement
**Note:**
postgres sql require a valid user to exists on local machine

postgresql, start 
```bash
brew install postgresql
brew services start postgresql
# by installing postgresql we can use the `createuser` command line 
# create an odoo user
createuser -s odoo
# create a database for odoo user
createdb odoo_dev
# or
# psql -c 'create database odoo_dev WITH OWNER=odoo;'

# -s is for super user, -P for pwdprompt
```
- create a virtual python environment 

```bash
python -m venv venv
source venv/bin/activate
# for macos
xcode-select --install 
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```
---
**note if error on `psycopg2`

```bash 
pip install psycopg2-binary
# reload install 
pip install -r requirements.txt
```
---

## run odoo application
```bash
./odoo-bin -r odoo -d odoo_dev --addons-path=addons/
```

## easy run in docker

```bash
docker run -it --name odoo_app -v /Volumes/Data/Dev/odoo/contribution:/var/odoo -w /var/odoo -p 8069:8069 ubuntu:24.04 /bin/bash

$ apt-get update
$ apt-get install python3 -y 
$ apt-get install pip postgresql -y
$ apt-get install python3.12-venv

$ python3 -m venv venv
$ ip install --upgrade pip setuptools wheel
$ apt-get install sudo
$ service postgresql start 
# create an `odoo` user
$ useradd odoo
$ mkdir -p /home/odoo
$ chmod -R 775 /home/odoo
$ chmod -R odoo:odoo /home/odoo
$ sudo -u postgres createuser -s odoo
$ su odoo 
$ source venv/bin/activate
$ apt-get install libsasl2-dev python-dev-is-python3 libldap2-dev libssl-dev
$ apt install libpq-dev python3-dev
$ pip install psycopg2-binary
$ pip install python-ldap
$ pip install psycopg2

$ pip install -r requirements.txt

 
# initialize the database 
$ sudo -u posgres psql
~ create database odoo_dev;

# first run odoo server
./odoo-bin -r odoo -d odoo_dev --addons-path=addons/ -i base

# ignore the -i flag when database is already created 

# login: admin
# passwd: admin
```
