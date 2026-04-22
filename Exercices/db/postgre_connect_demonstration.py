#!/usr/bin/env python 
# pip install psycopg2-binary
# use `psql` command line interface to manage and check access
# psql -h 0.0.0.0 -p 5432 -U user -d db

# check local : root is not connected by default is the `postgres`` user 
# so to connect use 
# $ sudo -u postgres psql 
# $# now we can create Database directly
# $# CREATE DATBASE demo;
# **NOTE:** if we want to use the period "." in database name we to put it in ""

import os
from psycopg2 import connect as dbConnect
from dotenv import load_dotenv
from lib.igk.database.dbconnexioninfo import DbConnexionInfo
from lib.igk.helpers.activator import Activator
from lib.igk.system.console.cli import *

load_dotenv()

cnx = Activator.CreateNewInstance(DbConnexionInfo, {
    'db':os.environ.get('PSQL_DB_NAME','mydb'),
    'user':os.environ.get('PSQL_USER', 'postsql'),
    'passwd':os.environ.get('PSQL_PWD'),
    'server':os.environ.get('PSQL_SERVER'),
    'port':os.environ.get('PSQL_PORT', '5432')
})

try:
    conn = dbConnect(**{
        "dbname":cnx.db,
        "user":cnx.user,
        "password":cnx.passwd,
        "host":cnx.server,
        "post": cnx.port
    })
except:
    print (cli.Red('Failed'))
else:
    print(cli.Green('Eureka'))
    cur = conn.cursor()
    cur.execute("SELECT version();")
    print(cur.fetchone())
    cur.close()
    conn.close()