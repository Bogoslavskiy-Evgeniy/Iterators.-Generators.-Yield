class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor_external_list = 0
        self.cursor_internal_list = -1
        return self

    def __next__(self):
        self.cursor_internal_list += 1
        if self.cursor_internal_list >= len(self.list_of_list[self.cursor_external_list]):
            self.cursor_external_list += 1
            self.cursor_internal_list = 0
        if self.cursor_external_list >= len(self.list_of_list):
            raise StopIteration
        item = self.list_of_list[self.cursor_external_list][self.cursor_internal_list]
        return item

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()