from collections import Counter
from operator import itemgetter
from typing import Dict, List


class CD:
    """CD диск"""

    def __init__(self, id_: int, title: str, author: str, library_id: int):
        self.id = id_
        self.title = title
        self.author = author

        self.library_id = library_id


class CDLibrary:
    """Библиотека CD дисков"""

    def __init__(self, id_: int, name: str):
        self.id = id_
        self.name = name


class CDLibraryCDs:
    """
    'CD диски библиотеки' для реализации
    связи многие-ко-многим
    """

    def __init__(self, cd_id: int, cd_library_id: int):
        self.cd_id = cd_id
        self.cd_library_id = cd_library_id


libraries = [
    CDLibrary(1, 'Tech House'),
    CDLibrary(2, 'Techno'),
    CDLibrary(3, 'Bangers'),
]

cds = [
    CD(1, 'Ferrari', 'James Hype', 1),
    CD(2, 'Dancing', 'James Hype', 1),
    CD(3, 'Music From Space', 'Horeno', 2),
    CD(4, 'The Age Of Love', 'Age Of Love', 2),
    CD(5, 'The X File', 'Matchy', 2),
]

libraries_cds = [
    CDLibraryCDs(1, 1),
    CDLibraryCDs(1, 3),

    CDLibraryCDs(2, 1),
    CDLibraryCDs(2, 3),

    CDLibraryCDs(3, 2),

    CDLibraryCDs(4, 2),
    CDLibraryCDs(4, 3),

    CDLibraryCDs(5, 2),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(cd.title, cd.author, library.name)
                   for library in libraries
                   for cd in cds
                   if cd.library_id == library.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(library.name, libraries_cd.cd_library_id, libraries_cd.cd_id)
                         for library in libraries
                         for libraries_cd in libraries_cds
                         if library.id == libraries_cd.cd_library_id]

    many_to_many = [(cd.id, cd.title, cd.author, library_name)
                    for library_name, cd_library_id, cd_id in many_to_many_temp
                    for cd in cds if cd.id == cd_id]

    # «Библиотека CD дисков» и «CD диск» связаны соотношением один-ко-многим.
    # Выведите список всех связанных CD дисков и библиотек, отсортированный по названию диска,
    # сортировка по библиотекам произвольная.
    print('Задание Б1')
    result_a = sorted(one_to_many, key=itemgetter(0))
    print(result_a)

    # «Библиотека CD дисков» и «CD диск» связаны соотношением один-ко-многим.
    # Выведите список библиотек с количеством дисков в каждой библиотеке, отсортированный по количеству дисков.
    print('\nЗадание Б2')
    libraries_counter = Counter([cd.library_id for cd in cds])
    result_b_unsorted = [(l.name, libraries_counter[l.id]) for l in libraries]
    print(sorted(result_b_unsorted, key=itemgetter(1), reverse=True))

    # «Библиотека CD дисков» и «CD диск» связаны соотношением многие-ко-многим.
    # Выведите список всех дисков, у которых название заканчивается на «e», и названия их библиотек.
    print('\nЗадание Б3')
    result_c: Dict[str, List[str]] = {}
    for cd in cds:
        if not cd.title.endswith('e'):
            continue

        libraries_with_cd = [m[3] for m in filter(lambda i: i[0] == cd.id, many_to_many)]
        result_c[cd.title] = libraries_with_cd
    print(result_c)


if __name__ == '__main__':
    main()
