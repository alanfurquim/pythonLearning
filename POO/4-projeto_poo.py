from datetime import datetime, timedelta


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def __str__(self):
        return f'{self.nome}- ({len(self.pendentes())} tarefas pendentes)'

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    def procurar(self, descricao):
        # POSSIVEL ERRO
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluida)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')

        return f'{self.descricao} ' + ' '.join(status)


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Passar roupa', datetime.now())
    casa.add('Lavar prato', datetime.now() + timedelta(days=3))
    # print(casa)

    # casa.procurar('Lavar prato').concluir()
    for tarefa in casa.tarefas:
        print(f'- {tarefa}')

    mercado = Projeto('Compras mercado')
    mercado.add('Arroz', datetime.now())
    mercado.add('Feijão', datetime.now() + timedelta(days=2))
    mercado.add('Batata')
    print(mercado)
    comprar_batata = mercado.procurar('Batata')
    comprar_batata.concluir()
    for tarefa in mercado.tarefas:
        print(f'- {tarefa}')


if __name__ == '__main__':
    main()

WHEN "DATA_LINK_168512137557314EAB" LIKE '%.% BRL' THEN CAST(SUBSTRING("DATA_LINK_168512137557314EAB", 1, LEN("DATA_LINK_168512137557314EAB") - LEN(SUBSTRING(REVERSE("DATA_LINK_168512137557314EAB"), 1, PATINDEX('%.%', REVERSE("DATA_LINK_168512137557314EAB")) - 1))) + ',' + SUBSTRING("DATA_LINK_168512137557314EAB", LEN("DATA_LINK_168512137557314EAB") - LEN(SUBSTRING(REVERSE("DATA_LINK_168512137557314EAB"), 1, PATINDEX('%.%', REVERSE("DATA_LINK_168512137557314EAB")) - 1))) + 2, LEN("DATA_LINK_168512137557314EAB") - CHARINDEX(' BRL', "DATA_LINK_168512137557314EAB") - LEN(SUBSTRING(REVERSE("DATA_LINK_168512137557314EAB"), 1, PATINDEX('%.%', REVERSE("DATA_LINK_168512137557314EAB")))) - 2) AS FLOAT)