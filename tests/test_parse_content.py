# test_parse_content.py
# author: Sienko Ikhabi
# date: 2025-01-16

import pytest
from dsci524_group29_webscraping.parse_content import parse_content

def test_parse_simple_xpath():
    actual = parse_content('<p>Hello! World.</p>', '//text()', 'XPath')
    expected = ['Hello! World.']
    assert actual == expected, "Basic test with simple XPath <p> block failed."

def test_parse_simple_css():
    actual = parse_content('<p class="test">ptest</p>', ".test", 'CSS')
    expected = ['ptest']
    assert actual == expected, "Basic test with simple CSS <p> block failed."

def test_parse_invalid_selector():
    """Check that ValueError is raised when selector_type is not known"""
    with pytest.raises(ValueError, match = "Only CSS/XPath selectors are supported"):
        parse_content('<p>test</p>', '//text()', 'MyPath')

def test_parse_invalid_xml():
    """Check that ValueError is raised when html is not valid"""
    with pytest.raises(ValueError, match = "Unable to parse the content provided for XPath"):
        parse_content('<body><h1>no closing tag<h1>', '//text()', 'XPath')

def test_parse_invalid_css():
    """Check that ValueError is raised when html is not valid"""
    with pytest.raises(ValueError, match = "Unable to parse the content provided for CSS"):
        parse_content('<body><h1>no closing tag<h1>', '.dummy', 'CSS')

def test_parse_zeromatch_xpath():
    actual = parse_content('<p>Hello! World.</p>', '//div', 'XPath')
    expected = []
    assert actual == expected, "Test for XPath selector with no matches."

def test_parse_zeromatch_css():
    actual = parse_content('<p class="test">ptest</p>', ".nomatch", 'CSS')
    expected = []
    assert actual == expected, "Test for CSS selector with no matches."