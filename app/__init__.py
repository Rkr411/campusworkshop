"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaabhe7avj5o48jfds0-a.oregon-postgres.render.com",
        database="postgressql_a1yj",
        user="postgressql_a1yj_user",
        password="quick0ceHxxxE3WLPbPEY9X1gMXgdRDH")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
