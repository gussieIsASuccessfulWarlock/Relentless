"""
This script does the following:
1. Updates the apt sources
2. Upgrades apt
3. Dist-upgrades apt
4. Autoremoves apt
"""

import subprocess
import os
import sys
import saveOutputs

#function to check if user is root
def checkRoot():
    if os.geteuid() != 0:
        saveOutputs.error("Please run as root.")
        sys.exit()

aptSources = [
    {
        "name": "Ubuntu 18.04",
        "source": """
# See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to
# newer versions of the distribution.
deb http://us.archive.ubuntu.com/ubuntu/ bionic main restricted
# deb-src http://us.archive.ubuntu.com/ubuntu/ bionic main restricted

## Major bug fix updates produced after the final release of the
## distribution.
deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates main restricted
# deb-src http://us.archive.ubuntu.com/ubuntu/ bionic-updates main restricted

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
## team. Also, please note that software in universe WILL NOT receive any
## review or updates from the Ubuntu security team.
deb http://us.archive.ubuntu.com/ubuntu/ bionic universe
# deb-src http://us.archive.ubuntu.com/ubuntu/ bionic universe
deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates universe
# deb-src http://us.archive.ubuntu.com/ubuntu/ bionic-updates universe

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu 
## team, and may not be under a free licence. Please satisfy yourself as to 
## your rights to use the software. Also, please note that software in 
## multiverse WILL NOT receive any review or updates from the Ubuntu
## security team.
deb http://us.archive.ubuntu.com/ubuntu/ bionic multiverse
# deb-src http://us.archive.ubuntu.com/ubuntu/ bionic multiverse
deb http://us.archive.ubuntu.com/ubuntu/ bionic-updates multiverse
# deb-src http://us.archive.ubuntu.com/ubuntu/ bionic-updates multiverse

## N.B. software from this repository may not have been tested as
## extensively as that contained in the main release, although it includes
## newer versions of some applications which may provide useful features.
## Also, please note that software in backports WILL NOT receive any review
## or updates from the Ubuntu security team.
# deb http://us.archive.ubuntu.com/ubuntu/ bionic-backports main restricted universe multiverse
# deb-src http://us.archive.ubuntu.com/ubuntu/ bionic-backports main restricted universe multiverse

## Uncomment the following two lines to add software from Canonical's
## 'partner' repository.
## This software is not part of Ubuntu, but is offered by Canonical and the
## respective vendors as a service to Ubuntu users.
# deb http://archive.canonical.com/ubuntu bionic partner
# deb-src http://archive.canonical.com/ubuntu bionic partner

deb http://security.ubuntu.com/ubuntu bionic-security main restricted
# deb-src http://security.ubuntu.com/ubuntu bionic-security main restricted
deb http://security.ubuntu.com/ubuntu bionic-security universe
# deb-src http://security.ubuntu.com/ubuntu bionic-security universe
deb http://security.ubuntu.com/ubuntu bionic-security multiverse
# deb-src http://security.ubuntu.com/ubuntu bionic-security multiverse"""
    },
    {
        "name": "Ubuntu 20.04",
        "source": """
deb http://archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse

deb http://archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse

deb http://archive.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse

deb http://archive.ubuntu.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal-backports main restricted universe multiverse

deb http://archive.canonical.com/ubuntu focal partner
deb-src http://archive.canonical.com/ubuntu focal partner
"""
    },
    {
        "name": "Ubuntu 21.10",
        "source": """
deb http://id.archive.ubuntu.com/ubuntu/ groovy main universe restricted multiverse
deb-src http://id.archive.ubuntu.com/ubuntu/ groovy main universe restricted multiverse
deb http://security.ubuntu.com/ubuntu groovy-security main universe restricted multiverse
deb-src http://security.ubuntu.com/ubuntu groovy-security main universe restricted multiverse
deb http://id.archive.ubuntu.com/ubuntu/ groovy-updates main universe restricted multiverse
deb-src http://id.archive.ubuntu.com/ubuntu/ groovy-updates main universe restricted multiverse
deb http://id.archive.ubuntu.com/ubuntu groovy-backports main restricted universe multiverse
deb-src http://id.archive.ubuntu.com/ubuntu groovy-backports main restricted universe multiverse
deb http://archive.canonical.com/ubuntu groovy partner
deb-src http://archive.canonical.com/ubuntu groovy partner"""
    },
    {
        "name": "Ubuntu 21.",
        "source": """
# See http://help.ubuntu.com/community/UpgradeNotes for how to upgrade to
# newer versions of the distribution.
deb http://no.archive.ubuntu.com/ubuntu/ impish main restricted
deb-src http://no.archive.ubuntu.com/ubuntu/ impish main restricted

## Major bug fix updates produced after the final release of the
## distribution.
deb http://no.archive.ubuntu.com/ubuntu/ impish-updates main restricted
deb-src http://no.archive.ubuntu.com/ubuntu/ impish-updates main restricted

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
## team. Also, please note that software in universe WILL NOT receive any
## review or updates from the Ubuntu security team.
deb http://no.archive.ubuntu.com/ubuntu/ impish universe
deb-src http://no.archive.ubuntu.com/ubuntu/ impish universe
deb http://no.archive.ubuntu.com/ubuntu/ impish-updates universe
deb-src http://no.archive.ubuntu.com/ubuntu/ impish-updates universe

## N.B. software from this repository is ENTIRELY UNSUPPORTED by the Ubuntu
## team, and may not be under a free licence. Please satisfy yourself as to
## your rights to use the software. Also, please note that software in
## multiverse WILL NOT receive any review or updates from the Ubuntu
## security team.
deb http://no.archive.ubuntu.com/ubuntu/ impish multiverse
deb-src http://no.archive.ubuntu.com/ubuntu/ impish multiverse
deb http://no.archive.ubuntu.com/ubuntu/ impish-updates multiverse
deb-src http://no.archive.ubuntu.com/ubuntu/ impish-updates multiverse

## N.B. software from this repository may not have been tested as
## extensively as that contained in the main release, although it includes
## newer versions of some applications which may provide useful features.
## Also, please note that software in backports WILL NOT receive any review
## or updates from the Ubuntu security team.
deb http://no.archive.ubuntu.com/ubuntu/ impish-backports main restricted universe multiverse
deb-src http://no.archive.ubuntu.com/ubuntu/ impish-backports main restricted universe multiverse

## Uncomment the following two lines to add software from Canonical's
## 'partner' repository.
## This software is not part of Ubuntu, but is offered by Canonical and the
## respective vendors as a service to Ubuntu users.
# deb http://archive.canonical.com/ubuntu impish partner
# deb-src http://archive.canonical.com/ubuntu impish partner

deb http://security.ubuntu.com/ubuntu impish-security main restricted
deb-src http://security.ubuntu.com/ubuntu impish-security main restricted
deb http://security.ubuntu.com/ubuntu impish-security universe
deb-src http://security.ubuntu.com/ubuntu impish-security universe
deb http://security.ubuntu.com/ubuntu impish-security multiverse
deb-src http://security.ubuntu.com/ubuntu impish-security multiverse"""
    },
    {
        "name": "Ubuntu 22.04",
        "source": """
deb http://archive.ubuntu.com/ubuntu/ jammy main restricted universe multiverse
# deb-src http://archive.ubuntu.com/ubuntu/ jammy main restricted universe multiverse

deb http://archive.ubuntu.com/ubuntu/ jammy-updates main restricted universe multiverse
# deb-src http://archive.ubuntu.com/ubuntu/ jammy-updates main restricted universe multiverse

deb http://archive.ubuntu.com/ubuntu/ jammy-security main restricted universe multiverse
# deb-src http://archive.ubuntu.com/ubuntu/ jammy-security main restricted universe multiverse

deb http://archive.ubuntu.com/ubuntu/ jammy-backports main restricted universe multiverse
# deb-src http://archive.ubuntu.com/ubuntu/ jammy-backports main restricted universe multiverse

deb http://archive.canonical.com/ubuntu/ jammy partner
# deb-src http://archive.canonical.com/ubuntu/ jammy partner"""
    }
]

