import os
import sys

def bold_tag(func):
    
    def inner(*args, **kwdargs):
        return '<b>'+func(*args, **kwdargs)+'</b>'
        
    return inner

def italic_tag(func):
    
    def inner(*args, **kwdargs):
        return '<i>'+func(*args, **kwdargs)+'</i>'
        
    return inner
    
#Add greet() function definition
@italic_tag
@bold_tag
def greet():
    return input()

print(greet())
