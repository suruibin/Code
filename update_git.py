# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:23:03 2019

@author: Suruibin
"""

import os


def share_github():
    os.chdir("/home/suruibin/Code/")
    
    os.system("cp /mnt/d/Code/Python/xsbdh/*.py /home/suruibin/Code/")
    os.system("cp /mnt/d/Code/Python/xsbdh/*.ui /home/suruibin/Code/")
    os.system("cp /mnt/d/Code/Python/xsbdh/*.txt /home/suruibin/Code/")

    os.system("/usr/bin/git add .")
    os.system("/usr/bin/git commit -m \"Update Code.\" -a >/tmp/msg.txt")
    os.system("/usr/bin/git push -q")

    
    os.chdir("/mnt/d/Software/TDX_SXBDH/T0002/signals/signals_user_4/")

if __name__ == "__main__":
    share_github()