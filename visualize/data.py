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

    def _converKeysToDF(self, input):
        rows = 0
        l = list()
        for row in input:
            rows += 1
            val = (row.id, row.started,
                   ss.pretty_seconds(
                       (row.created_at - row.started).total_seconds()),
                   row.process.name, '"%s"' % row.window.title, row.nrkeys,)
            l.append(val)

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
        colNames = ["RowId",  "StartTime",  "Duration",
                    "Process", "WindowTitle", "keysPressed"]
        df = self._converKeysToDF(self.getKeys())
        df.columns = colNames
        return df

    def getClicks(self):
        """
        returns generator for keys
        """
        return self.stats.filter_clicks()
