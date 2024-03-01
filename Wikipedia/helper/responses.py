import os
import ply.lex as lex
import ply.yacc as yacc

has_seen_reference = False
global_output_file = None
###DEFINING TOKENS###
tokens = ('FIRST',
          'SECOND',
          'CONTENT',
          'SKIPTAG',
          'OPENHREF',
          'CLOSEHREF')
t_ignore = ' \t\n'

###############Tokenizer Rules################
def t_FIRST(t):
     r'<h2>'
     return t

def t_OPENHREF(t):
    r'<a[^>]*>'
    return t

def t_CLOSEHREF(t):
    r'</a[^>]*>'
    return t

def t_CONTENT(t):
    r'[A-Za-z0-9, .\-:\'()]+'
    return t

def t_SKIPTAG(t):
    r'<[^>]*>'
    pass

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : content_section'''

def p_content_section(p):
    '''content_section : FIRST content_items'''

def p_content_items(p):
    '''content_items : content_item content_items
                     | content_item'''

def p_content_item(p):
    '''content_item : contents
                    | FIRST
                    | link'''
    
def p_contents(p):
    '''contents : CONTENT'''
    global has_seen_reference 
    global global_output_file
    if p[1] == "See also":
        has_seen_reference = True

    if not has_seen_reference and p[1] != '160':
        global_output_file.write(str(p[1]))

def p_link(p):
    '''link : OPENHREF CONTENT CLOSEHREF
            | OPENHREF CONTENT CONTENT CONTENT CLOSEHREF
            | OPENHREF CONTENT CONTENT CLOSEHREF
            | OPENHREF CLOSEHREF'''
    global has_seen_reference 
    global global_output_file
    if len(p) == 4:
        try:
            float(p[2])
            int(p[2])
        except ValueError:
            if p[2] != 'edit' and not has_seen_reference:
                global_output_file.write(str(p[2]))
    if len(p) == 5:
        try:
            float(p[2])
            int(p[2])
            float(p[3])
            int(p[3])
        except ValueError:
            if p[2] != 'edit' and p[3] != 'edit' and not has_seen_reference:
                global_output_file.write(str(p[2]))
                global_output_file.write(str(p[3]))

def p_error(p):
    pass

#########DRIVER FUNCTION#######
def process_html_page(html_page_name, output_dir):
    global has_seen_reference, global_output_file
    has_seen_reference = False
    
    output_file_path = os.path.join(output_dir, os.path.basename(html_page_name).replace('.html', '.txt'))
    
    global_output_file = open(output_file_path, 'w', encoding="utf-8")
    file_obj = open(html_page_name, 'r', encoding="utf-8")
    data = file_obj.read()
    file_obj.close()
    
    with open(output_file_path, 'w+', encoding="utf-8") as output_file:
        lexer = lex.lex()
        lexer.input(data)
        
        parser = yacc.yacc()
        parser.parse(data)
        global_output_file.close() 

def crawls():
    responses_file = 'responses.txt'
    output_dir = os.path.join('helper', 'responses_data')
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    with open(responses_file, 'r', encoding="utf-8") as file:
        for line in file:
            html_page_name = line.strip()
            process_html_page(html_page_name, output_dir)