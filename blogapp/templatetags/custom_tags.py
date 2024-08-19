
# 3 type of custom tags 
# simple_tag
# inclusion_tag
# assignment_tag 

from django import template 
from ..models import Post 

register = template.Library()

@register.simple_tag
def total_post():
    return Post.objects.count()

