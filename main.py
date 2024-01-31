from time import sleep
from sync_folders import SyncFolders

LOG_FILE = 'sync_log.txt'

source = input('type source directory: ')
replica = input('type replica directory: ')
sync_interval = int(input('type syncronization interval in seconds: '))

sync_folders = SyncFolders(source_path=source, replica_path=replica, log_file=LOG_FILE)

while(True):
    sync_folders.sync_folders()
    sleep(sync_interval)