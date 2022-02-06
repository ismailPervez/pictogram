from django.template import Library

register = Library()

def get_likes(obj, *args):
    return obj.get_likes()

def get_comments(obj, *args):
    return obj.get_comments()

def get_comment_count(obj, *args):
    return len(obj.get_comments())

def count(obj, *args):
    return len(obj)

register.filter('get_likes', get_likes)
register.filter('get_comments', get_comments)
register.filter('get_comment_count', get_comment_count)
register.filter('count', count)