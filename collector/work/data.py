import selfspy_stats as ss
import pandas as pd


def get_params(file_name):
    """
    Internal function to parse the parameter.json file and return dict
    """
    import ast

    with open(file_name) as data_file:
        data = data_file.read()
    return ast.literal_eval(data)


class SelfSpy:
    def __init__(self, parameters):
        self.args = parameters
        self.dbName = self.args['db_name']
        self.stats = ss.Selfstats(self.dbName, self.args)

    def _convertKeysToDF(self, data):
        rows = 0
        l = list()
        for row in data:
            rows += 1
            val = (row.id, row.started, row.created_at,
                   ss.pretty_seconds(
                       (row.created_at - row.started).total_seconds()),
                   row.process.name, '"%s"' % row.window.title, row.nrkeys)
            l.append(val)
        return pd.DataFrame(l)

    def getKeysDict(self):
        # Get list of stats and create dict
        kl = self.getKeys()
        fields = list()
        for i in kl:
            field = dict()
            field['id'] = int(i.id)
            field['started'] = i.started
            field['process'] = str(i.process.name)
            field['window_title'] = str(
                u' '.join((i.window.title, " ")).encode('utf-8').strip())
            field['duration'] = float(
                (i.created_at - i.started).total_seconds())
            field['duration_readable'] = str(ss.pretty_seconds(
                (i.created_at - i.started).total_seconds()))
            field['keys'] = int(i.nrkeys)
            fields.append(field)
        return fields

    def getKeys(self):
        """
        returns generator for keys
        """

        # def __init__(self, text, keys, timings, nrkeys, started, process_id,
        # window_id, geometry_id):

        return self.stats.filter_keys()

    def getKeysDF(self):
        """
        returns data frame for filter_keys
        """
        df = self._convertKeysToDF(self.getKeys())
        col_names = ["RowId",  "StartTime", "CreatedAt", "Duration",
                     "Process", "WindowTitle", "keysPressed"]
        df.columns = col_names
        return df

    def getClicks(self):
        """
        returns generator for keys
        """
        # def __init__(self, button, press, x, y, nrmoves, process_id,
        # window_id, geometry_id):

        return self.stats.filter_clicks()

    def getClicksDF(self):
        """
        returns data frame for filter_clicks
        """
        data = self.getClicks()
        rows = 0
        l = list()

        for row in data:
            rows += 1
            # print row.id, row.button, row.press,  row.nrmoves,
            # row.process_id, row.window_id, row.process, row.Duration
            val = (row.id, row.created_at, row.process.name, '"%s"' %
                   row.window.title, row.button, row.press, row.nrmoves,)
            l.append(val)
        col_names = ["RowId",  "CreatedAt", "Process",
                     "WindowTitle", "Button", "Pressed", "mouseMovements"]
        df = pd.DataFrame(l)
        df.columns = col_names

        return df
