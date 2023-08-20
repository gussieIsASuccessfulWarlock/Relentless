import fixAPT
import usersAndGroups
import saveOutputs
import checkAPTSources

def main():
    saveOutputs.showLogo()
    userMode = saveOutputs.createMenuPicker("Main Menu", ["Fix APT", "Users and Groups", "Check APT Sources"])
    if userMode == 1:
        fixAPT.main()
    elif userMode == 2:
        usersAndGroups.main()
    elif userMode == 3:
        checkAPTSources.main()
    else:
        saveOutputs.error("Invalid option")


if __name__ == '__main__':
    main()