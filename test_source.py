import unittest
from app.models import Source

class TestSource(unittest.TestCase):
    '''
    Test function for setting up data used in instanciating Source class
    '''

    def setUp(self):
        self.id = 66778899
        self.name = "Reuters"
        self.description = "Test Source description"
        self.url = "https://www.reuters.com/breakingviews/didis-new-york-woes-mask-deeper-problems-2022-05-04/"
        self.category = "Politics"
        self.country = "Kenya"
        self.source = Source(self.id, self.name, self.description,
                             self.url, self.category, self.country)

    def test_init_article(self):
        '''
        Test case to check if Source class objects are instantiated and created as expected
        '''
        self.assertTrue(isinstance(self.source, Source))


if __name__ == '__main__':
    unittest.main()