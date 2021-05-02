from cassandra.cluster import Cluster
from cassandra.query import ordered_dict_factory
from flask import app
import os


def connect_cassandra():
    cluster = Cluster([os.environ['CASSANDRA_HOST']],
                      port=os.environ['CASSANDRA_PORT'])
    session = cluster.connect(
        os.environ['CASSANDRA_DBNAME'], wait_for_all_pools=True)
    session.execute(f'USE {os.environ["CASSANDRA_DBNAME"]}')
    session.row_factory = ordered_dict_factory
    return session
