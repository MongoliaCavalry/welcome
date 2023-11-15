#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def generate_css_core(colors):
    css_code = f'''
<style>
body {{
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: linear-gradient(to right, {colors['body_gradient_start']}, {colors['body_gradient_end']});
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  flex-direction: column;
}}

.category {{
  background-color: {colors['category_background']};
  border-radius: 10px;
  margin: 10px 0;
  padding: 20px;
  box-sizing: border-box;
  width: 90%;
  max-width: 1200px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}}

.category-title {{
  text-align: center;
  color: {colors['category_title_color']};
  margin-bottom: 20px;
}}

.cards-container {{
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  gap: 10px;
}}

.card {{
  background-color: {colors['card_background']};
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: 5px;
  padding: 20px;
  flex: 1;
  min-width: calc((100% / 6) - 10px);
  box-sizing: border-box;
  text-align: left;
  display: flex;
  justify-content: space-between;
  align-items: center;
}}

.card-info {{
  flex: 3;
}}

.card-action {{
  flex: 1;
}}

.card h2 {{
  font-size: 1em;
  color: {colors['card_h2_color']};
}}

.card p {{
  font-size: 0.9em;
  color: {colors['card_p_color']};
}}

.card a {{
  background-color: {colors['card_a_background']};
  color: {colors['card_a_color']};
  padding: 10px 15px;
  border-radius: 5px;
  text-align: center;
  display: block;
  text-decoration: none;
}}

.card a:hover {{
  background-color: {colors['card_a_hover_background']};
}}

@media (max-width: 1400px) {{
  .card {{ min-width: calc((100% / 4) - 10px); }}
}}

@media (max-width: 1024px) {{
  .card {{ min-width: calc((100% / 3) - 10px); }}
}}

@media (max-width: 768px) {{
  .card {{ min-width: calc((100% / 2) - 10px); }}
}}

@media (max-width: 600px) {{
  .card {{ min-width: 100%; }}
}}
</style>
'''
    return css_code



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

def generate_css(css_data_file_path: str) -> str:
    
    color_dict = read_json_file(file_path=css_data_file_path)
    return generate_css_core(color_dict)

