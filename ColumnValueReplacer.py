class ColumnValueReplacer:

    @staticmethod
    def replace_value_from_column(column, old, new):
        return column.apply(lambda x: str(x).replace(old, new))
