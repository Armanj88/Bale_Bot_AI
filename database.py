import redis


class Database:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

    def add_item(self, table_name, item_id, item_data):
        for key, value in item_data.items():
            self.redis.hset(f"{table_name}:{item_id}", key, value)

    def get_item(self, table_name, item_id):
        return self.redis.hgetall(f"{table_name}:{item_id}")

    def delete_field(self, table_name, item_id, field):
        self.redis.hdel(f"{table_name}:{item_id}", field)

    def delete_item(self, table_name, item_id):
        self.redis.delete(f"{table_name}:{item_id}")

    def reset_database(self):
        self.redis.flushdb()
