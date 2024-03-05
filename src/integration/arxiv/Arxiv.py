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
        print(self.maker_url())
        data = urllib.request.urlopen(self.maker_url())
        print(data.read().decode('utf-8'))
        # if response.status_code == 200:
        #     return response.json()
        # else:
        #     return None

    def get_papers(self):
        papers = []
        response = self.search()
        if response:
            for entry in response['entries']:
                paper = {
                    'title': entry['title'],
                    'authors': entry['authors'],
                    'summary': entry['summary'],
                    'published': entry['published'],
                    'link': entry['link']
                }
                papers.append(paper)
        return papers[:self.max_results]