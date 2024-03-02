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

def extract_info(file_path): 
    global lists
    global l 
    l = []
    lists = []
    file_obj= open(file_path,'r',encoding="utf-8")
    dat=file_obj.read()
    lexer = lex.lex()
    lexer.input(dat)
    f=open('yoyo.txt','w',encoding="utf-8")
    for tok in lexer:
        f.write(str(tok) + "\n")
    f.close
    parser = yacc.yacc()
    parser.parse(dat)

extract_info("./Pages/responses/Responses_to_the_COVID-19_pandemic_in_April_2021.html")