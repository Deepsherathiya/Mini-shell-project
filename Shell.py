import os
import sys
import subprocess

history=[] #stores used commands

def execute_command(parts):
    if not parts: #if invalid command prints the blank line
        return

    cmd=parts[0]  #parts is the list of input and [0] will be the command
    history.append(" ".join(parts))

    #exit
    if cmd in ["quit", "exit"]:
        print("Exiting...")
        sys.exit(0)

    #about
    elif cmd=="about":
        print("A custom shell that supports human-style commands")
        print("Type 'Help' to see all available commands")

    #help
    elif cmd=="help":
        print("""
         -> Shell — Available Commands

        - Navigation
          goto <dir> / cd <dir>           - Change directory
          where / pwd                     - Show current directory
          list / ls                       - Show files and folders

        - Files
          create / touch <file>           - Create a new empty file
          open / nano <file>              - Open file in editor
          top / cat / read <file>         - Show file content
          make / mkdir <folder>           - Create folder
          remove / rmdir <folder>         - Delete folder
          delete / rm <file>              - Delete file
          copy / cp <src> <dest>          - Copy file
          move / mv <src> <dest>          - Move or rename file
          save <cmd> to <file>            - Save output of a command to file

        - System
          user / whoami                   - Show current system user
          time / date                     - Show current date & time
          clear / cls                     - Clear the terminal screen

        - Misc
          say / echo / print <msg>        - Print a message on screen
          history                         - Show last 10 commands
          about                           - Show shell information
          help                            - Show this help menu
          exit / quit                     - Exit the shell
        """)
        return

    #navigation
    elif cmd in ["cd", "goto"]:
        if len(parts)<2:                          #checks if folder name is given
            print("Please enter a directory name")
        else:
            try:
                os.chdir(parts[1])                #change directory
            except FileNotFoundError:
                print("Directory not found")

        return


    elif cmd in ["pwd", "where"]:
        if os.name == "nt":
            subprocess.run("cd", shell=True)
        else:
            subprocess.run(["pwd"])
        return


    #screen
    elif cmd in ["clear", "cls"]:
        os.system("cls")
        return

    #make file
    elif cmd in ["create","touch"]:
        if len(parts)<2:
            print("Usage: create empty file.")
        else:
            open(parts[1], "w").close()
            print(f"Created {parts[1]}")
        return

    #make new folder
    elif cmd in ["make","mkdir"]:
        if len(parts)<2:
            print("Usage: make empty folder.")
        else:
            os.mkdir(parts[1])
            print(f"Created {parts[1]}")
        return

    #remove folder
    elif cmd in ["remove","rmdir"]:
        if len(parts)<2:
            print("Usage: remove folder.")
        else:
            os.rmdir(parts[1])
            print(f"Removed {parts[1]}")
        return

    #delete file
    elif cmd in ["delete", "rm"]:
        if len(parts)<2:
            print("Usage: delete file.")
        else:
            os.remove(parts[1])
            print(f"Deleted {parts[1]}")
        return

    #copy file
    elif cmd in ["copy", "cp"]:
        if len(parts) < 3:
            print("Usage: copy <source> <destination>")
        else:
            if os.name == "nt":
                # Windows
                subprocess.run(f"copy {parts[1]} {parts[2]}", shell=True)
            else:
                # Linux/macOS
                subprocess.run(["cp", parts[1], parts[2]])
            print(f"Copied '{parts[1]}' → '{parts[2]}'")
        return

    #move file
    elif cmd in ["move", "mv"]:
        if len(parts) < 3:
            print("Usage: move <source> <destination>")
        else:
            if os.name == "nt":
                # Windows
                subprocess.run(f"move {parts[1]} {parts[2]}", shell=True)
            else:
                # Linux/macOS
                subprocess.run(["mv", parts[1], parts[2]])
            print(f"Moved '{parts[1]}' → '{parts[2]}'")
        return


    #open file
    elif cmd in ["open","nano"]:
        if len(parts)<2:
            print("Usage: open file.")
        else:
            os.system(f"notepad {parts[1]}")
        return

    #starting of a file
    elif cmd in["read","cat","view","show"]:
        if len(parts)<2:
            print("Usage: read file.")
            return
        try:
            with open(parts[1], "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("File not found")
        return

    #system info
    elif cmd in ["whoami","who","user"]:
        subprocess.run(["whoami"])
        return

    elif cmd in ["time","date"]:
        subprocess.run("date /t", shell=True)

        return

    #list
    elif cmd in ["list", "ls"]:
        # For Windows -> use 'dir'
        if os.name == "nt":
            subprocess.run("dir", shell=True)
        else:
            subprocess.run(["ls"])
        return


    #history
    elif cmd in ["history"]:
        for i, h in enumerate(history[-10:], 1):
            print(f"{i}. {h}")
        return

    #default(other command)
    else:
        try:
            subprocess.run(parts)
        except FileNotFoundError:
            print("Command not found")

def main():
    print("Welcome to Custom Shell that supports human-style commands")
    print("Type 'Help' to see all available commands")

    while True:
        try:
            cwd=os.getcwd()
            command=input(f"Shell:{cwd}$: ").strip()
            if not command:
                continue
            execute_command(command.split())
        except KeyboardInterrupt:
            print("\nUse 'exit' or 'quit' to exit the shell")


if __name__ == "__main__":
    main()







