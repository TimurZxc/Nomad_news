from django import template
import os

register = template.Library()

@register.filter(name='truncate')
def truncate(value, arg):
    """
    Truncates a string after a certain number of characters but does not break the word.
    """
    try:
        length = int(arg)
    except ValueError:  # handle the case when arg is not an integer
        return value  # just return the original string
    if len(value) > length:
        return value[:length].rsplit(' ', 1)[0] + ' . . .'
    else:
        return value 
    
@register.filter
def basename(value):
    """Return the base name of a file path."""
    return os.path.basename(value)