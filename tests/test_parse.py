import pytest
from dsci524_group29_webscraping.parse_content import parse_content

def test_parse_simple_xpath():
    actual = parse_content('<p>Hello! World.</p>', '//text()', 'xpath')
    expected = ['Hello! World.']
    assert actual == expected, "Basic test with simple XPath <p> block failed."

def test_parse_simple_css():
    actual = parse_content('<p class="test">ptest</p>', "//p[@class='test']/text()", 'CSS')
    expected = ['ptest']
    assert actual == expected, "Basic test with simple CSS <p> block failed."

def test_parse_invalid_selector():
    """Check that ValueError is raised when selector_type is not known"""
    with pytest.raises(ValueError):
        parse_content('<p></p>', '//text()', 'mypath')

def test_parse_invalid_xml():
    """Check that ValueError is raised when html is not valid"""
    with pytest.raises(ValueError):
        parse_content('<p>look at closing tag closely<p>', '//text()', 'mypath')