import unittest
from unittest.mock import patch
from subfinder import check_subdomain

class TestSubfinder(unittest.TestCase):

    @patch('requests.get')
    def test_found_subdomain(self, mock_get):
        """Test karein ki 200 status code par tool crash nahi hota."""
        mock_get.return_value.status_code = 200
        try:
            check_subdomain("www", "google.com")
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

    @patch('requests.get')
    def test_error_handling(self, mock_get):
        """Test karein ki Connection Error handle ho raha hai."""
        import requests
        mock_get.side_effect = requests.ConnectionError
        try:
            check_subdomain("invalid", "example.com")
            success = True
        except Exception:
            success = False
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()
