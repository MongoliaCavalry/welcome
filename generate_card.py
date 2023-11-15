#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def generate_card_core(info):
    print(info)
    name = info.get("name", "No Name")  # Use a default value if "name" is not present
    card_code = f'''
            <!-- Example service card -->
            <div class="card">
                <div class="card-info">
                    <h2>{name}</h2>
                    <p>{info.get("introduction", "")}</p>
                    <p>Port: {info.get("port", "")}</p>
                </div>
                <div class="card-action">
                    <a href="http://{info.get("ip", "")}:{info.get("port", "")}" target="_blank">访问</a>
                </div>
            </div>
    '''
    return card_code


def generate_cards_container(infos):
    print(infos)
    cards_html = [generate_card_core(info) for info in infos.values()]
    cards_container_code = f'''
        <div class="cards-container">
            {''.join(cards_html)}
        </div>
    '''
    return cards_container_code


def generate_category(blog_name, infos):
    print(f"generate_category: {blog_name}")
    cards_container_html = generate_cards_container(infos)
    category_code = f'''
    <div class="category">
        <h2 class="category-title">{blog_name}</h2>
        {cards_container_html}
    </div>
    '''
    return category_code

def read_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at path: {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Unable to decode JSON from file at path: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
        
        
def generate_card_html(cards_data_file_path: str) -> str:
    
    htmls = []
    data = read_json_file(file_path=cards_data_file_path)

    for blog_name, blog_data in data.items():
        print("generate_card_html:" + blog_name)
        htmls.append(generate_category(blog_name, blog_data))

    result_html = ''.join(htmls)
    return result_html

