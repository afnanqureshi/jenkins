'''
   This script generates a document that
    mentions the plugins installed in
    Jenkins.
    __author__ = "Mohd Afnan Qureshi"
    __maintainer__ = "Mohd Afnan Qureshi"
    __email__ = "md.afnan1995@gmail.com"
    __status__ = "Production"
'''

import requests
import json
import os
from urllib3.exceptions import InsecureRequestWarning

# Global variable declaration
token = os.getenv('token')
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + token
}
url = "https://jenkins.com/"
file_name = "JenkinsPlugins.md"


# Function to get plugin info
def get_data(url):
    name = []
    urls = []
    version = []
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    response = requests.get(url + "pluginManager/api/json?depth=1", headers=headers, verify=False)
    print(response.status_code)
    data = json.loads(response.text)
    data = data['plugins']
    for d in data:
        if 'url' in d:
            name.append(d['longName'])
            urls.append(d['url'])
            version.append(d['version'])
        else:
            name.append(d['longName'])
            urls.append('https://plugins.jenkins.io/')
            version.append(d['version'])

    return name, urls, version


# Function to create ReadMe document
def print_data(plugin_names, plugin_urls, plugin_versions, file_name):
    file = open(file_name, "a")
    file.write("# Jenkins : Plugins Installed\n\n| Plugins | Version | More Info |\n| ----- | ----- | ----- |\n")
    for i in range(len(plugin_names)):
        file.write("| ")
        file.write(plugin_names[i])
        file.write(" | ")
        file.write(plugin_versions[i])
        file.write(" | [Jenkins](")
        file.write(plugin_urls[i])
        file.write(") |\n")
    file.close()


# Function calls
plugin_names, plugin_urls, plugin_versions = get_data(url)
print_data(plugin_names, plugin_urls, plugin_versions, file_name)


