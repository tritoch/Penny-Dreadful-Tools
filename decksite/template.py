import pystache

def render_name(template, *context):
    return renderer().render_name(template, *context)

def render(view):
    return renderer().render(view)

def renderer():
    return pystache.Renderer(search_dirs=['decksite/templates'])
