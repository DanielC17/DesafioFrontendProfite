class Produto():
    def init(self, id, name, image, oldPrice, price, discription, count, value) -> None:
        self._id = id
        self._name = name
        self._image = image
        self.old_price = oldPrice
        self._price = price
        self._discription = discription
        self._count = count
        self._value = value

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_image(self):
        return self._image

    def set_image(self, img):
        self._image = img

    def get_oldPrice(self):
        return self.old_price

    def set_oldPrice(self, oldprice):
        self.old_price = oldprice

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_discription(self):
        return self._discription

    def set_description(self, discription):
        self._discription = discription

    def get_count(self):
        return self._count

    def set_count(self, count):
        self._count = count

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value