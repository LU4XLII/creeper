import unittest
import creeper

class TestCase(unittest.TestCase):
    # test if get page always return string even creeper is offline
    def test_get_page(self):
        result = creeper.get_page('not an url')
        assert isinstance(result, str)
        result = creeper.get_page(123)
        assert isinstance(result, str)

    def test_get_next_target(self):
        page = 'test <a href=\'http://blah.com\'>Blah</a> XXX'
        url, end_quote = creeper.get_next_target(page)
        assert isinstance(url, str)
        assert isinstance(end_quote, int)

if __name__ == "__main__":
    unittest.main()
