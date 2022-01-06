from .models import Blog
from .cassandra import connect_cassandra


def get_posts(args):
    cassandra = connect_cassandra()
    query = 'select * from blog'
    if args:
        query += f""" where {" and ".join(f"{k}='{v}'" for k, v in args.items())} ALLOW FILTERING"""
    items = list(cassandra.execute(query))
    return [Blog(**item).dict() for item in list(map(dict, items)) if items]


def include_post(body):
    data = Blog(**body).dict()
    data['uid'] = str(data['uid'])
    data['created_at'] = str(data['created_at'])[:19]
    cassandra = connect_cassandra()
    query = f"""insert into blog {str(tuple(data.keys())).replace("'", '')} values {tuple(data.values())}"""
    res = cassandra.execute(query)
    return data


def delete_post(args):
    cassandra = connect_cassandra()
    query = f"""delete from blog where {" and ".join(f"{k}='{v}'" for k, v in args.items())}"""
    res = cassandra.execute(query)
    return 'Success'
