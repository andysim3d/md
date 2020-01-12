class Element(object):
    """Super class for objects"""
    def __init__(self, content):
        self._content = content # text content 

    def render(self):
        """render self as html format"""
        return self._render()

    def _render(self):
        pass

    def nested(self):
        return True

class ElementTree(object):
    def __init__(self):
        self.content = None
        self.children = [] # all sub elements