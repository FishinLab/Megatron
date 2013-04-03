import Tkinter
import os
import sys
from Tkinter import *
from xml_merger import Mario
from xml_parser import Luigi
from html_report import html_reporter 
from html_report import html_parser

g_height = 50
g_width = 50
        
class Megatron(Frame):
    def __init__(self, master = None):
        self.height = 160
        self.width = 240 
        Frame.__init__(self, master, height = self.height, width = self.width, bd = 10)
        self.grid()
        self.click_merge()
        self.click_deploy()
        self.show_script_status()
        self.get_buffer()

    def click_merge(self):
        merge_button = Button(text = "merge", command = do_merge)
        merge_button.grid()

    def click_deploy(self):
        deploy_button = Button(text = "deploy", command = do_deploy)
        deploy_button.grid()

    def show_script_status(self):
        pass
    
    def get_buffer(self):
        pass
    
def do_merge():
    print >> sys.stdout, "merging"

def do_deploy():
    print >> sys.stdout, "deploying"

class meg_canvas(Canvas):
    def __init__(self, master = None):
        Canvas.__init__(self, master)

class test_list(Listbox):
    def __init__(self, master = None):
        Listbox.__init__(self, master)

class test_img(Canvas):
    def __init__(self, master):
meg = Megatron()
can = meg_canvas(master = meg)
can.grid(ipadx = 0, ipady = 0, padx = 100, pady = 100)

#li = test_list(can)
#li.grid(ipadx = 0, ipady = 0, padx = 20, pady = 20)
#DEBUG
#i = 0
#while(i < 1000):
#    print >> sys.stdout, can.winfo_x()
#print >> sys.stdout, can.winfo_x()
#print >> sys.stdout, can.winfo_y()

meg.master.title("Megatron")
meg.mainloop()
