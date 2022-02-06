from django.template import Library

register = Library()

def get_likes(obj, *args):
    return obj.get_likes()

def get_comments(obj, *args):
    return obj.get_comments()

register.filter('get_likes', get_likes)
register.filter('get_comments', get_comments)