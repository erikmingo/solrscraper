import json
import urllib
import os

class XmlDoc:
    def __init__(self, url, namespaces, destination):
        self.url = url
        self.namespaces = namespaces
        self.destination = destination
    def returnUrl(self):
        return self.url
    def returnNamespaces(self):
        return self.namespaces
    def setDestination(self, place):
        self.destination = place
    def returnDestination(self):
        return self.destination

def construct_site_array(jsonfile):
    with open(jsonfile + ".json", 'r') as f:
        data = json.load(f)
    sites = []
    for thing in data['response']['docs']:
        sites.append(thing[u'url'])
    return sites

#this function returns an array of xml objects, with a url and a set of namespaces
def getUrlandNamespace():
    with open('urlsns.json', 'r') as f:
        data = json.load(f)
    xmlobjects = []
    # get the link to the xml and the namespaces
    for dictionary in data['response']['docs']:
        url = dictionary[u'url']
        for array in dictionary.values():
            if not isinstance(array, basestring):
                namespace = array
                xml = XmlDoc(url, namespace, None)
                xmlobjects.append(xml)
    return xmlobjects

def defineAnXML(xml):
    #load the xml as an object as a giant string
    with open(xml, 'r') as f:
        data = f.read()
    print data.split('xmlns')[1]

def downloadxml(jsonfile):
    sites = construct_site_array(jsonfile)
    i = 0
    for site in sites:
        i = i + 1
        urllib.urlretrieve(site,'xml/%s.xml' %(i))


#def sortXML(xmlobjects):
def sortXML():
    i = 0
    xmlObjects = getUrlandNamespace()
    for xmldoc in xmlObjects:
        placeholder = ""
        for namespace in sorted(xmldoc.returnNamespaces()):
            placeholder = placeholder + str(namespace.replace('/', '-'))
        xmldoc.setDestination(placeholder)
        try:
            if not os.path.exists(xmldoc.returnDestination()):
                os.mkdir(xmldoc.returnDestination())

            urllib.urlretrieve(xmldoc.returnUrl(), 'xml/%s/%s.xml' %(xmldoc.returnDestination(), i))
            i = i + 1
        except:
            pass


sortXML()

