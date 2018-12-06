import json, os, subprocess


def load_secrets(secrets, selected_secrets = 0):

    secrets = json.load(open(secrets, 'r'))
    return secrets['credentials'][selected_secrets]


def build(secret = 'config.json'):

    secrets = load_secrets(secret)

    print(secrets)
    backup_database(secrets['username'], secrets['password'], secrets['database'], secrets['port'])


def backup_database(username, password, database, port = 3306):
    backup_command = "mysqldump -u %s %s -P%s -p%s > %s" % (username, database, port, password, 'mybackup_new.sql')

    os.system(backup_command)

def backup_codebase(codeBaseDir):

    pass


if __name__ == "__main__":

    print('Testing jenkins')
    build()
