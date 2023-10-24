import unittest

import data
from main import get_one_to_many_binding, get_many_to_many_binding, get_quantity_of_cds_in_libraries, \
    get_library_list_for_each_cd


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.data = data

    def test_get_one_to_many_binding(self):
        want = [('Ferrari', 'James Hype', 'Tech House'), ('Dancing', 'James Hype', 'Tech House'),
                ('Music From Space', 'Horeno', 'Techno'), ('The Age Of Love', 'Age Of Love', 'Techno'),
                ('The X File', 'Matchy', 'Techno')]
        actual = get_one_to_many_binding(self.data.libraries, self.data.cds)

        self.assertCountEqual(want, actual)

    def test_get_many_to_many_binding(self):
        want = [(1, 'Ferrari', 'James Hype', 'Tech House'), (2, 'Dancing', 'James Hype', 'Tech House'),
                (3, 'Music From Space', 'Horeno', 'Techno'), (4, 'The Age Of Love', 'Age Of Love', 'Techno'),
                (5, 'The X File', 'Matchy', 'Techno'), (1, 'Ferrari', 'James Hype', 'Bangers'),
                (2, 'Dancing', 'James Hype', 'Bangers'), (4, 'The Age Of Love', 'Age Of Love', 'Bangers')]
        actual = get_many_to_many_binding(self.data.libraries, self.data.libraries_cds, self.data.cds)

        self.assertCountEqual(want, actual)

    def test_get_quantity_of_cds_in_libraries(self):
        want = [('Techno', 3), ('Tech House', 2), ('Bangers', 0)]
        actual = get_quantity_of_cds_in_libraries(self.data.libraries, self.data.cds)

        self.assertCountEqual(want, actual)

    def test_get_library_list_for_each_cd(self):
        many_to_many = get_many_to_many_binding(self.data.libraries, self.data.libraries_cds, self.data.cds)
        want = {'Ferrari': ['Tech House', 'Bangers'], 'Dancing': ['Tech House', 'Bangers'],
                'Music From Space': ['Techno'], 'The Age Of Love': ['Techno', 'Bangers'], 'The X File': ['Techno']}
        actual = get_library_list_for_each_cd(many_to_many, self.data.cds)

        self.assertDictEqual(want, actual)
