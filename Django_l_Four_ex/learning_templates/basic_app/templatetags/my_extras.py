from django import template

register = template.Library()

#this is second options using decorators
@register.filter(name='cut')
#Define custom filter called "cut" like a function
def cut(value, arg):
    """
    This cuts out all values of 'arg' from the string!
    """
    return value.replace(arg,'')

# register.filter('cut', cut)
