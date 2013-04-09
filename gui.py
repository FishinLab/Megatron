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
        Frame.__init__(self, master, height = self.height, width = self.width)
        self.grid(row = 0, column = 0)
        self.click_merge()
        self.click_deploy()
        self.click_settings()
        self.show_script_status()
        self.get_buffer()
        self.init_server_canvas()
        self.init_path_canvas()

    def click_merge(self):
        merge_button = Button(text = "merge", command = do_merge)
        #merge_button.place(x = self.height, y = self.width, height = 40, width = 80)
        merge_button.grid(row = 1, column = 1)

    def click_deploy(self):
        deploy_button = Button(text = "deploy", command = do_deploy)
        deploy_button.grid(row = 2, column = 1)

    def click_settings(self):
        setting_button = Button(text = "settings", command = do_init_canvas) 
        setting_button.grid(row = 3, column = 1)

    def init_server_canvas(self):
        can_server = Canvas()
        can_server.place(relx = 0.8, height = 10)
        can_server.create_text(55, 10, text = "server name: ")

    def init_path_canvas(self):
        can_path = Canvas()
        can_path.place(rely = 0.9, height = 10)
        can_path.create_text(55, 10, text = "xml path: ")

    def show_script_status(self):
        pass
    
    def get_buffer(self):
        pass

    
#class setting_frame(Frame):
#    def __init__(self, master = None):
#        self.height = 160
#        self.width = 240
#        Frame.__init__(self, master, height = self.height, width = self.width, bd = 10)
#        self.grid()

#    def load_init_file(self):
#        fd_init = file(os.getcwd() + "settings.ini", "w")
#        print >> fd_init, "here is a test"
#        fd_init.close()

#    def do_destroy(self):
#        self.destroy()

def do_merge():
    print >> sys.stdout, "merging"

def do_deploy():
    print >> sys.stdout, "deploying"

def do_init_canvas():
    print >> sys.stdout, "setting"

#flag = True
#def init_canvas(flag):
#    if(flag):
#        can_setting.grid()
#    else:
#        can_setting.destroy()

class meg_canvas(Canvas):
    def __init__(self, master = None):
        Canvas.__init__(self, master)

class test_list(Listbox):
    def __init__(self, master = None):
        Listbox.__init__(self, master)

meg = Megatron()
#can = meg_canvas(master = meg)
#can.grid(ipadx = 0, ipady = 0, padx = 100, pady = 100)

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
