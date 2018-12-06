import json, os, subprocess


def load_config(configurations, configuration = 0):

    config = json.load(open(configurations, 'r'))
    return config['configurations'][configuration]


def build(secret = 'config.json'):
    print("Start...")

    config = load_config(secret)

    print(config)
    backup_database(config['name'], config['username'], config['password'], config['database'], config['backup_folder'], config['port'])


def backup_database(name, username, password, database, backup_folder, port=3306):
    backup_command = "mysqldump -u %s %s -p%s > %s" % (username, database, password, backup_folder+'/'+name+'.sql')

    os.system(backup_command)

def backup_codebase(codeBaseDir):

    pass


if __name__ == "__main__":

    print('Testing jenkins')
    build()
