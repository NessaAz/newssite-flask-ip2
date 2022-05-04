import unittest
from app.models import Article
from datetime import datetime


class TestArticle(unittest.TestCase):
    '''
    Test function for setting up data used in instanciating the Article class
    '''
    
    def setUp(self):
        self.source = 'https://newsapi.org/v2/everything?q=Politics&from=2022-05-04&sortBy=popularity&apiKey=7abbfe19bb734fc9b38d2ec53464b183'
        self.author = "Jane Doe"
        self.title = "Test Article on Politics - Reuters"
        self.description = "Test Article description"
        self.url = "https://www.reuters.com/breakingviews/didis-new-york-woes-mask-deeper-problems-2022-05-04/"
        self.url_to_image = "https://www.reuters.com/resizer/okAFpfbIRpNEDYyOBWo6aZbjvLY=/800x419/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/I5OEPBUM7RO53FO767L7JT3KYI.jpg"
        self.published_at = datetime.now()
        self.article = Article(self.source, self.author, self.title,
                               self.description, self.url, self.url_to_image, self.published_at)

    def test_init_article(self):
        '''
        Test case to check if Article class objects are instantiated and created as expected
        '''

        self.assertTrue(isinstance(self.article, Article))


if __name__ == '__main__':
    unittest.main()