#function to fix apt
def updateSources():
    saveOutputs.info("Getting OS Release...")
    # get os-release
    os_release = subprocess.check_output(["cat", "/etc/os-release"])
    os_release = os_release.decode("utf-8")
    os_release = os_release.split("\n")
    for line in os_release:
        if line.startswith("VERSION_ID="):
            os_version = line.split("=")[1].replace('"', '')
        elif line.startswith("NAME="):
            os_name = line.split("=")[1].replace('"', '')
    # get official apt sources for os
    for aptSource in aptSources:
        if aptSource["name"] == os_name + " " + os_version:
            official_apt_source = aptSource["source"]
    try:
        official_apt_source
    except NameError:
        official_apt_source = None
    if official_apt_source == None:
        saveOutputs.error("Official apt source not found for " + os_name + " " + os_version + ". Your on your own.")
        sys.exit()
    else:
        # make backup of /etc/apt/sources.list
        saveOutputs.createDevider("APT Sources")
        saveOutputs.saveBackupOfFile("/etc/apt/sources.list")
        # save it to /etc/apt/sources.list
        with open("/etc/apt/sources.list", "w") as f:
            f.write(official_apt_source)
        saveOutputs.endDevider()
        saveOutputs.endDevider("Updating APT")
        # update apt
        subprocess.call(["apt", "update"])
        # upgrade apt
        subprocess.call(["apt", "upgrade", "-y"])
        saveOutputs.endDevider()
        saveOutputs.createDevider("Upgrading Ubuntu")
        # dist-upgrade apt
        if input("Do you want to uptdate Ubuntu to the latest? (y/n): ") == "y":
            subprocess.call(["apt", "dist-upgrade", "-y"])
        saveOutputs.endDevider()
        saveOutputs.createDevider("Cleaning Up")
        # autoremove apt
        subprocess.call(["apt", "autoremove", "-y"])
        saveOutputs.endDevider()

