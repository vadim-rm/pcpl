def field(items, *args):
    assert len(args) > 0
    for item in items:
        result = {}
        for key in args:
            if key in item and item[key] is not None:
                result[key] = item[key]

        if len(result) == 1:
            yield list(result.values())[0]
        elif len(result) > 1:
            yield result


if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    print(list(field(goods, 'title')))  # 'Ковер', 'Диван для отдыха'
    print(list(field(
        goods,
        'title',
        'price',
    )))  # {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}
