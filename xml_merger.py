from xml_parser import Luigi
from xml.etree import ElementTree

class Mario(object):
    def __init__(self):
        self.merger_tree = ElementTree.ElementTree()
        self.mergee_tree = ElementTree.ElementTree()
        self.merger_root = ElementTree.Element(None)
        self.mergee_root = ElementTree.Element(None)
        self.result_tree = ElementTree.ElementTree()

    def load_merger_file(self, merger_path):
        if(os.path.exists(merger_path)):
            #here I changed the original code:
            #because tempory variable make no sense, and new code is more readalbe
            self.merger_tree = ElementTree.parse(merger_path)
            #to make code more robust, add else segment
        else:
            print >> sys.stderr, "merger file does not exists"
            sys.exit(0)

    def load_mergee_file(self, mergee_path):
        if(os.path.exists(mergee_path)):
            #here I changed the original code:
            #because tempory variable make no sense, and new code is more readalbe
            self.mergee_tree = ElementTree.parse(mergee_path)
            #to make code more robust, add else segment
        else:
            print >> sys.stderr, "mergee file does not exists"
            sys.exit(0)
    
    def get_merger_root(self, merger_tree):
        self.merger_root = merger_tree.getroot()

    def get_mergee_root(self, mergee_tree):
        self.mergee_root = mergee_tree.getroot()

    def get_fail_script_node(self, mergee_path):
        Luigi_obj = Luigi()
        Luigi_obj.pick_fail_scp_put(mergee_path)
        #I changed the original code:
        #verify f_scp_name making no sense, just return what Mario need is better
        return Luigi_obj.f_scp_name

    def get_succ_script_node(self, merger_path):
        Luigi_obj = Luigi()
        Luigi_obj.pick_succ_scp_out(merger_path)
        #I changed the original code:
        #verify f_scp_name making no sense, just return what Mario need is better
        return Luigi_obj.s_scp_name
#FIXME:
#Luigi get the failed scripts and pass his attribute to Mario, 
#what about return the failed scripts array by Luigi and here I do an IO operation

    def merge_xml(self, merger_tree, mergee_tree, succ_scp_name, fail_scp_name):
        merger_root = merger_tree.getroot()
        mergee_root = mergee_tree.getroot()
        tmp_removed_rec = []
        patt = "/Group"

        i = 1
        while(i < 10):
#FIXME:
#here I hardcoded the range of while loop, that means we could not handle xml report which deeper than 10
#use a flexable range instead of constant range 

            pattern = patt * i
            parent_path = "scripts" + pattern
            find_path = parent_path + "/Script"
            flag_obj_list = mergee_root.findall("Scripts" + pattern + "/Script")

            if(0 != len(flag_obj_list)):
                parents = mergee_root.findall(parent_path)

                for parent in parents:
                    c = 0
                    while(c < len(parent._children)):
                        scp = parent._children[c]

                        if("Script" == scp.tag and "File" in scp.attrib.keys()):
                            replace_scp_name = scp.attrib["File"]

                            if(replace_scp_name in succ_scp_name and replace_scp_name in failed):
                                tmp_removed_rec.append(replace_scp_name)
                                parent.remove(scp)
                                if c != 0:
                                    c = c - 1
                                else:
                                    c = 0
                        c = c + 1
                    
                    for scp in merger_root.findall(find_path):
                        if("Script" == scp.tag):
                            inert_scp_name = scp.attrib["File"]

                            if(insert_scp_name in tmp_removed_rec):
                                parent.insert(-1, scp)
#FIXME:
#here I insert the node after the tail, that means append
#if neccessary, Mario should replace the node but not append
                ele_arr = mergee_root.findall("Results" + pattern + "/Script")

                for ele in ele_arr:
                    if("name" in ele.attrib.keys() and "message" in ele.attrib.keys()):
                        if(ele.attrib["name"] in tmp_removed_rec and 0 != ele.attrib["errors"]):
                            ele.attrib["errors"] = "0"
                            ele.attrib.pop("message")

                ele_arr = mergee_root.findall("Shutdown/Message")

                for ele in ele_arr:
                    if("Error" == ele.attrib["Type"]):
                        ele.attrib["Message"] = "0 script(s) failed"
                        ele.attrib["Type"] = "Verification"

                ele_arr = mergee_root.findall("Results" + pattern + "/Script")

                for ele in ele_arr:
                    if("name" in ele.attrib.keys()):
                        if(ele.attrib["name"] in tmp_removed_rec and "0" != ele.attrib["errors"]):
                            ele.attrib["errors"] = "0"
                            ele.attrib.pop("message")
        i = i + 1
    self.result_tree = mergee_tree
#DEBUG:
#   for tmp in tmp_removed_rec:
#       print >> sys.stdout, tmp

    def generate_xml_tree(self, result_tree, output_path):
        if(os.path.exists(output_path)):
            print >> sts.stderr, "oops: Mario found that the output file already exists"
            sys.exit(0)
        else:
            self.result_tree.write(output_path)
