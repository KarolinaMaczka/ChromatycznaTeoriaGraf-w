class Circle:
    __slots__ = ["_pos_x", "_pos_y", "_radius"]

    def __init__(self, p_pos_x, p_pos_y, p_radius):
        assert p_radius > 0

        self._pos_x = p_pos_x
        self._pos_y = p_pos_y
        self._radius = p_radius

        return

    def intersects_with(self, p_other):
        """
            Decides whether two circles intersect.

        :param p_other: Another circle.
        :return: Boolean: Does given circles intersect?
        """
        assert isinstance(p_other, Circle)

        distance = ((self._pos_x - p_other._pos_x) ** 2 + (self._pos_y - p_other._pos_y) ** 2) ** 0.5

        return distance <= self._radius + p_other._radius

    def __repr__(self):
        return f"C(coord=(x={self._pos_x}; y={self._pos_y}); R={self._radius})"

    @property
    def pos_x(self):
        return self._pos_x

    @property
    def pos_y(self):
        return self._pos_y

    @property
    def radius(self):
        return self._radius
