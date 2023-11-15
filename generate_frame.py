#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generate_card import generate_card_html
from generate_css import generate_css


def generate_frame(cards_data_file_path: str, css_data_file_path: str) -> str:
    
    # Call generate_css function to get the CSS code
    css_code = generate_css(css_data_file_path)
    print(f"generate css over!")
    card_html = generate_card_html(cards_data_file_path)
    print(f"generate html over!")
    
    # Assemble the HTML frame
    html_frame = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>服务器服务导航</title>
    {css_code}
</head>
<body>
    {card_html}
</body>
</html>
'''
    return html_frame

# Example usage
# generated_html = generate_frame()
# print(generated_html)
