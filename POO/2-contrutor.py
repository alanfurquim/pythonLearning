class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        """
        This function returns a string representation of a date object in the format "day/month/year".
        :return: A string representation of the date object, in the format "dia/mes/ano".
        """
        return f"{self.dia}/{self.mes}/{self.ano}"


d1 = Data(5, 12, 2019)
# d1.dia = 5
# d1.mes = 12
# d1.ano = 2019
print(d1)

d2 = Data(7, 11, 2020)
# d2.dia = 7
# d2.mes = 11
# d2.ano = 2020
print(d2)
