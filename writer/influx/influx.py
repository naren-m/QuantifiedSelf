import argparse
import logger

from influxdb import InfluxDBClient


class Influx:
    def __init__(self, dbname, host='localhost', port=8086):
        user = 'root'
        password = 'root'
        self.dbname = dbname
        self.client = InfluxDBClient(host, port, user, password, dbname)

    def create_database(self):
        logger.debug("Create database: %s" + self.dbname)
        self.client.create_database(self.dbname)

    def write_json(self, data):
        logger.debug("Write points: %s", data)
        self.client.write_points(data)

    def write_data_frame(self, df, measurement, protocol='json'):
        logger.debug("Write dataframe to measurement: %s", measurement)
        self.client.write_points(df, measurement, protocol=protocol)

    def query(self, query):
        logger.debug("Queying data: " + query)
        result = self.client.query(query)
        return result

    def drop_database(self):
        logger.debug("Drop database: " + self.dbname)
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
    i.write_json(json_body)
    result = i.query(query)
    logger.debug("Result: %s", result)
    i.drop_database()


if __name__ == '__main__':
    main()
