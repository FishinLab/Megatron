import Tkinter
import os
import re
import sys
import commands
from Tkinter import *
from xml_merger import Mario
from xml_parser import Luigi
from html_report import html_reporter 

default_height = 480
default_width = 640

default_bar_height = 480
default_bar_width = 120

#fucntion: upload xml files and merge them
#parameters: @merger => <string> xml file path
#            @mergee => <string> xml file path
#            @result => <string> xml result path
def do_merge():
    #fd_setting = file(os.getcwd() + os.sep + "setting.conf", "r")
    fd_setting = file("".join([os.getcwd(), os.sep, "setting.conf"]), "r")
    fd_config = fd_setting.read()
    fd_setting.close()
    
    if(fd_config):
        ex_pathes = ["MERGER_PATH:.*", "MERGEE_PATH:.*", "RESULT_PATH:.*"]
        para_pathes = {}
        try:
            for i in range(3):
                ex_tmp = re.compile(ex_pathes[i])
                para_pathes[ex_pathes[i]] = (ex_tmp.findall(fd_config)[0]).strip(ex_pathes[i])
            merger, mergee, result = para_pathes.values()
#DEBUG: 
#           print >> sys.stdout, merger
#           print >> sys.stdout, mergee
#           print >> sys.stdout, result 
            m = Mario()
            m.load_merger_file(merger)
            m.load_mergee_file(mergee)
            succ_scp_name = m.get_succ_script_node(merger)
            fail_scp_name = m.get_fail_script_node(mergee)

            m.merge_xml(m.merger_tree, m.mergee_tree, succ_scp_name, fail_scp_name)
            m.generate_xml_tree(m.result_tree, result)
        except:
            print >> sys.stdout, "define parameters firstly"
#           return 
#DEBUG
    global default_width
    global default_height
    l = Luigi()
    l.pick_fail_scp_out(mergee)
    sum_fail_scp_info = "" 
    for fail_scp in l.f_scp_name:
        fail_scp += "\n"
        sum_fail_scp_info += fail_scp
    mess_info = Message(master = None, text = sum_fail_scp_info, width = default_width)
    mess_info.place(x = 0, y = 0, width = default_width, height = default_height)
    print >> sys.stdout, "clicked merge button"

def do_deploy():
#this button function is to deploy the html report with outlook to the boss
#because of the environment, this fucntion should be done with exists jar package
    fd_setting = file("".join([os.getcwd(), os.sep, "setting.conf"]), "r")
    fd_config = fd_setting.read()
    fd_setting.close()

    f_xmls_path = "" 
    f_deploy_servers = []
    f_deploy_pathes = []
    if(fd_config):
        try:
            ex_sum_models = re.compile("REPORTS_PATH:.*")
            ex_servers = re.compile("DEPLOY_SERVER:.*")
            ex_pathes = re.compile("FINAL_REPORT_PATH:.*")
            f_xmls_path = (ex_sum_models.findall(fd_config)[0]).strip("REPORTS_PATH:") 
            f_deploy_info = (ex_servers.findall(fd_config)[0]).strip("DEPLOY_SERVER:") 
            f_pathes = (ex_pathes.findall(fd_config)[0]).strip("FINAL_REPORT_PATH:") 
            f_deploy_servers = f_deploy_info.split(",")
            f_deploy_pathes = f_pathes.split(",") 
            if(len(f_deploy_servers) != len(f_deploy_pathes)): 
                print >> sys.stdout, "wrong number of parameters for deploy server and final report path"
                return
        except:
            print >> sys.stdout, "define parameters firstly"

    report_names = []
    for f in os.listdir(f_xmls_path):
        if "." in f and "xml" == (f.split(".")[1]).lower():
            report_names.append(f)
    
    reporter = html_reporter(reports_path = f_xmls_path, report_names = report_names)
    for f in report_names:
		reporter.parse_xml(f_xmls_path + f)

    for dp, ds in zip(f_deploy_pathes, f_deploy_servers):    
        print >> sys.stdout, dp
        try:
            reporter.generate_html_report(dp)
            #os.system("".join(["java -jar ../jars/SendMailtoAll_", ds, ".jar"]))
            if("" != commands.getoutput("".join(["java -jar ../jars/SendMailtoAll_", ds, ".jar"]))):
                print >> sys.stdout, "sending email, but jar failed"
                return 
        except:
            print >> sys.stdout, "when send report email to all, an exception happened"
            return 

    print >> sys.stdout, "clicked deploy button"
#flag = False
def do_setting():
#this button function is to set parameters such like xml, html report path, email client and so on
#using JSON file style to store users'  report parameters
    global default_height
    global default_width
    
    entry_para = Entry(maste = None, selectbackground = "red")
    entry_para.place(x = 5, y = 5, height = default_height - 10, width = default_width - 10)
    entry_para.bind(sequence = "<Enter>", func = press_enter())

#    entry_merger = Entry(master = None, textvariable = de_merger_v, selectbackground = "red")    
#    entry_merger.place(x = 5, y = 45, height = 35, width = default_width)

#    entry_mergee = Entry(master = None, textvariable = de_mergee_v, selectbackground = "red") 
#    entry_mergee.place(x = 5, y = 80, height = 35, width = default_width)

#    entry_reports= Entry(master = None, textvariable = de_reports_v, selectbackground = "red")
#    entry_reports.place(x = 5, y = 120, height = 35, width = default_width)
#    global flag 
#    if(flag):
#        de_merger_v.set(entry_merger.get())
#        print >> sys.stdout, de_merger_v.get() 
#        print >> sys.stdout, entry_mergee.get()
#        print >> sys.stdout, entry_reports.get()
#        flag = False 
#    else:
#        de_merger_v.set("MERGER_PATH")
#        de_mergee_v.set("MERGEE_PATH")
#        de_reports_v.set("REPORTS_PATH")
#        flag = True 

    print >> sys.stdout, "clicked setting button"

def run():
    global default_height
    global default_width

    Megatron_main = Frame(master = None) 
    Megatron_main.grid(row = 0, column = 0)

    can_main = Canvas(master = Megatron_main, height = default_height, width = default_width) 
    can_main.grid(row = 0, column = 0)

#   can_merge = Canvas(master = Megatron_main, bg = "yellow", height = 40, width = default_width)
#   can_merge.grid(row = 1, column = 0)
    
#   can_deploy= Canvas(master = Megatron_main, bg = "red", height = 40, width = default_width)
#   can_deploy.grid(row = 2, column = 0)

#   can_setting= Canvas(master = Megatron_main, bg = "blue", height = 40, width = default_width)
#   can_setting.grid(row = 3, column = 0)

    butt_merge = Button(master = Megatron_main, text = "merge", command = do_merge)
    butt_merge.grid(row = 1, column = 1)

    butt_deploy = Button(master = Megatron_main, text = "deploy", command = do_deploy)
    butt_deploy.grid(row = 2, column = 1)

    butt_setting = Button(master = Megatron_main, text = "setting", command = do_setting)
    butt_setting.grid(row = 3, column = 1)

    Megatron_main.mainloop()

if "__main__" == __name__:
    run()
