import fixAPT
import usersAndGroups
import saveOutputs
import checkApt

def main():
    saveOutputs.showLogo()
    userMode = saveOutputs.createMenuPicker("Main Menu", ["Fix APT", "Users and Groups", "Check APT Installed Files"])
    if userMode == 1:
        fixAPT.main()
    elif userMode == 2:
        usersAndGroups.main()
    elif userMode == 3:
        checkApt.main()
    else:
        saveOutputs.error("Invalid option")


if __name__ == '__main__':
    main()