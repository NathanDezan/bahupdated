from src.integration.arxiv.Arxiv import Arxiv
from src.integration.notion.Notion import Notion
from src.schema.Schema import Schema
from dotenv import load_dotenv
import os

load_dotenv()

config = {
    'arxiv': {
        'url': os.getenv('ARXIV_URL'),
        'query': '',
        'max_results': os.getenv('ARXIV_MAX_RESULTS')
    }
}

notion = Notion()
notion.database_status()

schema = Schema()
schema.set_database_id(os.getenv('NOTION_DATABASE_ID'))


for query in ['generative models']:
    config['arxiv']['query'] = query.replace(' ', '+')
    
    arxiv = Arxiv(config)
    papers = arxiv.get_papers()

    print(papers[0])

#make a function for remove left spaces, rights spaces and break line "\n"
def remove_spaces(text):
    return text.strip().replace('\n', '')