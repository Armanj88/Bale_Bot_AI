import redis

# Connect to the local Redis instance
r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)


# Create a 'table' and add items to it
def add_item(table_name, item_id, item_data):
    for key, value in item_data.items():
        r.hset(f"{table_name}:{item_id}", key, value)


def get_item(table_name, item_id):
    return r.hgetall(f"{table_name}:{item_id}")


# Example usage:
table_name = "users"
item_id = "1"
item_data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "age": "30"
}

add_item(table_name, item_id, item_data)

item_id = "2"
item_data = {
    "name": "Jane Doe",
    "email": "jane.doe@example.com",
    "age": "25"
}

add_item(table_name, item_id, item_data)

print(get_item(table_name, "1"))