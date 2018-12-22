from xml.sax.handler import ContentHandler
from xml.sax import make_parser

class StaffHandler(ContentHandler):
    def startElement(self, name, attrs):#contenthandler accepts name and attr
        if (name == "food"):
            self.name = attrs.get("id")
    def endElement(self, name):
       if (name == "food"):
            print ("%-8s " %(self.name))
food = StaffHandler()
saxparser = make_parser() #creating a parser
saxparser.setContentHandler(food) #setting the content handler
datasource = open("sample.xml", 'r')
saxparser.parse(datasource)
datasource.close()