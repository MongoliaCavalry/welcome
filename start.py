#!/usr/bin/env python
# -*- coding: utf-8 -*-

from generate_frame import generate_frame


def write_html_code_to_file(html_content, file_path):
    try:
        with open(file_path, 'w') as file:
            file.write(html_content)
        print(f"HTML信息已成功写入文件: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    
    cards_data_file_path = './source/cards.json'
    css_data_file_path = './source/color_table.json'
    html_file_path = './index.html'
    code = generate_frame(cards_data_file_path=cards_data_file_path,
                          css_data_file_path=css_data_file_path)
    
    
    write_html_code_to_file(
        html_content=code,
        file_path=html_file_path
    )
