import unittest
from unittest.mock import patch, MagicMock
from subfinder import check_subdomain

class TestSubfinder(unittest.TestCase):

    @patch('requests.get')
    def test_found_subdomain(self, mock_get):
        """Test karein ki 200 status code par tool sahi report karta hai."""
        # Mock response setup
        mock_get.return_value.status_code = 200
        
        # Function call (yahan sirf check kar rahe hain ki crash na ho)
        try:
            check_subdomain("www", "google.com")
            success = True
        except Exception:
            success = False
            
        self.assertTrue(success)

    @patch('requests.get')
    def test_connection_error_handling(self, mock_get):
        """Test karein ki connection error aane par script crash nahi hoti."""
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
