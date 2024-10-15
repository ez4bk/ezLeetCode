from in_memory_db import InMemoryDB
from collections import defaultdict

class InMemoryDBImpl(InMemoryDB):
    def __init__(self):
        self.records = defaultdict(lambda: defaultdict(list))

    def set(self, timestamp, key, field, value):
        self.set_with_ttl(timestamp, key, field, value, ttl=float('inf'))

    def set_with_ttl(self, timestamp, key, field, value, ttl):
        expiration_time = timestamp + ttl
        self.records[key][field].append((timestamp, value, expiration_time))

    def compare_and_set(self, timestamp, key, field, expected_value, new_value):
        return self.compare_and_set_with_ttl(timestamp, key, field, expected_value, new_value, ttl=float('inf'))

    def compare_and_set_with_ttl(self, timestamp, key, field, expected_value, new_value, ttl):
        expiration_time = timestamp + ttl
        if key in self.records and field in self.records[key]:
            latest_value, latest_expiration = self.records[key][field][-1][1], self.records[key][field][-1][2]
            if latest_expiration > timestamp and latest_value == expected_value:
                self.records[key][field].append((timestamp, new_value, expiration_time))
                return True
        return False

    def compare_and_delete(self, timestamp, key, field, expected_value):
        if key in self.records and field in self.records[key]:
            latest_value, latest_expiration = self.records[key][field][-1][1], self.records[key][field][-1][2]
            if latest_expiration > timestamp and latest_value == expected_value:
                del self.records[key][field]
                if not self.records[key]:
                    del self.records[key]
                return True
        return False

    def get(self, timestamp, key, field):
        if key in self.records and field in self.records[key]:
            latest_value, latest_expiration = self.records[key][field][-1][1], self.records[key][field][-1][2]
            if latest_expiration > timestamp:
                return latest_value
        return None

    def get_when(self, timestamp, key, field, at_timestamp):
        if at_timestamp == 0:
            return self.get(timestamp, key, field)
        
        if key in self.records and field in self.records[key]:
            for ts, value, expiration in reversed(self.records[key][field]):
                if ts <= at_timestamp < expiration:
                    return value
        return None

    def scan(self, timestamp, key):
        if key in self.records:
            return [f"{field}({self.records[key][field][-1][1]})" for field in sorted(self.records[key]) if self.records[key][field][-1][2] > timestamp]
        return []

    def scan_by_prefix(self, timestamp, key, prefix):
        if key in self.records:
            return [f"{field}({self.records[key][field][-1][1]})" for field in sorted(self.records[key]) if field.startswith(prefix) and self.records[key][field][-1][2] > timestamp]
        return []