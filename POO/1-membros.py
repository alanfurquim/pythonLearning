class Data:
    def __str__(self):
        """
        This function returns a string representation of a date object in the format "day/month/year".
        :return: A string representation of the date object, in the format "dia/mes/ano".
        """
        return f"{self.dia}/{self.mes}/{self.ano}"


d1 = Data()
d1.dia = 5
d1.mes = 12
d1.ano = 2019
print(d1)

d2 = Data()
d2.dia = 7
d2.mes = 11
d2.ano = 2020
print(d2)
