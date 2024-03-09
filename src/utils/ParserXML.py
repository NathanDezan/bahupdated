import xml.etree.ElementTree as ET

class XMLParser:
  def __init__(self, xml_data):
    self.xml_data = xml_data
    self.root = ET.fromstring(xml_data)

  def create_template(self):
    template = {
        'id': '',
        'pdf': '',
        'published': '',
        'title': '',
        'summary': '',
        'authors': []
    }

    return template

  def extract_xml_data(self):
    try:
      list_template = []

      for entry in self.root.findall('{http://www.w3.org/2005/Atom}entry'):
        template = self.create_template()

        for child in entry:
          if child.tag == '{http://www.w3.org/2005/Atom}id':
            template['id'] = child.text
          if child.tag == '{http://www.w3.org/2005/Atom}link':
            if child.attrib.get('title') == 'pdf':
              template['pdf'] = child.attrib.get('href')
          if child.tag == '{http://www.w3.org/2005/Atom}published':
            template['published'] = child.text
          if child.tag == '{http://www.w3.org/2005/Atom}title':
            template['title'] = child.text
          if child.tag == '{http://www.w3.org/2005/Atom}summary':
            template['summary'] = child.text
          if child.tag == '{http://www.w3.org/2005/Atom}author':
            for author_child in child:
              if author_child.tag == '{http://www.w3.org/2005/Atom}name':
                template['authors'].append(author_child.text)
        list_template.append(template)
        
      return list_template
    except Exception as e:
        return None