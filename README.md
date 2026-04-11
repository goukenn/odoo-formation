# Formation Odoo

## installation 

- python, pip, postgressql

```bash
apt-get install python3 -y
apt-get install pip -y 
apt-get install git -y 
apt install postgresql postgresql-contrib -y
snap install dbeaver-ce --classic
```

- tart sql server

```bash
service postgresql start
```


## communication 

- Discord : [Room](https://discord.com/invite/rJ7D3wrj)


## projet d'integration 

[ ] to realise



## A. PostGre SQL 

postgres use authentication with system's user. 

the user is `postgres`
the client terminal to connect `psql`


```bash
sudo -u postgre psql
````

## manage database de donnée avec l'interface graphique 

- dbeaver-ce


## B. pgsq
get help \?
quit the shell \q


**Note:**
in php we need php-pgsql module to be installed

On MACOS

```zsh
brew install python3 # <- that will install pip3 
# create a link in /usr/local/bin because /usr/bin is readonly

brew install venv  # <- install python environment package manager
python -m venv dir_where_to_create_env  

# activate the environment
source dir_where_to_create_env/bin/activate

# install local so that debugger can resolve 
pip install -e .

```
