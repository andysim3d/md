import Element

class Header(Element.Element):
    def __init__(self, content, level):
        super().__init__(content)
        self._level = level
    def _label(self):
        return "h{0}".format(self._level)
    def _render(self):
        return "<{0}> {1} </{0}>".format(self._label(), self._content)
    
    def nested(self):
        return False