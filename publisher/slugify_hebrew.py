# encoding: utf-8


HEBREW_STRING = u'אבגדהוזחטיכךלמםנןסעפףצץקרשת'
ENGLISH_SUBS = ['a','b','g','d','h','w','z','kh','t','y','c','C','l','m','M','n','N','s','aa','p','P','tz','TZ','k','r','sh','th']
ALLOWED_CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_0123456789'

SUBS_DICT = dict(zip(HEBREW_STRING, ENGLISH_SUBS))
SUBS_DICT.update( zip(ALLOWED_CHARS,ALLOWED_CHARS) )

WHITESPACE = '_'

def slugify (unicode_string):
    slug = ''
    ws = False
    for c in unicode_string:
        repl = SUBS_DICT.get(c,WHITESPACE)
        if not ws or repl != WHITESPACE: 
            slug += repl
        ws = repl == WHITESPACE
    return slug

if __name__=="__main__":
    
    print slugify("שלום עולם! מה המצב? ראיתי היום 35 תפוחים ליד Amsterdam!".decode('utf8'))
