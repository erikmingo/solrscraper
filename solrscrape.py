import json
import urllib

def construct_site_array(jsonfile):
    with open(jsonfile + ".json", 'r') as f:
        data = json.load(f)
    sites = []
    for thing in data['response']['docs']:
        sites.append(thing[u'url'])
    return sites

def getAllNamespaces():
    with open('namespaces.json', 'r') as f:
        data = json.load(f)
    namespaces = []
    for dictionary in data['response']['docs']:
        for array in dictionary.values():
            for ns in array:
                if ns not in namespaces:
                    namespaces.append(ns)
    with open('namespaces.txt', 'w') as f:
        for thing in namespaces:
            f.write(thing)
            f.write("\n")


def downloadxml(jsonfile):
    sites = construct_site_array(jsonfile)
    i = 0
    for site in sites:
        i = i + 1
        urllib.urlretrieve(site,'xml/%s/%s.xml' %(jsonfile, i))



getAllNamespaces()
#downloadxml('kml')
#downloadxml('atoms')
#downloadxml('opensearch')




