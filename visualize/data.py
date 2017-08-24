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

    def _convertToList(self, input):
        rows = 0
        l = list()
        for row in input:
            rows += 1
            val = (row.id, row.started,
                   ss.pretty_seconds(
                       (row.created_at - row.started).total_seconds()),
                   row.process.name, '"%s"' % row.window.title, row.nrkeys,)
            l.append(val)

        return l

    def _converKeysToDF(self, input):
        l = self._convertToList(input)
        return pd.DataFrame(l)

    def getKeys(self):
        """
        returns generator for keys
        """
        return self.stats.filter_keys()

    def getKeysDF(self):
        """
        returns data frame for filter_keys
        """
        df = self._converKeysToDF(self.getKeys())
        colNames = ["RowId",  "StartTime",  "Duration",
                    "Process", "WindowTitle", "keysPressed"]
        df.columns = colNames
        return df

    def getClicks(self):
        """
        returns generator for keys
        """
        return self.stats.filter_clicks()

    def getClicksDF(self):
        """
        returns data frame for filter_clicks
        """
        df = self._converKeysToDF(self.getKeys())
        colNames = ["RowId",  "StartTime",  "Duration",
                    "Process", "WindowTitle", "mouseMovements"]
        df.columns = colNames
        return df
