# private
# public
# protected

class Bus:
    def __init__(self, brand='no name', price=0, number=[]):
        self._brand = brand          # protected
        self._price = price          # protected
        self._number = number        # protected

    def __str__(self):
        return f"Bus: {self._brand}, price = ${self._price}," \
               f"number = {self._number}"


if __name__ == "__main__":
    bus = Bus()
    bus._number = -10    # protected
    print(bus)