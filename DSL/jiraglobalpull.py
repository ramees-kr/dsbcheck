#!/usr/bin/python3
#courtesy:Arun
#Authors:Sanith,Ramees
import pprint
import os.path
import requests
import sys
from requests.auth import HTTPBasicAuth
try:
  import yaml
except ModuleNotFoundError:
  os.system('python3 -m pip install yaml')
  import yaml
try:
  from neotermcolor import colored
except ModuleNotFoundError:
  os.system('python3 -m pip install neotermcolor')
  from neotermcolor import colored
try:
  from jira.client import JIRA
except ModuleNotFoundError:
  os.system('python3 -m pip install jira')
  from jira.client import JIRA
  
#from jira import JIRA
#from neotermcolor import colored

path = '~/.config/jira'
try:
  with open(os.path.expanduser(path), 'r') as config:
    auth = yaml.safe_load(config)
    #print(auth)
except FileNotFoundError:
  sys.exit('\nAdd your Email & JIRA User API Token & Execute "{}" \
            \n\nFor API Token: \
            \nNavigate to {}'\
            .format(colored('mkdir -p ~/.config;echo -e \'username: <emailid>\\ntoken: <api-token>\' > ~/.config/jira','yellow'),\
            colored('JIRA > Settings > Atlassian Account Settings > Security > API Token > Create and Manage API Token > Create API Token > Input Label > Copy','blue')))


def jirasearch():

    # Specify a server key. It is your domain
    # name link.
    jiraOptions = {'server': "https://infoblox.atlassian.net"}

        # Get a JIRA client instance, Pass
        # Authentication parameters
        # and Server name.
        # emailID = your emailID
        # token = token you receive after registration
    jira = JIRA(options = jiraOptions,
                basic_auth = (auth.get('username'),auth.get('token')))


    search_sysobj_id = input("Enter the SysObjectID: ")
    # Search all issues mentioned against a project name.
    
    if search_sysobj_id.replace(".","").isdigit():
        search_out = jira.search_issues(jql_str=f'project = NEWDEVICE AND text ~ {search_sysobj_id}')
    
        if (len(search_out) == 0):
            print("Match not found in JIRA")
        else:
            for singleIssue in search_out:
                print('{}: {}: {} : {}: {}'.format(singleIssue.key, singleIssue.fields.summary,
                                singleIssue.fields.reporter.displayName,
                                singleIssue.fields.status,
                                singleIssue.fields.resolution))
    
        return()
    else:
        print("You appear to have entered an Invalid SysObjectID")
