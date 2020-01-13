
def parse(context: str):
    if isinstance( context, Element):
        return (context,) 
    return (Text(context),)

class Element(object):
    """Super class for any objects"""
    def __init__(self, content):
        self._content = content # text content 

    def render(self):
        """render self as html format"""
        return self._render()

    def content(self):
        if self.nested():
            d = parse(self._content)
            return parse(self._content)
        else:
            d = Text(self._content)
            return [d]

    def inner_text(self):
        "inner text or nested elements as string format"
        p = [i._render() for i in self.content()]
        return "".join(p)

    def _render(self):
        pass

    def nested(self):
        """Could this element holds other elements inside, True for yes.
        """
        return False


class Text(Element):
    """Wrap for regular text"""
    def __init__(self, content):
        super().__init__(content)
    
    def _render(self):
        return str(self._content)
    
    def nested(self):
        return False

class Paragraph(Element):
    """ Stands for a single paragraph"""
    pass

class ElementTree(object):
    def __init__(self):
        self.content = None
        self.children = [] # all sub elements