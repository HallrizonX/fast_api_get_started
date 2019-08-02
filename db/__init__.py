"""
Documentation
1) async/await https://peewee-async.readthedocs.io/en/latest/peewee_async/api.html
2) main - http://docs.peewee-orm.com/en/latest/peewee/querying.html#creating-a-new-record
"""

from peewee_async import PostgresqlDatabase

database = PostgresqlDatabase(
    'CUSTOMARY',
    user='postgres',
    password='postgres',
    host='127.0.0.1',
    port=6543
)
