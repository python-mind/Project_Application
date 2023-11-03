import time
import sys
import os


def input(msg):
    print(msg)
    try:
        line = sys.stdin.readline().split('\n')
    except Exception as e:
        print(e)
    return line[0]


help = '''
Using this command you can easily Rename any file at a time. Run this code using following step:
Step 1: Run 'MultipleFileRename.exe'
Step 2: Enter 'Folder location'  Just Copy & Past  -->  EX:  ' F:\Python\Python_Mind '
Step 3: Select Your Choice: 1. Single File Rename   |   2. Multiple File Rename  |   0. Exit Program
Step 4: Depends on Your Choice:
For Choice 1 :
1. Select the file name with serial number
2. Type New Name & Press Enter

For Choice 2 :
1.  A Notepad will open
     serial ----  :  ----- Old-----  :  ------ New -------
2. Change New Name  as you want to Rename your file  --> then save (ctrl +s) the Notepad.
3. Type Done after Changing  you file name in Notepad
4. Wait Until All the file get Renamed

Don't Forget To Share Your Experience...
Hope you like It. 
Thank You
'''


class Rename:
    def __init__(self):
        print("Welcome To 'Python Mind' Project \nYou Can Rename Single or Multiple File At A Time With This Program\n")
        self.programPath = self.FixedUrl(os.getcwd())
        self.path = input('Enter Your Folder Location:  -->')
        # self.path = 'F:\\PHOTOSHOP\\drawing'
        self.TXTFile = f'{self.programPath}\\Rename_File.txt'

    def FixedUrl(self, Path):
        FinalEdit = ''
        for i in range(len(Path)):
            if Path[i] == '\\':
                if Path[i + 1] == '\\':
                    pass
                else:
                    FinalEdit = FinalEdit + '\\'
            FinalEdit += Path[i]
        return FinalEdit

    def CheckFolder(self):
        Folder = os.listdir(self.path)
        print(f"Folder Location: {self.path}")
        print("In Selected Folder Those Files Are Founded")
        print('*********************************')

        for sl, i in enumerate(Folder):
            print(f'{sl}. {i}')
        return Folder

    def Single(self, Folder):
        print()
        file_SL = int(input("Input The 'File Number' You Want To Rename: "))
        file_name = Folder[file_SL]
        extension = file_name[len(file_name) - 5:].split('.')[1]
        file_New = input(f"Rename File: -->\n\t\t\t\t  Old File Name: {file_name}\n\t\t\t\t  New File Name: ")
        if extension not in file_New:
            file_New = f'{file_New}.{extension}'

        old = f"{self.path}\\{file_name}"
        new = f"{self.path}\\{file_New}"

        try:
            os.rename(old, new)
            print(f'''{file_SL}. File: {file_name} --> Changed To -->  {file_New}''')
            print(f"Rename Successfully... New File Name: {file_New}")
        except Exception as e:
            print(f"Error Occurred: {Folder[file_SL]} | Renamed Failed.. \nReport: {e}")
            pass
        time.sleep(1)

    def CreateTXT(self, Folder):
        file = open(self.TXTFile, 'w')
        file.write('Change New Name for Rename\n"Serial------- : -------Old-------" : "-------New-------",\n')
        file.write('Filename = {\n')
        count = 0
        for i in range(len(Folder)):
            text = f"{i} : {Folder[i]} : {Folder[i]}\n"
            # print(text)
            try:
                file.write(text)
                count += 1
            except Exception as e:

                print(f"Error Occurred: {Folder[i]} \nReport: {e}")
                pass
        file.write('}')
        file.close()
        print(f'''
=> {count} File Can Be Rename. 
=> Change 'New Name' From 'Rename_File.txt' As you Want To Rename The File
=> Type 'Done' When You Finish Editing And Saved 'Rename_File.txt\'''')
        time.sleep(3)
        os.startfile(self.TXTFile)

    def rename(self, Folder):
        fileOpen = open(self.TXTFile, 'r')
        lines = fileOpen.readlines()
        edited = 0
        startLine = None
        for line in range(len(lines)):
            if 'Filename = {' in lines[line]:
                startLine = True
                # print(line)

            elif '}' in lines[line]:
                startLine = False
                print(f"\n\n{edited} Files Renamed...")
                break

            elif startLine:
                RLine = lines[line].replace('\n', '')
                RLine = RLine.split(' : ')
                # print(RLine)
                if RLine[1] != RLine[2]:
                    Sl = int(RLine[0])
                    file_name = Folder[Sl]
                    newName = RLine[2]
                    extension = file_name[len(file_name) - 5:].split('.')[1]
                    if extension not in newName:
                        newName = f'{newName}.{extension}'

                    old = f"{self.path}\\{file_name}"
                    new = f"{self.path}\\{newName}"
                    # print(f' old: {old} \n new: {new}')
                    try:
                        os.rename(old, new)
                        print(f'''File: {RLine[0]}. {RLine[1]} --> Changed To -->  {newName}''')
                        print(f"Rename Successfully... New File Name: {newName}")
                        edited += 1
                    except Exception as e:
                        if '[WinError 183]' in e:
                            print(f"Error Occurred: Same Named Already Exist.. \n{e}")
                        else:
                            print(e)
                        pass
                    print()
                    time.sleep(1)

    def Multiple(self, Folder):
        print("\nPlease Wait... \nScanning All File List")

        try:
            self.CreateTXT(Folder)
        except Exception as e:
            print(e)

        while True:
            done = input("Are You Done With Your Renaming in Saved 'Rename_File.txt' File? ~ Type 'Done' ")
            if done.lower() == 'done':
                RenameNow = True
                print()
                break

        if RenameNow:
            print('Please Wait While Renaming Files....')
            self.rename(Folder)

    def run(self):
        print()
        print("Starting Program...")
        print()
        Stop = False
        while not Stop:
            print("""\n
****** What do you want to do? ****** 
1. Rename Single File
2. Rename Multiple File
3. For Help
0. Stop Program
            """)
            choice = int(input("Choice: "))
            print()
            if choice == 0:
                print("See You Later, Have A Nice Day...\nExiting Program.....")
                input("Enter any key to Exit")
                break
            Folder = self.CheckFolder()

            if choice == 3:
                print(help)

            if choice == 1:
                self.Single(Folder)

            if choice == 2:
                self.Multiple(Folder)


if __name__ == '__main__':
    Code = Rename()
    Code.run()
