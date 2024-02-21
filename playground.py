class Database:
    def __init__(self):
        self.data = {}
        
    def set(self, key, field, value):
        if key not in self.data:
            self.data[key] = {}
        self.data[key][field] = value
        return ""
    
    def get(self, key, field):
        if key not in self.data or field not in self.data[key]:
            return ""
        return self.data[key][field]
        
    def delete(self, key, field):
        if key not in self.data or field not in self.data[key]:
            return "false"
            
        del self.data[key][field]
        if not self.data[key]:
            del self.data[key]
        return "true"
        
    def scan(self, key):
        if key not in self.data:
            return ""
        fields = sorted(self.data[key].items())
        return ", ".join(f"{field}({value})" for field, value in fields)
        
    def scan_by_prefix(self, key, prefix):
        if key not in self.data:
            return ""
        filtered_fields = [(field, value) for field, value in self.data[key].items() if field.startswith(prefix)]
        sorted_fields = sorted(filtered_fields)
        return ", ".join(f"{field}({value})" for field, value in sorted_fields)
        
    def set_at(self, key, field, value, timestamp):
        if key not in self.data:
            self.data[key] = {}
        self.data[key][field] = (value, timestamp, None)
        return ""
        
    def set_at_with_ttl(self, key, field, value, timestamp, ttl):
        if key not in self.data:
            self.data[key] = {}
        self.data[key][field] = (value, timestamp, ttl)
        return ""
    
    def delete_at(self, key, field, timestamp):
        # TODO
        if key not in self.data or field not in self.data[key]:
            return "false"
        _, field_timestamp, ttl = self.data[key][field]
        if not ttl or int(timestamp) < int(field_timestamp) + int(ttl):
            del self.data[key][field]
            if not self.data[key]:
                del self.data[key]
            return "true"
        return "false"
        
    def get_at(self, key, field, timestamp):
        if key not in self.data or field not in self.data[key]:
            return ""
        value, field_timestamp, ttl = self.data[key][field]
        # print( + ", " + timestamp)
        if not ttl:
            return value
        if int(timestamp) < int(field_timestamp) + int(ttl):
            return value
        return ""
    
    def scan_at(self, key, timestamp):
        if key not in self.data:
            return ""
        fields = [
            (field, value)
            for field, (value, ts, ttl) in self.data[key].items()
            if not ttl or int(ts) + int(ttl) > int(timestamp)
        ]
        sorted_fields = sorted(fields, key=lambda x: x[0])
        return ", ".join(f"{field}({value})" for field, value in fields)
    
    def scan_by_prefix_at(self, key, prefix, timestamp):
        if key not in self.data:
            return ""
        filtered_fields = [
            (field, value)
            for field, (value, ts, ttl) in self.data[key].items()
            if not ttl or int(ts) + int(ttl) > int(timestamp) and field.startswith(prefix)
        ]
        sorted_fields = sorted(filtered_fields, key=lambda x: x[0])
        return ", ".join(f"{field}({value})" for field, value in sorted_fields)



def solution(queries):
    res = []
    db = Database()
    
    for q in queries:
        cmd, key = q[0], q[1]
        if cmd == "SET":
            output = db.set(key, q[2], q[3])
        elif cmd == "GET":
            output = db.get(key, q[2])
        elif cmd == "DELETE":
            output = db.delete(key, q[2])
        elif cmd == "SCAN":
            output = db.scan(key)
        elif cmd == "SCAN_BY_PREFIX":
            output = db.scan_by_prefix(key, q[2])
        elif cmd == "SET_AT":
            output = db.set_at(key, q[2], q[3], q[4])
        elif cmd == "SET_AT_WITH_TTL":
            output = db.set_at_with_ttl(key, q[2], q[3], q[4], q[5])
        elif cmd == "DELETE_AT":
            output = db.delete_at(key, q[2], q[3])
        elif cmd == "GET_AT":
            output = db.get_at(key, q[2], q[3])
        elif cmd == "SCAN_AT":
            output = db.scan_at(key, q[2])
        elif cmd == "SCAN_BY_PREFIX_AT":
            output = db.scan_by_prefix_at(key, q[2], q[3])
        res.append(output)
    
    return res
