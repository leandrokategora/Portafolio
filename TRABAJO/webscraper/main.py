import argparse
from common import config
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def _new_scraper(news_site_uid):
    host = config()['news_site'][news_site_uid]['url']

    logging.info('Beginning scraper for {}'.format(host))
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    news_site_choices = list(config()['news_site'].keys())
    parser.add_argument('news_site',
                        help='The new site that you want to scrape',
                        type=str,
                        choices=news_site_choices)

    args = parser.parse_args()
    _new_scraper(args.news_site)