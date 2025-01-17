# test_fetch_html.py
# author: Lixuan Lin
# date: 2025-01-16

from dsci524_group29_webscraping.fetch_html import fetch_html
import unittest
from unittest.mock import patch, Mock
import requests
from requests.exceptions import RequestException

class TestFetchHtml(unittest.TestCase):
    """
    Unit tests for the fetch_html function.

    Each test case is designed to cover different scenarios and edge cases:
    - Successful HTTP requests.
    - Handling of HTTP errors (e.g., 404 Not Found).
    - Handling of timeouts.
    - Handling of invalid URLs.
    - Handling of connection errors.
    """
    @patch('requests.get')
    def test_fetch_html_success(self, mock_get):
        """
        Test fetch_html with a successful HTTP response.

        Mocks a valid HTTP response and checks if the returned HTML content matches the expected output.
        """
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = "<html><body>Success</body></html>"
        mock_get.return_value = mock_response

        url = "http://example.com"
        result = fetch_html(url)
        self.assertEqual(result, "<html><body>Success</body></html>")

    @patch('requests.get')
    def test_fetch_html_404_error(self, mock_get):
        """
        Test fetch_html with a 404 HTTP error.

        Mocks a 404 response and checks if the function raises a ValueError with the appropriate message.
        """
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
        mock_get.return_value = mock_response

        url = "http://example.com/notfound"
        with self.assertRaises(ValueError) as context:
            fetch_html(url)
        self.assertIn("404 Client Error", str(context.exception))

    @patch('requests.get')
    def test_fetch_html_timeout(self, mock_get):
        """
        Test fetch_html with a timeout exception.

        Mocks a timeout scenario and checks if the function raises requests.exceptions.Timeout.
        """
        mock_get.side_effect = requests.exceptions.Timeout("Request timed out")

        url = "http://example.com/timeout"
        with self.assertRaises(requests.exceptions.Timeout) as context:
            fetch_html(url)
        self.assertIn("Request timed out", str(context.exception))

    @patch('requests.get')
    def test_fetch_html_invalid_url(self, mock_get):
        """
        Test fetch_html with an invalid URL.

        Mocks an invalid URL scenario and checks if the function raises a ValueError with the appropriate message.
        """
        mock_get.side_effect = requests.exceptions.InvalidURL("Invalid URL")

        url = "invalid-url"
        with self.assertRaises(ValueError) as context:
            fetch_html(url)
        self.assertIn("Invalid URL", str(context.exception))

    @patch('requests.get')
    def test_fetch_html_connection_error(self, mock_get):
        """
        Test fetch_html with a connection error.

        Mocks a connection failure and checks if the function raises a ValueError with the appropriate message.
        """
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection failed")

        url = "http://example.com/connectionerror"
        with self.assertRaises(ValueError) as context:
            fetch_html(url)
        self.assertIn("Connection failed", str(context.exception))

if __name__ == "__main__":
    unittest.main()