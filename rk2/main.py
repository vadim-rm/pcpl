from collections import Counter
from operator import itemgetter
from typing import Dict, List

import data
from entities import CDLibrary, CD, CDLibraryCDs


def get_one_to_many_binding(libraries: List[CDLibrary], cds: List[CD]):
    return [(cd.title, cd.author, library.name)
            for library in libraries
            for cd in cds
            if cd.library_id == library.id]


def get_many_to_many_binding(libraries: List[CDLibrary], libraries_cds: List[CDLibraryCDs], cds: List[CD]):
    many_to_many_temp = [(library.name, libraries_cd.cd_library_id, libraries_cd.cd_id)
                         for library in libraries
                         for libraries_cd in libraries_cds
                         if library.id == libraries_cd.cd_library_id]

    return [(cd.id, cd.title, cd.author, library_name)
            for library_name, cd_library_id, cd_id in many_to_many_temp
            for cd in cds if cd.id == cd_id]


def get_quantity_of_cds_in_libraries(libraries: List[CDLibrary], cds: List[CD]):
    libraries_counter = Counter([cd.library_id for cd in cds])
    return [(l.name, libraries_counter[l.id]) for l in libraries]


def get_library_list_for_each_cd(many_to_many, cds: List[CD]):
    result: Dict[str, List[str]] = {}
    for cd in cds:
        libraries_with_cd = [m[3] for m in filter(lambda i: i[0] == cd.id, many_to_many)]
        result[cd.title] = libraries_with_cd

    return result


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = get_one_to_many_binding(data.libraries, data.cds)

    # Соединение данных многие-ко-многим
    many_to_many = get_many_to_many_binding(data.libraries, data.libraries_cds, data.cds)

    # «Библиотека CD дисков» и «CD диск» связаны соотношением один-ко-многим.
    # Выведите список всех связанных CD дисков и библиотек, отсортированный по названию диска,
    # сортировка по библиотекам произвольная.
    print('Задание Б1')
    result_a = sorted(one_to_many, key=itemgetter(0))
    print(result_a)

    # «Библиотека CD дисков» и «CD диск» связаны соотношением один-ко-многим.
    # Выведите список библиотек с количеством дисков в каждой библиотеке, отсортированный по количеству дисков.
    print('\nЗадание Б2')
    result_b_unsorted = get_quantity_of_cds_in_libraries(data.libraries, data.cds)
    print(sorted(result_b_unsorted, key=itemgetter(1), reverse=True))

    # «Библиотека CD дисков» и «CD диск» связаны соотношением многие-ко-многим.
    # Выведите список всех дисков, у которых название заканчивается на «e», и названия их библиотек.
    print('\nЗадание Б3')
    print(get_library_list_for_each_cd(many_to_many, list(filter(lambda x: x.title.endswith('e'), data.cds))))


if __name__ == '__main__':
    main()
