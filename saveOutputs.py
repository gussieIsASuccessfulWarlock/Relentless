import os
import rich

def error(message):
    rich.print(f"[bold red]Error: {message}[/bold red]")

def success(message):
    rich.print(f"[bold green]Success: {message}[/bold green]")

def info(message):
    rich.print(f"[bold blue]Info: {message}[/bold blue]")

def warning(message):
    rich.print(f"[bold yellow]Warning: {message}[/bold yellow]")

def createDevider(title):
    rich.print("")
    rich.print("[bold blue]==============================================================================[/bold blue]")
    rich.print(f"[bold blue]{title}[/bold blue]")

def endDevider():
    rich.print("[bold blue]==============================================================================[/bold blue]")

def showLogo():
    logo = """
__________       .__                 __  .__                        
\______   \ ____ |  |   ____   _____/  |_|  |   ____   ______ ______
 |       _// __ \|  | _/ __ \ /    \   __\  | _/ __ \ /  ___//  ___/
 |    |   \  ___/|  |_\  ___/|   |  \  | |  |_\  ___/ \___ \ \___ \ 
 |____|_  /\___  >____/\___  >___|  /__| |____/\___  >____  >____  >
        \/     \/          \/     \/               \/     \/     \/                                 
"""
    # print the logo as info
    info(logo)

# Create a menu picker returning the picked option
def createMenuPicker(title, options):
    createDevider(title)
    for i in range(len(options)):
        rich.print(f"[bold blue]{i+1}[/bold blue] - {options[i]}")
    endDevider()
    while True:
        try:
            pickedOption = int(input(f"Pick an option (1-{len(options)}): "))
            if pickedOption > 0 and pickedOption <= len(options):
                return pickedOption
            else:
                error(f"Option {pickedOption} does not exist")
        except ValueError:
            error("Please enter a number")

def saveBackupOfFile(path):
    if not os.path.exists("backups"):
        os.popen("sudo mkdir backups")
        info("Created backups directory")
    if os.path.exists(path):
        if os.path.exists(f"backups/{path.replace('/', '_')}.bak"):
            if input(f"Backup of {path} already exists. Overwrite? (y/n) ") == 'y':
                os.popen(f"sudo cp {path} backups/{path.replace('/', '_')}.bak")
                success(f"Backup of {path} created as backups/{path.replace('/', '_')}.bak")
            else:
                info(f"Backup of {path} not created")
        else:
            os.popen(f"sudo cp {path} backups/{path.replace('/', '_')}.bak")
            success(f"Backup of {path} created as backups/{path}.bak")
    else:
        error(f"File {path} does not exist")