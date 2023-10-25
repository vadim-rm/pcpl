from gen_random import gen_random


class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.returned_items = set()

    def _get_element_for_comparing(self, el):
        if isinstance(el, str):
            return el.lower() if self.ignore_case else el
        return el

    def __next__(self):
        while True:
            element = next(self.items)

            if self._get_element_for_comparing(element) not in self.returned_items:
                found = True
                break

        if found:
            self.returned_items.add(self._get_element_for_comparing(element))
            return element

        raise StopIteration

    def __iter__(self):
        return self


if __name__ == "__main__":
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(list(Unique(data)))  # [1, 2]

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data)))  # ['a', 'A', 'b', 'B']

    data = gen_random(10, 1, 3)
    print(list(Unique(data)))  # [2, 1, 3]

    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data, ignore_case=True)))  # ['a', 'b']
