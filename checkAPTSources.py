import os
import saveOutputs

# in the cwd I have a file called reg.txt I want you to compare the output of the command "apt list --installed" to the contents of reg.txt
# if there is a difference, print the difference to the screen

def main():
    # open the file
    f = open("reg.txt", "r")
    # read the file
    reg = f.read()
    # close the file
    f.close()
    
    # run the command
    apt = os.popen("apt list --installed").read()
    
    # compare the two
    if reg != apt:
        saveOutputs.warning("APT sources are not the same:")
        # loop through the lines of the file
        for line in apt.splitlines():
            # if the line is not in the file
            if line not in reg:
                saveOutputs.warning("     " + line)