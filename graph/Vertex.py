class Vertex:
    _counter = 0
    __slots__ = ["_name", "_deg", "_colour", "_info"]

    def __init__(self, p_info=None):
        self._name = f"v{Vertex._counter}"
        self._deg = 0
        self._colour = None
        self._info = p_info

        Vertex._counter += 1

    @property
    def name(self):
        return self._name

    @property
    def deg(self):
        return self._deg

    @deg.setter
    def deg(self, p_new):
        self._deg = p_new

    @property
    def colour(self):
        return self._colour

    @colour.setter
    def colour(self, p_new):
        self._colour = p_new

    @property
    def info(self):
        return self._info

    def __repr__(self):
        return "{" + f"name: {self._name}; colour: {self._colour}; info: {self._info}" + "}"

    def __eq__(self, other):
        assert isinstance(other, Vertex)

        return self._name == other.name