def main():
    checkRoot()
    saveOutputs.info("Updating Sources...")
    updateSources()
    saveOutputs.success("Sources Updated")
    if input("Do you want more ways to fix APT? (y/n): ") == "y":
        saveOutputs.info("Here are the commands or steps to address each of the common APT errors:")
        saveOutputs.success("Dependency Issues:")
        saveOutputs.info("  Command: sudo apt-get -f install")
        saveOutputs.info("  Explanation: This command attempts to fix unmet dependencies and completes pending installations or upgrades.")
        saveOutputs.success("Repository Issues:")
        saveOutputs.info("  Command: None (usually a temporary server issue)")
        saveOutputs.info("  Explanation: Check your internet connection, try again later, or update your repository URLs if they're misconfigured.")
        saveOutputs.success("Lock Files:")
        saveOutputs.info("  Command: sudo rm /var/lib/dpkg/lock")
        saveOutputs.info("  Explanation: This command removes the lock file, allowing APT to proceed. Make sure no other package management processes are running.")
        saveOutputs.success("Broken Packages:")
        saveOutputs.info("  Command: sudo dpkg --configure -a")
        saveOutputs.info("  Explanation: This command configures any pending package installations or upgrades and fixes any issues.")
        saveOutputs.success("Corrupted Cache:")
        saveOutputs.info("  Command: sudo apt-get clean")
        saveOutputs.info("  Explanation: This command cleans the package cache, removing corrupted or outdated files. Then run sudo apt update to refresh the cache.")
        saveOutputs.success("Invalid Configuration:")
        saveOutputs.info("  Command: Edit /etc/apt/sources.list and related files using a text editor like nano or gedit.")
        saveOutputs.info("  Explanation: Ensure the repository URLs are correct and properly formatted. You might need to consult official Ubuntu documentation for proper configurations.")
        saveOutputs.success("Disk Space Issues:")
        saveOutputs.info("  Command: Check available disk space using df -h and free up space by removing unnecessary files.")
        saveOutputs.info("  Explanation: Clearing up disk space allows APT to function properly.")
        saveOutputs.success("Network Problems:")
        saveOutputs.info("  Command: None (check your network connection or try later)")
        saveOutputs.info("  Explanation: Ensure you have a stable internet connection and consider using a reliable network.")
        saveOutputs.success("Authentication Errors:")
        saveOutputs.info("  Command: sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <KEY>")
        saveOutputs.info("  Explanation: Replace <KEY> with the GPG key ID causing the issue. This command fetches the missing key.")
        saveOutputs.success("Outdated Packages:")
        saveOutputs.info("  Command: sudo apt update and sudo apt upgrade")
        saveOutputs.info("  Explanation: Update the package lists and then upgrade installed packages to the latest versions.")
        saveOutputs.warning("If you need more help, please ask your perferred AI Bot.")