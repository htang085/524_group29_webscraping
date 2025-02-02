# test_parse_content.py
# author: Sienko Ikhabi
# date: 2025-01-16

import pytest
from dsci524_group29_webscraping import parse_content

def test_parse_simple_xpath():
    """
    Test using XPath on a simple HTML fragment.
    Ensures that function can retrieve all text from an HTML code block using XPath.
    """
    actual = parse_content('<p>Hello! World.</p>', '//p', 'XPath')
    expected = [{'value': 'Hello! World.'}]
    assert actual == expected, "Basic test with simple XPath <p> block failed."

def test_parse_simple_css():
    """
    Test using CSS on a simple HTML fragment.
    Ensures that function can retrieve specific tag from HTML code block using CSS.
    """
    actual = parse_content('<p class="test">ptest</p>', ".test", 'CSS')
    expected = [{'value': 'ptest'}]
    assert actual == expected, "Basic test with simple CSS <p> block failed."

def test_parse_invalid_selector():
    """
    Test that function gracefully handles invalid selector_type parameter.
    Check the function raises a ValueError when selector_type is not {'CSS', 'XPath'}
    """
    with pytest.raises(ValueError, match = "Invalid selector_type 'MyPath'. Only CSS/XPath selectors are supported."):
        parse_content('<p>test</p>', '//p', 'MyPath')

def test_parse_invalid_xpath():
    """
    Test that function gracefully handles invalid HTML string value (XPath branch).
    Check that ValueError is raised when html argument passed is not valid HTML for XPath case
    """
    with pytest.raises(ValueError, match = "Unable to parse the html_content provided."):
        parse_content('<body ><h1 />Testing Xpath<h1>', '\\h1', 'XPath')

def test_parse_invalid_css():
    """
    Test that function gracefully handles invalid HTML string value (CSS branch).
    Check that ValueError is raised when html argument passed is not valid HTML for CSS case
    """
    with pytest.raises(ValueError, match = "Unable to parse the html_content provided."):
        parse_content('<body><h1>Testing CSS</h1></body>', '--dummy', 'CSS')

def test_parse_zeromatch_xpath():
    """
    Test that function returns empty matches when no matching expression using XPath.
    A valid HTML that does not contain the specified XPath expression returns empty array.
    """
    actual = parse_content('<p>Hello! World.</p>', '//div', 'XPath')
    expected = []
    assert actual == expected, "Test for XPath selector with no matches."

def test_parse_zeromatch_css():
    """
    Test that function returns empty matches when no matching expression using CSS.
    A valid HTML that does not contain the specified CSS expression returns empty array.
    """
    actual = parse_content('<p class="test">ptest</p>', ".nomatch", 'CSS')
    expected = []
    assert actual == expected, "Test for CSS selector with no matches."