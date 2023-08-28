def build_where_clause(**kwargs):
    where_clause = ""

    if len(kwargs) > 0:
        where = []

        for key, value in kwargs.items():
            where.append("{0} = {1}".format(key, value))

        where_clause = " AND ".join(where)

    return where_clause


def build_choose_clause(choices, field):
    where_clause = ""

    if len(choices) > 0:
        where = []

        for choice in choices:
            where.append("{0}".format(choice))

        where_clause = ", ".join(where)
        where_clause = "{0} in ({1})".format(field, where_clause)

    return where_clause
