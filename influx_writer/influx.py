import argparse

from influxdb import InfluxDBClient


class Influx:
    def __init__(self, dbname, host='localhost', port=8086):
        user = 'root'
        password = 'root'
        self.dbname = dbname
        self.client = InfluxDBClient(host, port, user, password, dbname)

    def create_database(self):
        print("Create database: " + self.dbname)
        self.client.create_database(self.dbname)

    def write(self, data):
        print("Write points: {0}".format(data))
        self.client.write_points(data)

    def query(self, query):
        print("Queying data: " + query)
        result = self.client.query(query)
        return result

    def drop_database(self):
        print("Drop database: " + self.dbname)
        self.client.drop_database(self.dbname)


def main():
    db_name = "example"
    json_body = [
        {
            "measurement": "cpu_load_short",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": "2006-11-10T23:00:00Z",
            "fields": {
                "Float_value": 0.64,
                "Int_value": 3,
                "String_value": "Text",
                "Bool_value": True
            }
        }
    ]
    query = 'select value from cpu_load_short;'
    i = Influx(db_name)
    i.create_database()
    i.write(json_body)
    result = i.query(query)
    print("Result: {0}".format(result))
    i.drop_database()


if __name__ == '__main__':
    main()
