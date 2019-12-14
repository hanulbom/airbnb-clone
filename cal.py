import calendar

class Calendar():

    def __init(self, uear, month):
        self.year = year
        self.month = month
        self.day_names = ("mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
        self.month_names = (
            "January",
            "February",
            "March",
            "April",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        )

    def get_month(self):
        return self.month[self.month - 1]