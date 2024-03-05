from src.integration.arxiv.Arxiv import Arxiv
import os
from dotenv import load_dotenv

load_dotenv()

config = {
    'arxiv': {
        'url': os.getenv('ARXIV_URL'),
        'query': '',
        'max_results': os.getenv('ARXIV_MAX_RESULTS')
    }
}

for query in ['generative models', 'llms']:
    config['arxiv']['query'] = query.replace(' ', '+')
    
    arxiv = Arxiv(config)
    papers = arxiv.search()

    # print(papers)