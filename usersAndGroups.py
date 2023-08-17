"""
This script does the following:
1. Reads a .csv file containing a list of users and groups
2. Creates the users and groups
3. Adds the users to the groups
4. Removes users that are not in the .csv file
"""

import csv
import subprocess
import saveOutputs

# Golbal variables
csv_path = 'users.csv'
input_file = input("Enter the path to the .csv file (users.csv): ")
if input_file != '':
    csv_path = input_file
authorized_users =[]

# Support Functions
def checkShell(user):
    #check if user has bash shell
    if subprocess.call(["egrep", "-e", f"^{user}:.*sh$", "/etc/passwd"], stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
        return True
    else:
        return False

def main():
    global authorized_users, csv_path
    saveOutputs.saveBackupOfFile('/etc/shadow')
    saveOutputs.saveBackupOfFile('/etc/passwd')
    saveOutputs.saveBackupOfFile('/etc/group')

    # Open the .csv file
    with open(csv_path, 'r') as file:
        # Create a csv reader object
        reader = csv.reader(file)
        # Skip the header line
        next(reader)
        # Iterate over each row in the .csv file
        saveOutputs.createDevider("Users and Groups")
        for row in reader:
            # Define the username, group, and group type
            username = row[0]
            authorized_users.append(username)
            groups = row[1].split(':')
            # Check to see if the user exists
            if subprocess.run(['grep', '-q', f'^{username}:', '/etc/passwd']).returncode == 0:
                # If the user exists, print a message
                saveOutputs.info(f'{username} already exists')
            else:
                # If the user does not exist, create the user
                subprocess.run(['useradd', username])
                saveOutputs.success(f'{username} has been created')
            # Check to see if the group exists
            for group in groups:
                if subprocess.run(['grep', '-q', f'^{group}:', '/etc/group']).returncode == 0:
                    # If the group exists, check to see if the user is a member of the group
                    if subprocess.run(['grep', '-q', f'^{group}:.*{username}', '/etc/group']).returncode == 0:
                        # If the user is a member of the group, print a message
                        saveOutputs.info(f'{username} is already a member of {group}')
                    else:
                        # If the user is not a member of the group, add them to the group
                        subprocess.run(['usermod', '-a', '-G', group, username])
                        saveOutputs.success(f'{username} has been added to {group}')
                else:
                    # If the group does not exist, create the group
                    subprocess.run(['groupadd', group])
                    saveOutputs.success(f'{group} has been created')
                    # Add the user to the group
                    subprocess.run(['usermod', '-a', '-G', group, username])
                    saveOutputs.success(f'{username} has been added to {group}')

                # Check to see if user is in group unallowed by the .csv file
            for group in subprocess.run(['groups', username], capture_output=True, text=True).stdout.split(':')[-1].strip().split(' '):
                if group not in groups and group != username and group != 'users':
                    group = group.strip()
                    # remove user from group
                    if input(f'{username} is in {group} but should not be. Remove? (y/n) ') == 'y':
                        subprocess.run(['gpasswd', '-d', username, group])
                        saveOutputs.success(f'{username} has been removed from {group}')
        saveOutputs.endDevider()
    saveOutputs.createDevider("Checking For Unauthorized Users")
    # Find users not in the .csv file
    for user in subprocess.run(['cut', '-d:', '-f1', '/etc/passwd'], capture_output=True, text=True).stdout.split('\n'):
        if user not in authorized_users and user != 'root':
            # check if user must be in BIN/BASH or /sbin/nologin or /BIN/ZSH else log it 
            if checkShell(user):
                saveOutputs.error(f'{user} is not authorized to be on the system')
                # remove user
                subprocess.run(['userdel', user])
                saveOutputs.success(f'{user} has been removed from the system')
            else:
                saveOutputs.createDevider("Unknow User")
                saveOutputs.warning(f'{user} is not authorized to be on the system and is not in a valid shell')
                saveOutputs.endDevider()
    saveOutputs.endDevider()