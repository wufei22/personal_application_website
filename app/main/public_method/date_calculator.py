import datetime


class DateCalculator(object):

    @staticmethod
    def calculate_date(start_date, end_date):
        """
        calculator date function.
        :param start_date: start_date, form:"2023-01-01"
        :param end_date: end_date, form:"2023-01-01"
        :return: interval date
        """
        start_year = int(start_date.split("-")[0])
        start_month = int(start_date.split("-")[1])
        start_day = int(start_date.split("-")[2])
        end_year = int(end_date.split("-")[0])
        end_month = int(end_date.split("-")[1])
        end_day = int(end_date.split("-")[2])
        start_time = datetime.datetime(year=start_year, month=start_month, day=start_day)
        end_time = datetime.datetime(year=end_year, month=end_month, day=end_day)
        interval_day = (end_time - start_time).days
        return interval_day


if __name__ == '__main__':
    test_day = DateCalculator.calculate_date(start_date="2022-09-10", end_date="2023-02-07")
    print(test_day, type(test_day))
