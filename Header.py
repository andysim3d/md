import Element
import os
class Header(Element.Paragraph):
    """ element of # marked head. level stands for number of '#'s"""
    def __init__(self, content, level):
        super().__init__(content)
        self._level = level
    def _label(self):
        return "h{0}".format(self._level)
    def _render(self):
        _rendered_ = "<{0}> {1} </{0}>".format(self._label(), self.inner_text())
        return _rendered_
    
    def nested(self):
        return False

class EmptyLine(Element.Paragraph):
    def __init__(self):
        super().__init__(None)
    def nested(self):
        return False
    def _render(self):
        return "<br/>"

class Sperater(Element.Paragraph):
    def __init__(self):
        super().__init__(None)
    def nested(self):
        return False

class LineSperator(Sperater):
    """Line seperator, usually by more than 3 - or _ in a row"""
    def __init__(self):
        super().__init__()
    def _render(self):
        return "<hr class='line_sep'/>"

class Quote(Element.Paragraph):
    """Quote paragraph, usually leading by >"""
    def __init__(self, content):
        super().__init__(content)
    def nested(self):
        return True
    def _render(self):
        """
        since Quote accepts nested, recursive render all inner elements and then output
        """
        return "<blockquote> {0} </blockquote>".format(self.inner_text())

class List(Element.Paragraph):
    """List element."""
    def __init__(self, content):
        super().__init__(content)
    
    def nested(self):
        return True
    
    def _label(self):
        return ""

    def _render(self):
        inner = "".join(ele._render() for ele in self.content())
        return "<{0}> {1} </{0}>".format(self._label(), self.inner_text())


class OrderedList(List):
    """List element."""
    def __init__(self, content):
        super().__init__(content)
    def _label(self):
        return "ol"    

class UnorderedList(List):
    """List element."""
    def __init__(self, content):
        super().__init__(content)
    def _label(self):
        return "ul"    


