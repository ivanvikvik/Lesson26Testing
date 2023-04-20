import bus

if __name__ == "__main__":
    b = bus.Bus()
    b._number = -10  # protected
    print(b)
