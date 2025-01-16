from lxml import etree
from io import StringIO

def parse_content(html, selector, selector_type = 'css'):
    """
    Parses HTML content to extract data based on the provided selector.

    Parameters:
        html (str): The raw HTML content.
        selector (str): The CSS selector or XPath expression to target elements.
        selector_type (str): The type of selector ('css' or 'xpath').

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
    # first, we try to read the value
    try:
        temp_file = StringIO(html)
        value_tree = etree.parse(temp_file)
    except:
        raise ValueError("Unable to parse the content provided")
    
    # parsed OK
    if(selector_type == 'xpath'):
        parsed_value = value_tree.xpath(selector)
    else:
        parsed_value = value_tree.xpath(selector)
    return parsed_value
