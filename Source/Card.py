CardWidth = 250
CardHeight = 350

class Card:
    def __init__(self, image_file, size, name, type, price, face_up=False):
        self._image_file = image_file
        self._size = size
        self._position = [0, 0]
        self._face_up = face_up
        self._name = name
        self._type = type
        self._price = price

    @property
    def x(self):
        return self._position[0]

    @property
    def y(self):
        return self._position[1]

    @property
    def image(self):
        if self._face_up:
            return self._image_file
        else:
            return "backside"

    def is_clicked(self, mouse_position):
        width, height = self._size
        mouse_x, mouse_y = mouse_position

        if self.x < mouse_x < self.x + width and self.y < mouse_y < self.y + height:
            return True
        else:
            return False

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return self.__str__()
