# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:23:03 2019

@author: Suruibin
"""

import os


def share_github():
    os.chdir("/home/suruibin/Code/")
    
    os.system("cp /mnt/d/Code/Python/xsbdh/*.7z /home/suruibin/Code/")


    os.system("/usr/bin/git add .")
    os.system("/usr/bin/git commit -m \"Update Code.\" -a >/tmp/msg.txt")
    os.system("/usr/bin/git push -q")

    print("已同步!")

if __name__ == "__main__":
    share_github()