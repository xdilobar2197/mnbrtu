# mnbrtu


class Temperature:
    def __init__(self, degree):
        self.degree = degree

    def check_weather(self):
        return "Issiq" if self.degree == 25 else "Sovuq"
