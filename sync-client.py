#!/usr/bin/env python

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.files import FileNotDownloadableError
from sys import exit
from shutil import move

SYNC_PATH="/home/kk/gdrive-sync/"

gauth = GoogleAuth()
gauth.CommandLineAuth()

drive = GoogleDrive(gauth)

# get ID of sync folder
folder_id = ""
file_list = drive.ListFile({"q": "'root' in parents and trashed=false"}).GetList()
for f in file_list:
    if "sync" == f["title"]:
        folder_id = f["id"]
if not folder_id:
    print("Error: could not find folder 'sync' in drive")
    exit(1)

sync_list = drive.ListFile({"q": f"'{folder_id}' in parents and trashed=false"}).GetList()
for f in sync_list:
    try:
        filename = f["title"]
        print(f"Downloading {filename}")
        f.GetContentFile(filename=filename, mimetype=f["mimeType"])
        print(f"Download successful. Moving {filename} to {SYNC_PATH}")
        try:
            move(filename, SYNC_PATH)
        except Exception as e:
            print(f"Exception {e} on move({filename}, {SYNC_PATH})")
        else:
            print(f"Moving successful. Trashing {filename}")
            f.Trash()
    except FileNotDownloadableError as fnde:
        print(f"file {f['title']} not downloadable")
    except Exception as e:
        print(f"Exception {e} on file {f['title']}")
