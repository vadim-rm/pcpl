from entities import CDLibrary, CD, CDLibraryCDs

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
