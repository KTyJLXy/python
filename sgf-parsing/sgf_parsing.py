class SgfTree(object):
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for k, v in self.properties.items():
            if k not in other.properties:
                return False
            if other.properties[k] != v:
                return False
        for k in other.properties.keys():
            if k not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for a, b in zip(self.children, other.children):
            if a != b:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if not re.match('\(;(.*)+\)', input_string):
        raise ValueError(input_string + ' does not match regex')
        
    # use this to preremove initial () and ;
    # (;a[b]a[c](;a[b])) -> a[b]a[c](;a[b])
    return SgfTree(string = input_string[2:-1])
