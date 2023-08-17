import fixAPT
import usersAndGroups
import saveOutputs

def main():
    saveOutputs.showLogo()
    userMode = saveOutputs.createMenuPicker("Main Menu", ["Fix APT", "Users and Groups"])
    if userMode == 1:
        fixAPT.main()
    elif userMode == 2:
        usersAndGroups.main()
    else:
        saveOutputs.error("Invalid option")


if __name__ == '__main__':
    main()