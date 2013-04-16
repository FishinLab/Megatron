import Tkinter
import os
import sys
from Tkinter import *
from xml_merger import Mario
from xml_parser import Luigi
from html_report import html_reporter 

default_height = 480
default_width = 640

default_bar_height = 480
default_bar_width = 120

def do_merge():
#this button function is to read parameters from setting.conf file, and do merge job
    print >> sys.stdout, "clicked merge button"

def do_deploy():
#this button function is to deploy the html report with outlook to the boss
#because of the environment, this fucntion should be done with exists jar package
    print >> sys.stdout, "clicked deploy button"

def do_setting():
#this button function is to set parameters such like xml, html report path, email client and so on
#using JSON file style to store users'  report parameters
    fd_setting = file(getcwd() + "setting.conf", "w")
    print >> fd_setting, "here is a setting test"

def run():
    global default_height
    global default_width
    #global default_bar_height
    #global default_bar_width

    Megatron_main = Frame(master = None) 
    Megatron_main.grid(row = 0, column = 0)
    #Megatron_bar = Frame(master = Megatron_main)
    #Megatron_info = Frame(master = None)
    #Megatron_info.grid(row = 1, column = 0)

    can_main = Canvas(master = Megatron_main, height = default_height, width = default_width, bg = "black") 
    can_main.grid(row = 0, column = 0)

    can_merge = Canvas(master = Megatron_main, bg = "yellow", height = 40, width = default_width)
    can_merge.grid(row = 1, column = 0)

    can_deploy= Canvas(master = Megatron_main, bg = "red", height = 40, width = default_width)
    can_deploy.grid(row = 2, column = 0)

    can_setting= Canvas(master = Megatron_main, bg = "blue", height = 40, width = default_width)
    can_setting.grid(row = 3, column = 0)
    #can_info = Canvas(master = Megatron_info, bg = "red")
    #can_info.grid(row = 1, column = 0)

    #can_bar = Canvas(master = Megatron_bar, height = default_bar_height, width = default_bar_width)
    #can_bar.grid()

    butt_merge = Button(master = Megatron_main, text = "merge", command = do_merge)
    butt_merge.grid(row = 1, column = 1)

    butt_deploy = Button(master = Megatron_main, text = "deploy", command = do_deploy)
    butt_deploy.grid(row = 2, column = 1)

    butt_setting = Button(master = Megatron_main, text = "setting", command = do_setting)
    butt_setting.grid(row = 3, column = 1)

    Megatron_main.mainloop()

if "__main__" == __name__:
    run()
"""
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
"""
