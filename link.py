'''This file contain different replace functions.'''

import re

status_pattern = re.compile(r'\.\. status:: title=(\w+) color=(\w+)\s*')
link_pattern = re.compile(r'.. link:: title=(.*?)\s+address=(\S+)')
image_pattern = re.compile(r'.. image:: height=(.*?)\s+address=(\S+)')
children_pattern = re.compile(r'.. children:: depth=(\d)')
contentBylabel_pattern = re.compile(r'.. contentBylabel:: label=(.*?)\s')
datetime_pattern = re.compile(r'\.\. datetime:: timestamp=(\S+)\s*')

def content_replace_match(match):
    '''This function replace string in content by label format'''

    label = match.group(1)
    confluence_content_format = f'''<ac:structured-macro ac:name="contentbylabel">
    <ac:parameter ac:name="label">{label}</ac:parameter>
    </ac:structured-macro>'''
    #print(confluence_content_format)
    return confluence_content_format

def children_replace_match(match):
    '''This function replace string in children display format'''

    depth = match.group(1)
    confluence_children_format = f'''<p><ac:structured-macro ac:name="children">
    <ac:parameter ac:name="depth">{depth}</ac:parameter>
    </ac:structured-macro></p>'''
    #print(confluence_children_format)
    return confluence_children_format

def image_replace_match(match):
    '''This function replace string in image format'''

    height, address = match.groups()
    confluence_image_format = f'''
                <ac:image ac:height="{height}">
                    <ri:attachment ri:filename="{address}" />
                </ac:image>'''
    #print(confluence_image_format)
    return confluence_image_format

def link_replace_match(match):
    '''This function replace string in link format'''
    key, value = match.groups()
    confluence_link_format = f""" <a href="{value}">{key}</a> """

    return confluence_link_format

def status_replace_match(match):
    '''This function replace string in status format'''

    key, value = match.groups()
    status_xml = f"""<ac:structured-macro ac:name="status"><ac:parameter ac:name="title">{key}</ac:parameter><ac:parameter ac:name="color">{value}</ac:parameter></ac:structured-macro>"""
    return status_xml


def datetime_replace_match(match):
    '''This function replaces string in datetime format using the <time> HTML tag'''

    timestamp = match.group(1)
    datetime_html_format = f'''<time datetime="{timestamp}" />'''
    
    return datetime_html_format
