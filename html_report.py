# vim: abstop=4 shiftwidth=4 softtabstop=4

import os
import sys
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

    def parse_xml(self, file_path):
        global type_error
        global type_verification
        global type_info

        if(os.path.exists(file_path)):
            xml_report = ET.parse(file_path)
            xml_root = xml_report.getroot()
            shutdown_msgs = xml_root.findall(self.msg_path)
            model_name = (file_path.split(os.sep)[1]).split(".")[0]
            
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

    def report_generate(self, storage_path):
        dir_list = os.listdir("current path")
        template_list = [template_path, temp_table_path, sum_path]
        template_map = {}

        for temp in template_list:
            if temp in dir_list:
                tmp_fd = open(temp, "r")
                template_content = tmp_fd.read()
                template_map[temp.split("."[1])] = template_content
            else:
                print("template files are not completed")
                #sys.exit(0)  
        scp_sum_num = sum(self.total.values()) 
        scp_err_num = sum(self.results.values())
        scp_passed_num = scp_sum_num - scp_err_num

#    def __init__(self, passed_num, error_num, rate_percent):
#        self.rexpresses = ["Passed Script Number", "Error Script Number", "Rate Percent Number"]
#        self.passed_num = passed_num 
#        self.error_num = error_num
#        self.rate_percent = rate_percent

    def load_table_template(self):
        fd_table_template = file(os.getcwd() + "html_templates" + os.sep + "temp_table.html", "r") 
        table_template = fd_table_template.read()
        fd_table_template.close()
        return table_template
    
    def load_summary_template(self):
        fd_summary_template = file(os.getcwd() + "html_templates" + os.sep + "summary.html", "r")
        summary_template = fd_summary_template.read()
        fd_summary_template.close()
        return summary_template

    def generate_html_report(self, table_template, summary_template):
        pass

#class html_parser(HTMLParser):
#    def __init__(self):
#        self.tag = ""
#        self.reading_flag = False
#        self.data = [] 
#        self.replace_text = ["Passed Script Number", "Error Script Number" , "Rate Percent Number"]
#        HTMLParser.__init__(self)

#    def handle_starttag(self, tag, data):
#        if "span" == tag:
#            if data in self.replace_data:
#                self.reading_flag = True
#                self.data.append(data)

#    def handle_endtag(self, tag):
#        if self.reading_flag:
#            self.reading_flag = False

#    def replace_summary_data(self, nums = {"Passed Script Number":0, "Error Script Number":0, "Rate Percent Number":0}): 
#        self.data = nums[data]
        
#    def generate_model_table(self, template_path = ""):
#        pass

           
if __name__ == "__main__":
    default_xmls_path = os.getcwd()
    xsl_sheet_path = os.getcwd() + "report.xsl"
    template_path = os.getcwd() + "report" + os.sep +"report_temp.xml"

    report_names = []
    for f in os.listdir(default_xmls_path):
        if "." in f and "xml" == (f.split(".")[1]).lower():
            report_names.append(f)
    
    reporter = html_reporter(reports_path = default_xmls_path, report_names = report_names)
    
    for f in report_names:
		reporter.parse_xml(default_xmls_path + f)

    total_num = 0 
    total_error = 0
    
    for mod in reporter.total:
        total_num += int(reporter.total[mod]) 
        total_error += int(reporter.result[mod])
    
#   parser.generate_xml(default_xmls_path + "report\\report.xml", template_path)
    
#FIXME: Because of parser.transmit method depends on libxml2 and libxslt,
#       but these tools are not installed,
#       so, please make sure these two packages exist in your environment
#
#   parser.transmit(xsl_sheet_path)

