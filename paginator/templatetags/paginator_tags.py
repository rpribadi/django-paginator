from django import template
from django.template import Context
from django.core.paginator import Paginator, InvalidPage

register = template.Library()

from paginator.paginator import Paginator

class PaginatorNode(template.Node):
    def __init__(self, object_list, per_page, max_page_nav, max_jumper, template):
        self.paginator = Paginator(object_list,
                                   per_page=per_page,
                                   max_page_nav=max_page_nav,
                                   max_jumper=max_jumper)
        self.template = template

    def render(self, context):
        t = template.loader.get_template(self.template)
        return t.render(
            Context({'paginator': paginator},
            autoescape=context.autoescape)
        )


def do_render_page_nav(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, date_to_be_formatted, format_string = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires exactly two arguments" % token.contents.split()[0])

    if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    return RenderPageNavNode(date_to_be_formatted, format_string[1:-1])

register.tag('render_page_nav', do_render_page_nav)



from django.utils.safestring import mark_safe

register = template.Library()

@register.filter()
def render_nav(paginator):
    t = template.loader.get_template('paginator/paginator.html')
    return mark_safe(t.render(
        Context({'paginator': paginator},
    )))

