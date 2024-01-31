def log_changes(log_file, message):
    print(message)

    with open(log_file, 'a') as log:
        log.write(message + '\n')