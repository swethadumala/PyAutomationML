from textwrap import indent
from pyautomationml_test import PyAutomationML as aml_tree
from pyautomationml_test import AmlElement 
from pprint import pprint
import json
import time

start_time = time.time()
with open('config.json') as json_file:
    structure_dict = json.load(json_file)

#nesting = None
#nesting = "local"
nesting = "global"

abbreviate=True

globally_managed = {"Attribute", "InternalElement", "ExternalInterface"}

key_dict = {
}


#Normal JSON Key-Value-Structure
def dict_filler(element: AmlElement, element_list=None): #(object that is analyzed)
    global structure_dict
    raw_dict= {}
    
    for key in element.keys():
        if key in structure_dict.keys() and abbreviate==True: # not all keys have an abbreviation
            key = structure_dict[key]["abbreviation"]
        elif key in structure_dict.keys():
            key = structure_dict[key]["fullname"]
        raw_dict[key] = element.getattrib(key)
        if key not in structure_dict[element.gettag()]["tags"]:
            structure_dict[element.gettag()]["tags"].append(key)

    # If element has pure text attributes 
    child_list = element.iterchildren()
    for child in child_list:
        if child.getattrib("Name") is None or child.getattrib("Name") == "None":
            raw_dict[child.gettag()] = child.text
            if child.gettag() not in structure_dict[element.gettag()]["attributes"]:
                structure_dict[element.gettag()]["attributes"].append(child.gettag())

    return raw_dict

def dict_filler_local_kv(element: AmlElement):
    global structure_dict
    raw_dict= {}
    keylist = []
    valuelist = []

    for key in element.keys():
        if key in structure_dict.keys() and abbreviate==True: # not all keys have an abbreviation
            key = structure_dict[key]["abbreviation"]
        elif key in structure_dict.keys():
            key = structure_dict[key]["fullname"]
        keylist.append(key)
        valuelist.append(element.getattrib(key))

    child_list = element.iterchildren()
    for child in child_list:
        if child.gettag() not in structure_dict[element.gettag()]["children"]:
            keylist.append(child.gettag())
            valuelist.append(child.text)

    raw_dict["keys"] = tuple(keylist)
    raw_dict["values"] = tuple(valuelist)

    return raw_dict

def dict_filler_global(element: AmlElement):
    global structure_dict
    global key_dict
    valuelist = []
    
    if element.gettag() not in key_dict: 
        key_dict[element.gettag()] = []

    for key in element.keys():
        if key in structure_dict.keys() and abbreviate==True: # not all keys have an abbreviation
            key = structure_dict[key]["abbreviation"]
        elif key in structure_dict.keys():
            key = structure_dict[key]["fullname"]
        
        if key not in key_dict[element.gettag()]:
            key_dict[element.gettag()].append(key)

        while (key_dict[element.gettag()].index(key) >= len(valuelist)):
                valuelist.append("")
        valuelist[key_dict[element.gettag()].index(key)] = (element.getattrib(key))
        
    child_list = element.iterchildren()
    for child in child_list:   
        if child.gettag() not in structure_dict[element.gettag()]["children"]:
            if child.gettag() not in key_dict[element.gettag()]:
                key_dict[element.gettag()].append(child.gettag())

            while (key_dict[element.gettag()].index(child.gettag()) >= len(valuelist)):
                valuelist.append("")
            valuelist[key_dict[element.gettag()].index(child.gettag())] = child.text
    return valuelist

def dict_filler_sorted_global(element: AmlElement):
    global structure_dict
    global key_dict
    valuelist = []

    if element.gettag() not in key_dict: 
        key_dict[element.gettag()] = structure_dict[element.gettag()]["sorted"]

    for key in element.keys():
        if key in structure_dict.keys() and abbreviate==True: # not all keys have an abbreviation
            key = structure_dict[key]["abbreviation"]
        elif key in structure_dict.keys():
            key = structure_dict[key]["fullname"]
    
        while (key_dict[element.gettag()].index(key) >= len(valuelist)):
                valuelist.append("")
        valuelist[key_dict[element.gettag()].index(key)] = (element.getattrib(key))

    child_list = element.iterchildren()
    for child in child_list:   
        if child.gettag() not in structure_dict[element.gettag()]["children"]:
            while (key_dict[element.gettag()].index(child.gettag()) >= len(valuelist)):
                valuelist.append("")
            valuelist[key_dict[element.gettag()].index(child.gettag())] = child.text

    return valuelist


def element_builder(element: AmlElement, nesting=None):
    global structure_dict
    global key_dict

    def hasChildren(element):
        child_list = element.iterchildren()
        for child in child_list:
            if child.gettag() in structure_dict[element.gettag()]["children"]: 
                return True
        return False

    # Get Tags and attributes from current element
    # Case dependent decision, how data is stored
    if nesting == "global":
        if element.gettag() in globally_managed:
            element_dict = dict_filler_sorted_global(element) 
        else:
            element_dict = dict_filler_global(element) 
    elif nesting == "local" :
        element_dict = dict_filler_local_kv(element)
    else:
        element_dict = dict_filler(element) 


    if structure_dict[element.gettag()]["children"]:
        for child in structure_dict[element.gettag()]["children"]:
            childlist= element.findall(child)
            child_obj: AmlElement
            if childlist:
                element_list = [] # temporary storage for objects with multiple elements
                for child_obj in childlist:
                    child_dict = element_builder(child_obj, nesting)
                    element_list.append(child_dict)
                if abbreviate:
                    if structure_dict[child_obj.gettag()]["multi"] == True:
                        element_dict[structure_dict[child_obj.gettag()]["abbreviation"]] = element_list 
                    else:
                        element_dict[structure_dict[child_obj.gettag()]["abbreviation"]] = element_list
                else:
                    if structure_dict[child_obj.gettag()]["multi"] == True:
                        element_dict[structure_dict[child_obj.gettag()]["fullname"]] = element_list 
                    else:
                        print(element_dict[structure_dict[child_obj.gettag()]["fullname"]])
                        print(child_dict)
                        element_dict[structure_dict[child_obj.gettag()]["fullname"]] = element_list
    return element_dict

def AML_to_dict():
    global key_dict
    global structure_dict
    doc = aml_tree("./Examples/Testbed.aml")
    return_dict = element_builder(doc.root, nesting)  
    return_dict["AttributeKeys"] = key_dict  

    with open("config.json", "w", encoding="utf-8") as outfile:
        json.dump(structure_dict, outfile, ensure_ascii=False)

    return return_dict


def dict_to_json(dict: dict, name: str):
    with open(name, "w", encoding="utf-8") as outfile:
        json.dump(dict, outfile, ensure_ascii=False, indent=1)

    
if __name__ == '__main__':
    dict_to_json(AML_to_dict(), "./output/Testbed_global.json")
    print("--- %s seconds ---" % (time.time() - start_time))