# Accessing fitbit data

## Requirements

- Register to Fitbit API as a personal type app
- Set the callback url to http://127.0.0.1:8080/
- Install [python-fitbit](https://github.com/orcasgit/python-fitbit)

## Steps to get Access to your data

Run [gather_keys_oauth2.py](https://github.com/orcasgit/python-fitbit/blob/master/gather_keys_oauth2.py) passing client id and client secret

```shell
➜  python-fitbit git:(master) python gather_keys_oauth2.py <client id> <client secret>

You are authorized to access data for the user: Naren Mudivarthy
TOKEN
=====

token_type = Bearer
user_id = blahblah
refresh_token = blahblah
access_token = blahblahblah
scope = [u'weight', u'heartrate', u'location', u'profile', u'settings', u'activity', u'nutrition', u'sleep', u'social']
```

Save the access and refresh tokens.