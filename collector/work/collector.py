import schedule
import time
import webbrowser
import configparser as cfg

import writer.influx.influx as influx

from data import get_params, SelfSpy


class Exporter():
    """
    Data exporter to influx
    """

    def __init__(self):
        config_file = 'config.ini'
        self.config = cfg.ConfigParser()
        self.config.read(config_file)

    def get_cadence(self):
        cadence = self.config.get('work', 'cadence')
        return cadence.split(" ")

    def get_parameters_file(self):
        return self.config.get('work', 'parameters')

    def get_data(self):
        params = get_params(self.get_parameters_file())
        params["back"] = self.get_cadence()
        print params
        selfStats = SelfSpy(params)

        # Get list of stats and create dict
        # RowId	StartTime CreatedAt	Duration Process WindowTitle keysPressed
        fields = selfStats.getKeysDict()
        return fields

    def save_data_to_influx(self):
        fields = self.get_data()
        measurement = "keys"

        tags = dict()
        all_data = list()
        for f in fields:
            data = dict()
            tag = dict()
            tag['processes'] = f['process']
            data['measurement'] = measurement
            data['tags'] = tag
            data['time'] = f['started']
            del f['started']
            data['fields'] = f
            all_data.append(data)
        db_name = "selfspy"
        i = influx.Influx(db_name)
        i.create_database()

        print("Write json")
        print len(all_data)

        for d in all_data:
            print d
            ld = list()
            ld.append(d)
            i.write_json(ld)


def main():
    e = Exporter()
    # print e.get_cadence()
    # print e.get_data()
    e.save_data_to_influx()
    c = e.get_cadence()
    t = int(c[0])

    if c[1] == "m":
        schedule.every(t).minutes.do(e.save_data_to_influx)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    main()
