

class Vertex:
    def __init__(self, pos, schläffli = (4,4,4,4)):
        self.pos = pos
        self.children = []

    def add_child(self, child):
        self.children = child
