import pprint

class Student:
    """class description student-entity"""

    def __init__(self):
        self.__marks = {}  # []
        self.id = 0

    def add(self, mark=0, subject=''):
        if subject:
            self.__marks[subject] = mark
        else:
            self.__marks[self.id] = mark
            self.id += 1

    def get_marks(self):
        return self.__marks.values()

    def get_subjects(self):
        return self.__marks.keys()

    def get_items(self):
        return self.__marks.items()

    def __find_max_index(self, ls):
        pass

    def __find_min_index(self, ls):
        pass

    def swap_max_min_elements(self, ls):
        index_min = self.find_min_index(ls)
        index_max = self.find_max_index(ls)
        ls[index_min], ls[index_max] = ls[index_max], ls[index_min]


if __name__ == "__main__":
    st = Student()
    st.add(10, "math")
    st.add(6, "C++")
    st.add(7, "Python")
    st.add(9)
    st.add(10)
    st.add(9)
    st.add(10)

    st.add(99)
    st.add(100)

    # st.add(10, "math")

    print(st.get_marks())
    pprint.pprint(st.get_items())
