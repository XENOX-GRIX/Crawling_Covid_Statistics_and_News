import re
import ply.lex as lex
import ply.yacc as yacc

###DEFINING TOKENS###
tokens = ('FIRST',
          'SECOND',
          'CONTENT',
          'SKIPTAG',
          'START',
          'LAST')
t_ignore = '\t'

###############Tokenizer Rules################
def t_START(t):
    r'<span.class="mw-headline".id="Worldwide_timelines_by_month_and_year">'
    return t

def t_FIRST(t):
     r'<a[^>]*>'
     return t

def t_SECOND(t):
    r'</a[^>]*>'
    return t

def t_LAST(t):
    r'<h2>'
    return t

def t_CONTENT(t):
    r'[A-Za-z0-9, ]+'
    return t

def t_SKIPTAG(t):
    r'<[^>]*>'
    return t

def t_error(t):
    t.lexer.skip(1)
####################################################################################################################################################################################################
											#GRAMMAR RULES
parsing_scope = False
count = 0

def p_start(p):
    '''start : table'''

def p_dataCell(p):
    '''dataCell : FIRST CONTENT SECOND '''
    global parsing_scope
    global count
    if parsing_scope and len(p) == 4:
        if any(year in p[2] for year in ('2019', '2020', '2021', '2022')):
            if count <= 70:
                link = re.search(r'href="([^"]+)"', p[1])
                if link:
                    with open('extracted_link.txt', 'a+',encoding="utf-8") as link_file:
                        link_file.write(link.group(1)+'\n')
                count += 1

def p_table(p):
    '''table : startTag tableContent lastTag
             | tableContent'''
    pass

def p_tableContent(p):
    '''tableContent : dataCell tableContent
                    | SKIPTAG tableContent
                    | CONTENT tableContent
                    | empty'''
    pass

def p_start_tag(p):
    '''startTag : START'''
    global parsing_scope
    parsing_scope = True

def p_last_tag(p):
    '''lastTag : LAST'''
    global parsing_scope
    parsing_scope = False

def p_empty(p):
    '''empty :'''
    pass

def p_content(p):
    '''content : CONTENT
               | empty'''
    p[0] = p[1]

def p_error(p):
    pass

#########DRIVER FUNCTION#######
def wiki_crawl():
    file_obj= open('webpage.html','r',encoding="utf-8")
    data=file_obj.read()
    lexer = lex.lex()
    lexer.input(data)
    wf = open('tokenlist.txt','w+', encoding="utf-8")
    for tok in lexer:
        wf.write(str(tok)+'\n')
    parser = yacc.yacc()
    parser.parse(data)
    file_obj.close()