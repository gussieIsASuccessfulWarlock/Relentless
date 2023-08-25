# Relentless

## Python Requierments
```bash 
pip install -r requirements.txt
```
## Run Python Script
```bash
python3 main.py
```

### What the script does
- Manages users and groups (In usersAndGroups.py)
- Creates users and groups (In usersAndGroups.py)
- Deletes users and groups (In usersAndGroups.py)
- Fixes apt sources (In fixApt.py)
- Updates and upgrades the system (In fixApt.py)
- Checks APT Installed Files (In checkApt.py)

## Manage Users and Groups
When managing users and groups you are often given a README. In that README you will find the authorized users. Our program doesn't know how to read the README as it doesn't have NLP (Natral Language Processing). Thus you must tell the program who is authorized and in which groups the should be in. You can do this by editing the users.csv file. In the file you will find a list of users and groups. You can add users and groups to the list. The program will then add the users and groups to the system. If you want to delete a user or group you can do so by removing the user or group from the list. The program will then delete the user or group from the system. Remember you can't just update the file you must run the script again after changes. With dummy data, the input file should look like this:
| User | Group |
|------|-------|
| Florine | managers:operators:sudo |
| Zion | managers |
| Adrien | managers:operators |
| Adelle | admin:sudo |

## Fixing APT
When fixing APT you are often given an error before installing a package, eventhough their isn't an error its alaways a good idea to run the fix apt script. This script will fix the apt sources and update and upgrade the system. This script is very simple to use. All you have to do is run the script and it will do the rest. (Note: This is still in development and may not work on all systems. As of now it only updates the apt sources and upgrades the system. It does not alaways fix the apt sources, although it provides some pointers.)

## Check Installed Files
When checking installed files you are often expected to know what should be installed. This script will cross check the normal files that are installed. If there are discrepancies it will tell you. This script is very easu to use. All you have to do is run the script and it will do the rest.

## Checklists
- [Checklist 1](https://github.com/gussieIsASucessfullWarlock/Relentless/blob/main/Checklist%201.md)

## Scripts fpr Forensics Questions
- [Hashes](https://github.com/gussieIsASucessfullWarlock/Hash-Finder)

### Supported OS
- Ubuntu
- Debian
- Parrot OS
- Kali Linux
