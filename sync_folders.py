import os
import shutil

from calculate_file_hash import calculate_file_hash
from log_changes import log_changes

class SyncFolders:
    def __init__(self, source_path, replica_path, log_file) -> None:
        self.source_path = source_path
        self.replica_path = replica_path
        self.log_file = log_file

    def sync_folders(self):
        # check if source exist
        if not os.path.exists(self.source_path):
            print(f"{self.source_path} does not exist.")
            exit()

        # check if replica exist and create if not
        if not os.path.exists(self.replica_path):
            os.makedirs(self.replica_path)
            print(f'{self.replica_path} were created')

        # walk through files in the source
        for root, _, files in os.walk(self.source_path):
            for file in files:
                source_file_path = os.path.join(root, file)
                replica_file_path = os.path.join(self.replica_path, file)

                # if doesn't exist in replica, create it
                if not os.path.exists(replica_file_path):
                    shutil.copy(source_file_path, replica_file_path)
                    log_changes(self.log_file, f'{file} created in replica')

                # id exists in replica but not in source, delete it
                elif not os.path.exists(source_file_path):
                    os.remove(replica_file_path)
                    log_changes(self.log_file, f'{file} deleted from replica')

                # compare and update
                else:
                    source_hash = calculate_file_hash(source_file_path)
                    replica_hash = calculate_file_hash(replica_file_path)

                    if source_hash != replica_hash:
                        shutil.copy(source_file_path, replica_file_path)
                        log_changes(self.log_file, f'{file} updated in replica')
                    else:
                        log_changes(self.log_file, f'{file} without changes')
