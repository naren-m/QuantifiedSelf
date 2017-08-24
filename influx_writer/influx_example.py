import argparse
import pandas as pd

from influx import *


def example_record():
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


def example_data_frame():
    db_name = "example"
    protocol = 'json'
    print("Create pandas DataFrame")
    df = pd.DataFrame(data=list(range(30)),
                      index=pd.date_range(start='2017-11-16',
                                          periods=30, freq='H'))
    query = 'select * from demo;'
    i = Influx(db_name)
    i.create_database()

    print("Write DataFrame")
    i.client.write_points(df, 'demo', protocol=protocol)

    # print("Write DataFrame with Tags")
    # i.client.write_points(
    #     df, 'demo', {'k1': 'v1', 'k2': 'v2'}, protocol=protocol)

    # result = i.query(query)
    # print("Result: {0}".format(result))
    i.drop_database()


if __name__ == '__main__':
    example_record()
    example_data_frame()
