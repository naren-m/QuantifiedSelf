
import data as d
import writer.influx.influx as influx

params = d.get_params("parameters.json")
params["back"] = ['500', 'd']
print params
selfStats = d.SelfSpy(params)


# Get list of stats and create dict
# RowId	StartTime	CreatedAt	Duration	Process	WindowTitle	keysPressed
fields = selfStats.getKeysDict()


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
