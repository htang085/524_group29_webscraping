# parse_content.py
# author: Sienko Ikhabi
# date: 2025-01-16

from lxml import etree
from lxml.html import fromstring

def parse_content(html, selector, selector_type = 'css'):
    """
    Parses HTML content to extract data based on the provided selector.

    Parameters:
        html (str): The raw HTML content.
        selector (str): The CSS selector or XPath expression to target elements.
        selector_type (str): The type of selector ('css' or 'xpath'). Case-insensitive

    Returns:
        list: A list of extracted data elements.

    Raises:
        ValueError: If the selector_type is unsupported or parsing fails.

    Example:
        # Sample HTML content
        html = '''
        <html>
            <body>
                <div class="item">alfa</div>
                <div class="item">bravo</div>
                <div class="item">charlie</div>
            </body>
        </html>
        '''

        # Using CSS selector
        parse_content(html, ".item")  # Returns: ['alpha', 'bravo', 'charlie']

        # Using XPath selector
        parse_content(html, "//div[@class='item']", selector_type='xpath')  # Returns: ['alpha', 'bravo', 'charlie']
    """
    # check that selector_type in [xpath, css]
    if not selector_type.lower() in ['xpath', 'css']:
        raise ValueError("Only CSS/XPath selectors are supported")    
    # process the value
    elif(selector_type.lower() == 'xpath'):
        # first, we try to read the value 
        try:
            value_tree = etree.fromstring(html)
        except:
            raise ValueError("Unable to parse the content provided for XPath")
        # parsed OK
        temp_result = value_tree.xpath(selector)
        parsed_value = [t.strip() for t in temp_result if len(t.strip()) > 0]
    else:
        try:
            # for CSS, we must parse the string as using etree first
            # because `fromstring` is lenient
            value_tree = etree.fromstring(html)
            # now parse as HTML
            value_tree = fromstring(html)
        except:
            raise ValueError("Unable to parse the content provided for CSS")
        # parse as HTML, extract the CSS
        temp_result = value_tree.cssselect(selector)
        parsed_value = [t.text_content() for t in temp_result if len(t.text_content().strip()) > 0]
    return parsed_value
