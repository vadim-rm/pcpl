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
