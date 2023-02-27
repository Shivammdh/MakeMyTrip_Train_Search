import os
import sys
import time
from threading import Thread

class Hub(Thread):
    def run(self) -> None:
        os.chdir('D:\Selenium')
        os.system('java -jar selenium-server-4.8.1.jar hub')


class Node(Thread):
    def run(self) -> None:
        os.chdir('D:\Selenium')
        os.system('java -jar selenium-server-4.8.1.jar node')

class RunCode(Thread):
    def run(self) -> None:
        os.system(
            'python D:\Train-Search-POM\Tests\RunTestInGrid.py')




hubobj=Hub()
nodeobj=Node()
runcode=RunCode()
hubobj.start()
time.sleep(1)
nodeobj.start()
time.sleep(2)
runcode.start()

hubobj.join()
nodeobj.join()
runcode.join()

