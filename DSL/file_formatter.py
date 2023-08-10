#!/usr/bin/python3
#author: Ramees
import re
import os

def format_file(file_name):
    '''
    This funtion formats file as per the requirement. If follows the below algorithm.
    1.Remove below Block
        ###
        NetMRI
        N – 
        Network
        Insight
        ###
    2.Remove headers and columns
    3.Remove occurances of word 'Insight' from begining of lines that contain Validated|Both
    4.Search for lines that do not contain 'Validated' and then append the next line to the end.
    5.Run step 4 until there are no lines without 'Validated'
    '''
    #place holder for sed command to remove block {sed -n '/NetMRI/, /Insight/d'}

    regex1 = r"^NetMRI.*List|^Copyright.+|Vendor.+Product|NOTE.+|.+support.infoblox.com.+|^(Insight)(\n)|.+Advisor\ssupport.+|.*\/var.+"
    regex2 = r"^(Insight)([^\n]+)" #To ignore line that only contains 'Insight'

    regex3_1 = r"^NetMRI[\n]"
    #regex3_2 = r"^N{1}\s{1}–\s{1}[\n]"
    regex3_2 = r"^N{1}\s{1}–\s{1}[\n]|^No\s–\s[\n]|^[N]\s+–\s+Network.[\n]"
    regex3_3 = r"^Network\s[\n]"

    #regex4 = r"^(Networks)(\S.+(Validated|Best\sEffort))" #Match lines that starts with Networ and contain best effort or Validated
    regex4= r"^(Networks)(P[AS].+(Enterprise|Firewall|Switch-Router).+)"
    
    copying = True
    with open(file_name, 'rt') as inf, open('/import/tools/support/DSL/stripped.txt', 'wt') as outf:

        for line in inf:
            if copying:
                if line.startswith('(NetMRI'): #This removes column headers Lines between '(NetMRI,' and 'Control' ignored
                    copying = False
                elif (re.match(regex1, line)):
                    copying = False
                    '''
                    NetMRI 7.5.1 NIOS 8.6.1 Device Support List Infoblox Network Infrastructure Complete Device Support List
                    Copyright �2021, Infoblox, Inc. All rights reserved. Page 10
                    �Vendor Model Type OS/Firmware Capabilities Product
                    NOTE:�
                    NetMRI�for�Check�Point�models�Smart-1�3050,�5600,�and�23500:�To�enable�Advisor�support,�create�the�following�file�in�the�specified�directory:�/var/home/admin/Backup/useCheckPointAdvisor.
                    Network Insight: Advisor support is disabled by default, but you can contact Infoblox support  to enable it.
                    NOTE : OpenSSH disabled certain legacy vulnerable ciphers that some Cisco devices and versions relied on for CLI collection. To ensure successful CLI collection for such devices, download and install the hotfix referenced as 
                    NIOS-69328 in the Infoblox Knowledge Base article 10068 at https://support.infoblox.com .
                    Insight
                    '''    
                elif (re.match(regex2, line)):
                    outf.write(re.sub(regex2, r"\2", line)) #replace line that starts with Insight with the rest of the line
                
                elif (re.match(regex4, line)):
                    outf.write(re.sub(regex4, r" \1 \2", line)) #Fix space issue for Palo Alto lines
                    #match = re.sub(regex4, r" \1 \2", line)
                    #print(f"line = {line}")
                    #print(f"matched reg = {match}")

                elif (re.match(regex3_1, line)) or (re.match(regex3_2, line)) or (re.match(regex3_3, line)):
                    copying = False
                    continue
                
                else:
                    outf.write(line)
            elif line.startswith('Control'):
                copying = True

    inf.close()
    outf.close()
    return('/import/tools/support/DSL/stripped.txt')

def fix_invalid_lines(file_name,outfile):
    regex11 = r"^((?!(Validated|Best\sEffort)).)*$" # Matches lines that does not contain Validated or Best Effort In them

    with open(file_name, 'rt') as inf, open(outfile, 'wt') as outf:
        for line in inf:
            if not (re.match(regex11, line)): #Write if line contains Validated or Best Effort 
                outf.write(line)
            else:
                 outf.write(line.rstrip())

        outf.close()
        os.system('rm /import/tools/support/DSL/stripped.txt')

if __name__ == '__main__':

    regex = r"Infoblox_(NetMRI_\d.\d.\d)"

    filenames = ["Infoblox_NetMRI_7.5.1_NIOS_8.6.1_Device_Support_List.txt",
                 "Infoblox_NetMRI_7.5.0_NIOS_8.5.3_Device_Support_List.txt",
                 "Infoblox_NetMRI_7.5.2_NIOS_8.6.2_Device_Support_List.txt",
                 "Infoblox_NetMRI_7.5.3_NIOS_9.0_Device_Support_List.txt",
                 "Infoblox_NetMRI_7.5.4_NIOS_9.0_Device_Support_List.txt"]

    #filenames = ["Infoblox_NetMRI_7.5.2_NIOS_8.6.2_Device_Support_List.txt"]

    for file in filenames:
        outfile = re.match(regex, file).group(1) +".txt"
        formatted = format_file(file)
        fix_invalid_lines(formatted, outfile)
