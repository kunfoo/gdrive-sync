# gdrive-sync
Python script and wrapper to sync files from google drive to local drive. This is meant to be run as a cronjob once a day.

# Installation
Create virtual environment and install pydrive:
```
mkdir venv
virtualenv -p `which python3` venv
. venv/bin/activate
pip install -U pip
pip install pydrive
```

Get your client ID and client secret from google cloud console. More information
on how to do this can be found here:
https://pythonhosted.org/PyDrive/quickstart.html

Now configure _settings.yaml_ from template.

Run `python sync-client.py` and follow instructions. You should now have a file
_creds.json_.

From now on, you can run `sync-wrapper.sh`.
