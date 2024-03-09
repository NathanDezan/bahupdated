from src.utils.ParserXML import XMLParser
import urllib, urllib.request

class Arxiv():
    def __init__(self, config):
        self.config = config
        self.url = self.config['arxiv']['url']
        self.query = self.config['arxiv']['query']
        self.max_results = self.config['arxiv']['max_results']

    def maker_url(self):
        return f'{self.url}?search_query={self.query}&start=0&max_results={self.max_results}'
    
    def search(self):
        try:
            data = urllib.request.urlopen(self.maker_url())

            return data.read().decode('utf-8')
        except Exception as e:
            return None

    def get_papers(self):
        try:
            response = self.search()
            xml_parser = XMLParser(response).extract_xml_data()

            return xml_parser
        except Exception as e:
            return None