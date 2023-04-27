from bus import *
from manager import Manager

x = 10

def main():
    bus1 = Bus("Scania", 23000, 42)
    bus2 = Bus("MAZ", 12000, 34)
    bus3 = Bus("Volvo", 31000, 48)
    bus4 = Bus("PAZ", 11000, 15)
    bus5 = Bus("Mercedes Benz", 123000, 67)

    y = x

    buses = (bus1, 5, bus2, 6.7, bus3, bus4, "dkjnfsdkj", bus5)

    result = Manager.find_bus(buses)

    print(result)


if __name__ == "__main__":
    main()
