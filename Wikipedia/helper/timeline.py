import os
import ply.lex as lex
import ply.yacc as yacc

global_output_file = None
###DEFINING TOKENS###
tokens = ('FIRST',
          'SECOND',
          'CONTENT',
          'SKIPTAG',
          'HEADSTART',
          'HEADEND',
          'OPENHREF',
          'CLOSEHREF',
          'OPENFIG',
          'CLOSEFIG')
t_ignore = ' \t\n'

###############Tokenizer Rules################
def t_FIRST(t):
     r'<h2><span.class="mw-headline".id="Pandemic_chronology">'
     return t

def t_SECOND(t):
    r'<h2><span.class="mw-headline".id="Summary">'
    return t

def t_HEADSTART(t):
    r'<h3>'
    return t

def t_HEADEND(t):
    r'</span></h3>'
    return t

def t_OPENHREF(t):
    r'<a[^>]*>'
    return t

def t_CLOSEHREF(t):
    r'</a[^>]*>'
    return t

def t_OPENFIG(t):
    r'<figure[^>]*>'
    return t

def t_CLOSEFIG(t):
    r'</figure[^>]*>'
    return t

def t_CONTENT(t):
    r'[A-Za-z0-9, .]+'
    return t

def t_SKIPTAG(t):
    r'<[^>]*>'
    pass

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
											#GRAMMAR RULES
def p_start(p):
    '''start : section'''

def p_section(p):
    '''section : FIRST contentSequence SECOND '''

def p_contentSequence(p):
    '''contentSequence : contentSequence contentElement
                       | contentElement'''

def p_contentElement(p):
    '''contentElement : HEADSTART content HEADEND
                      | OPENHREF skip CLOSEHREF
                      | OPENFIG skipcontent CLOSEFIG
                      | CONTENT'''
    global global_output_file
    if len(p) == 2:
        global_output_file.write(str(p[1])+"\n")

def p_skip(p):
    '''skip : CONTENT skip
            | empty'''
    global global_output_file
    if len(p) == 3:
        try:
            float(p[1])
            int(p[1])
        except ValueError:
            if p[1] != 'edit':
                global_output_file.write(str(p[1])+"\n")

def p_skipcontent(p):
    '''skipcontent : CONTENT skipcontent
                   | OPENHREF skipcontent
                   | CLOSEHREF skipcontent
                   | empty'''

def p_content(p):
    ''' content : CONTENT'''
    global global_output_file
    if len(p) == 2:
        global_output_file.write('\n' + str(p[1]) + '\n')

def p_error(p):
    pass

def p_empty(p):
    '''empty :'''
    pass

#########DRIVER FUNCTION#######
def process_html_page(html_page_name, output_dir):
    global global_output_file
 
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
    timeline_file = './Pages/timeline.txt'
    output_dir = os.path.join('Pages', 'timeline_data')
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(timeline_file, 'r', encoding="utf-8") as file:
        for line in file:
            html_page_name = line.strip() 
            process_html_page(html_page_name, output_dir)