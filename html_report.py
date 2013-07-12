# vim: abstop=4 shiftwidth=4 softtabstop=4
# email: fishinlab@sina.com

import os
import sys
import re
from copy import deepcopy
from xml import etree
from xml.etree import ElementTree as ET
from xml.etree.ElementTree import Element as E
from HTMLParser import HTMLParser

try:
    import libxml2, libxslt
except:
    print("packages not completed, do not use python xml transmittion tool")

type_verification = "Verification"
type_error = "Error"
type_info = "Info"

class html_reporter(object):

    def __init__(self, reports_path = os.getcwd(), report_names = []):
        self.reports_path = reports_path
        self.report_names = report_names
        self.total = {}
        self.results = {}
        self.msg_path = "Shutdown/Message"
        self.re_expresses = ["Passed Script Number", "Error Script Number", "Rate Percent Number"] 

    def parse_xml(self, file_path):
        global type_error
        global type_verification
        global type_info

        if(os.path.exists(file_path)):
            xml_report = ET.parse(file_path)
            xml_root = xml_report.getroot()
            shutdown_msgs = xml_root.findall(self.msg_path)
            model_name = (file_path.split(os.sep)[-1]).split(".")[0]
#FIXME:
# i want to get the model name acording to file name,
# now here is a bug that, parse_file method must accept absolute file path
            
            for msg in shutdown_msgs:
                if( type_verification == msg.attrib["Type"]):
                    to = int(msg.attrib["Message"].split(" ")[0]) 
                    if model_name in self.total:
			            self.total[model_name] += to
			            self.results[model_name] = 0
                    else:
                        self.total[model_name] = to

                elif( type_error == msg.attrib["Type"]):
                    res = int(msg.attrib["Message"].split(" ")[0]) 
                    self.results[model_name] = res
                    self.total[model_name] += res
                
                elif( type_info == msg.attrib["Type"]):
                    pass
                
                else:
                    print("Errors found in XML report")
#DEBUG
#		for mo in self.total:
#			print(mo)
#			print(self.total[mo])
#		for res in self.results:
#			print(res)
#			print(self.results[res])
    def generate_xml(self, report_path, template_path):
        et = ET.ElementTree()
        et._root = E("report", {})

        for res in self.results: 
            e_attr = {"name":str(res), "total":str(self.total[res]), "errors":str(self.results[res])}
            e_insert = E("module", e_attr)
            et._root.insert(-1, e_insert)
        
        et.write(report_path)
        fd = open(report_path, "r")
        fd_c = fd.read()
        fd.close()
        xml_beginning = "<?xml version='1.0' encoding='UTF-8'?>\n"
        fd = open(report_path, "w")
        fd.write(xml_beginning + fd_c)
        fd.close()

    def transmit(self, xsl_path):
        xml = libxml2.parseFile(report_path)
        xsl_style = libxml2.parseFile(xsl_path)
        xsl = libxslt.parseStylesheetDoc(xml_style)
        week_report = xsl.applyStyleSheet(xml)
        xsl.saveResultToFilename(os.getcwd(), week_report, 0)

    def generate_html_report(self, final_report_path):
        succ_num = sum(self.total.values()) - sum(self.results.values())
        failed_num = sum(self.total.values()) - succ_num
        tmp_str = str(float(succ_num) / (sum(self.total.values())))
        tmp_str = tmp_str.split(".")[1]
        #succ_rate = tmp_str[0:2] + "." + tmp_str[2:4] + "%" 
        succ_rate = "".join([tmp_str[0:2], ".", tmp_str[2:4], "%"])
#replace the flag with, success script number, failure script number and success rate  
        #fd_sum_temp = file(os.getcwd() + os.sep + "html_templates" + os.sep +"summary.html", "r")
        fd_sum_temp = file("".join([os.getcwd(), os.sep, "html_templates", os.sep, "summary.html"]), "r")
        fd_sum_content = fd_sum_temp.read()
        fd_sum_temp.close()

        ex_succ_num = re.compile(self.re_expresses[0]) 
        fd_sum_content = fd_sum_content.replace(ex_succ_num.findall(fd_sum_content)[0], str(succ_num))
        #fd_sum_content.replace("Passed Script Number", str(succ_num))

        ex_fail_num = re.compile(self.re_expresses[1])
        fd_sum_content = fd_sum_content.replace(ex_fail_num.findall(fd_sum_content)[0], str(failed_num))
        #fd_sum_content.replace("Error Script Number", str(failed_num))

        ex_rate_num = re.compile(self.re_expresses[2])
        fd_sum_content = fd_sum_content.replace(ex_rate_num.findall(fd_sum_content)[0], succ_rate)    
        #fd_sum_content.replace("Rate Percent Number", str(succ_rate))
