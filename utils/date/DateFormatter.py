from pandas import Series


class DateFormatter:
    @staticmethod
    def format_date_column(month_list: Series):
        new_month_column = []
        for month in month_list:
            text_month = month[:2]
            text_year = month[3:]
            new_month_value = text_year + '/' + text_month
            new_month_column.append(new_month_value)
        return new_month_column

    @staticmethod
    def remove_day_of_month_from_date(month_list: Series):
        new_month_column = []
        for month in month_list:
            new_month_column.append(month[3:])
        return new_month_column
