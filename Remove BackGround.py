
import os
from tkinter import filedialog
import rembg
import threading
import time


class BgRemover:
    def __init__(self, path):
        self.count = 0
        self.path = path
        self.CurrentPath = os.listdir(path)
        self.saveAs = f'{path}/removedBg/'
        if 'removedBg' not in self.CurrentPath:
            os.mkdir(self.saveAs)
        else:
            pass

    def Remover(self, img):
        FileName = img.replace('.JPG', '')
        print(f'Image: {FileName}   |  Starting Background Removing...')
        with open(fr'{self.path}\{img}', 'rb') as inp:
            with open(fr"{self.saveAs}{FileName}.png", 'wb') as out:
                Input = inp.read()
                Output = rembg.remove(Input)
                out.write(Output)
        print(f'File {FileName}. Background Removed Successfully...')

    def DirectoryData(self):
        print(f'Selected Folder: {self.path} ')
        print('Folder Item: ')
        fileList = dict()
        for i, file in enumerate(self.CurrentPath):
            print(i + 1, file)
            if file.endswith('.jpg') or file.endswith('.JPG') or file.endswith('.png'):
                fileList[i] = file
        return fileList

    def main(self):
        ThreadLIst = []
        print('Staring Program')
        welcome = '''
Select Your Remover Mode:   _______ Image Remove Background
    1. Single 
    2. Multiple  
    3. All 
    4. Help
    5.Exit
        '''

        while 1:
            print(welcome)
            select = int(input('Select Mode Choice : '))
            if select == 5:
                print("Good Bye....")
                break
            if select == 1:
                files = self.DirectoryData()
                selection = int(input('Select You Image Serial :'))
                fileSelected = files[selection - 1]
                if fileSelected.endswith('.JPG'):
                    thread = threading.Thread(target=self.Remover, args=(fileSelected,))
                    thread.start()
                    self.count += 1
                thread.join()

                print(f"{self.count} Image's Background is removed ")
                self.count = 0

            elif select == 2:
                files = self.DirectoryData()
                selection = input('Select You Image Serial By Separating with space  :').split(' ')
                for i in selection:
                    Index = int(i) - 1
                    fileSelected = files.get(Index)
                    if fileSelected.endswith('.JPG'):
                        thread = threading.Thread(target=self.Remover, args=(fileSelected,))
                        ThreadLIst.append(thread)
                        thread.start()
                        self.count += 1

                for Thd in ThreadLIst:
                    Thd.join()

                print(f"{self.count} Image's Background is removed ")
                self.count = 0

            elif select == 3:
                files = self.DirectoryData()
                print(f"{len(files)} Image Found...")
                print('Please wait... Preparing for starting background removing...')
                for i in files.keys():
                    fileSelected = files[i]
                    if fileSelected.endswith('.JPG'):
                        thread = threading.Thread(target=self.Remover, args=(fileSelected,))
                        ThreadLIst.append(thread)
                        thread.start()
                        self.count += 1

                for Thd in ThreadLIst:
                    Thd.join()

                print(f"{self.count} Image's Background is removed ")
                self.count = 0


if '__main__' == __name__:
    welcome = '''
***** Welcome To Python Mind Background Remover Project. *****

Select Your Image Folder:  
    '''
    print(welcome)
    time.sleep(2)
    while True:
        path = filedialog.askdirectory()
        if path:
            run = BgRemover(path)
            run.main()
        else:
            print('Select Your Folder: ')
            time.sleep(2)


