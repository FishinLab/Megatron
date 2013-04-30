import sys
import os
from xml.dom import minidom

class Luigi(object):

    def __init__(self):
        self.s_scp_name = []
        self.s_scp_time = []
        self.s_scp_error_num = []

        self.f_scp_name = []
        self.f_scp_time = []
        self.f_scp_error_num = []
        self.f_scp_error_msg = []

    def pick_fail_scp_out(self, file_path):
        if(os.path.exists(file_path)):
            rpt_obj = minidom.parse(file_path)

            try:
                ele_arr = rpt_obj.getElementsByTagName("Script")
                if(ele_arr is not None):
                    for ele in ele_arr:
                        if(ele.getAttribute("name") != "" and ele.getAttribute("errors") != "0"):
                            #here I change the original code:
                            #because we do not need generate a tempory variable like before
                            self.f_scp_name.append(ele.getAttribute("name"))
                            self.f_scp_time.append(ele.getAttribute("time"))
                            self.f_scp_error_msg.append(ele.getAttribute("message"))
                            self.f_scp_error_num.append(1)
#FIXME:
#when we initialize a new object of Luigi, try to use map instead of array
            except:
                print >> sys.stderr , "oops, when Luigi try to get failed scripts, he got failed"
                sys.exit(0)

    def pick_succ_scp_out(self, file_path):
        if(os.path.exists(file_path)):
            rpt_obj = minidom.parse(file_path)
            try:
                ele_arr = rpt_obj.getElementByTagName("Script")
                if(ele_arr is not None):
                    for ele in ele_arr:
                        if(ele.getAttribute("name")  != "" and ele.getAttribute("errors") == "0"):
                            #here I change the original code:
                            #because we do not need generate a tempory variable like before
                            self.s_scp_name.append(str(ele.getAttribute("name")))
                            self.s_scp_time.append(ele.getAttribute("time"))
                            self.s_scp_error_num.append(0)
#FIXME:
#use map instead of array, except self.s_scp_name
            except:
                print >> sys.stderr, "oops: when Luigi try to get success scripts, he got failed"
                sys.exit(0)
