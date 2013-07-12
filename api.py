# vim: abstop=4 shiftwidth=4 softtabstop=4
# email: fishinlab@sina.com

import os
import sys
from xml_merger import Mario
from xml_parser import Luigi
from html_report import html_reporter 
from html_report import html_parser

#function: upload xml file(merger file) to Mario
#parameters: @merger => <string> xml file path
def load_merger_file(m = Mario()):
    merger = "path/to/merger/xml"
    m.load_merger_file(merger) 

#function: upload xml file(mergee file) to Mario
#parameters: @mergee => <string> xml file path
def load_mergee_file(m = Mario()):
    mergee = "path/to/mergee/xml"
    m.load_mergee_file(mergee)

#function: call Luigi to get tree node which script's status is success 
#parameters: @merger => <string> xml file path
def get_succ_script_node(m = Mario()):
    merger = "path/to/merger/xml"
    return m.get_succ_script_node(merger)

#function: call Luigi to get tree node which script's status is failure 
#parameters: @mergee => <string> xml file path
def get_fail_script_node(m = Mario()):
    mergee = "path/to/mergee/xml"
    return m.get_fail_script_node(mergee)

#function: depends on uploaded files, and merge these files into one
#parameters: @m.merger_tree => <ElementTree> merger xml file etree 
#            @m.mergee_tree => <ElementTree> mergee xml file etree
#            @succ_scp_name => <array> which keeps successful scripts
#            @fail_scp_name => <array> which keeps failed scripts
def merge_xml(m = Mario()):
    return m.merge_xml(m.merger_tree, m.mergee_tree, succ_scp_name, fail_scp_name)

#function: when merging files finished, this method generated a final xml file
#parameters: @m.result_tree => <ElementTree> keeps the result report etree
#            @result => <string> result storage path
def generate_xml_tree(m = Mario()):
    return m.generate_xml_tree(m.result_tree, result)

#function: parse each uploaded xml file, and pick out which script's status is failure 
#parameters: @file_path => <string> xml report path
def pick_fail_scp_out(l = Luigi(), file_path = "path/to/xml"):
    return l.pick_fail_scp_out(file_path)

#function: parse each uploaded xml file, and pick out which script's status is success
#parameters: @file_path => <string> xml report path
def pick_succ_scp_out(l = Luigi(), file_path = "path/to/xml"):
    return l.pick_succ_scp_out(file_path)