#DEBUG 
#        print >> sys.stdout, fd_sum_content
#append summary html template to the whole html report
        #temp_fd = file(os.getcwd() + os.sep + "html_templates" + os.sep +"temp_header.html", "r")
        temp_fd = file("".join([os.getcwd(), os.sep, "html_templates", os.sep, "temp_header.html"]), "r")
        final_html_report = ""
        final_html_report += temp_fd.read()
        temp_fd.close()
        final_html_report += fd_sum_content

#replace the flag with each model name and specific number
        ex_mod_name = re.compile("MODEL NAME")
        ex_total_num = re.compile("TOTAL NUMBER")
        ex_error_num = re.compile("ERROR NUMBER")

        #fd_temp = file(os.getcwd() + os.sep + "html_templates" + os.sep +"temp_table.html", "r")
        fd_temp = file("".join([os.getcwd(), os.sep, "html_templates", os.sep, "temp_table.html"]), "r")
        temp_table_con = fd_temp.read()
        fd_temp.close()

        for mod in self.total:
            cop_temp_table_con = deepcopy(temp_table_con)
            cop_temp_table_con = cop_temp_table_con.replace(ex_mod_name.findall(temp_table_con)[0], mod)
            cop_temp_table_con = cop_temp_table_con.replace(ex_total_num.findall(temp_table_con)[0], str(self.total[mod]))
            cop_temp_table_con = cop_temp_table_con.replace(ex_error_num.findall(temp_table_con)[0], str(self.results[mod]))
            #cop_temp_table_con = cop_temp_table_con.replace("MODEL NAME", mod)
            #cop_temp_table_con = cop_temp_table_con.replace("TOTAL NUMBER", str(self.total[mod]))
            #cop_temp_table_con = cop_temp_table_con.replace("ERROR NUMBER", str(self.results[mod]))

            final_html_report += cop_temp_table_con             
#DEBUG
#        print >> sys.stdout, self.results
#        print >> sys.stdout, self.total
#depends on which server to generate this file path
        #temp_fd = file(os.getcwd() + os.sep + "html_templates" + os.sep + "temp_tailer.html", "r")
        temp_fd = file("".join([os.getcwd(), os.sep, "html_templates", os.sep, "temp_tailer.html"]), "r")
        final_html_report += temp_fd.read()
        temp_fd.close()
        if(final_report_path):
            final_report = file(final_report_path, "w")
            final_report.write(final_html_report)
        else:
            final_report = file(os.getcwd() + os.sep + "final_report.html", "w")
            final_report.write(final_html_report)
#FIXME:
#in function generate_html_report: I use regular express to get the flag to replace with what I want to write in 
#compiled regular express is more effective that using string to replace, and the this function time duration is O(n)
#how to fix this defect with html parser? I think if that works, function time duration will be O(lgn)

if __name__ == "__main__":
    default_xmls_path = os.getcwd()
    xsl_sheet_path = os.getcwd() + "report.xsl"
    #template_path = os.getcwd() + "report" + os.sep +"report_temp.xml"
    template_path = "".join([os.getcwd(), "report", os.sep, "report_temp.xml"])

    report_names = []
    for f in os.listdir(default_xmls_path):
        if "." in f and "xml" == (f.split(".")[1]).lower():
            report_names.append(f)
    
    reporter = html_reporter(reports_path = default_xmls_path, report_names = report_names)
    
    for f in report_names:
		reporter.parse_xml(default_xmls_path + f)

    reporter.generate_html_report()
#   parser.generate_xml(default_xmls_path + "report\\report.xml", template_path)
    
#FIXME: Because of parser.transmit method depends on libxml2 and libxslt,
#       but these tools are not installed,
#       so, please make sure these two packages exist in your environment
#
#   parser.transmit(xsl_sheet_path)

