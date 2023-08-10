#!/usr/bin/python3
#author:Sanith
import os
import subprocess
import pprint

output = subprocess.getoutput("pip3 --version 2> /dev/null")
ver=(output.split(" ")[1][:2].replace("."," "))
if not int(float(ver)) >= 20:
    subprocess.run("pip3 install --upgrade pip",shell=True)
#subprocess.run("pip3 install --upgrade pip",shell=True)

try:
  from PyPDF2 import PdfReader
except ModuleNotFoundError:
  os.system('python3 -m pip install PyPDF2')
  from PyPDF2 import PdfReader

#from PyPDF2 import PdfReader
#from jira import JIRA

from jiraglobalpull import jirasearch
from file_formatter import format_file,fix_invalid_lines

pdfdir = "/import/tools/support/DSL"
textdir="/import/tools/support/DSL/TXT"
out="/import/tools/support/DSL/TXT/OUT"

if not os.path.exists(textdir):
    os.makedirs(textdir)
pdf_list=[fl for fl in os.listdir(pdfdir) if fl.endswith(".pdf")]    
for pdf_name in pdf_list:
    pdf_path=os.path.join(pdfdir,pdf_name)
    text_path=os.path.join(textdir,pdf_name.replace('.pdf','.txt'))
    if not os.path.exists(text_path):
        reader = PdfReader(pdf_path)

        #name=os.path.splitext("Infoblox_NetMRI_7.5.0_NIOS_8.5.3_Device_Support_List.pdf")[0]
        number_of_pages = len(reader.pages)
        #print(number_of_pages)
        page = reader.pages[number_of_pages-1]
        text = page.extract_text()
        textfile = open(text_path, "w")
        #textfile.close()
        for file_pages in range(0,number_of_pages):
            page = reader.pages[file_pages]
            text = page.extract_text()
            if "Vendor Model Type" in text:
                textfile.write(text + "\n")

text_list=[fl for fl in os.listdir(textdir) if fl.endswith(".txt")]
if not os.path.exists(out):
    os.makedirs(out)
for text_name in text_list:
    out_path=os.path.join(out,text_name.replace('.txt','out.txt'))
    
    #print(textdir+"/"+text_name)

    formatted = format_file(textdir+"/"+text_name)

    fix_invalid_lines(formatted,out_path)

key_word = input("\nEnter the Device Model : ")
#title=['Vendor','Model','Type','OS','SNMP','CC','Port','Product','Support','Advisor']
#print(title)
device_dict={}
for file_name in os.listdir(out):
    file_path=os.path.join(out,file_name)

    textout = open(file_path, "r")
    
    
    DSL= file_name.replace('_Device_Support_List','').replace('Infoblox_','').replace('out.txt','')
    
   
    for line in textout:
        
        if key_word.lower() in line.lower():
            if not DSL in device_dict.keys():
                    device_dict[DSL]=[]
            device_dict[DSL].append(line.strip())

#print(device_dict)
        

opt_list=[]
for k,v in device_dict.items():
    opt_list.extend(v)
    #print(device_dict.values())
    #print(opt_list)

opt_set=list(set(opt_list))
#print(opt_set)
if len(opt_set)!=0:
 
    opt_str=["{}. {}\n".format(i+1,ln) for i,ln in enumerate(opt_set)]
    #print(type(opt_str))
    #print(len(opt_str))
    if (len(opt_str))!=1:
        opt_str= ''.join(opt_str) + "\nPlease type the number corresponding to the exact Vendor,model and version  : \n"

        
        opt=int(input(opt_str))
        opt_sel=opt_set[opt-1]
        print(opt_sel)
        print ("\nDevice is Officially supported in \n")
        for k,v in device_dict.items():
            
            if opt_sel in v:
                    
                print(k)
    else:
        opt_sel=opt_set[0]
        print(opt_sel)
        print ("\nDevice is Officially supported in \n")
        for k,v in device_dict.items():
            
            if opt_sel in v:
                    
                
                print(k)
else:
    print("\nThe Device is not officially supported till the latest version!!!!")
    print("\n>>>  Checking NewDevice Ticket ++++++ \n")
    jirasearch()
    
    



        #print(device_dict[k])'''

