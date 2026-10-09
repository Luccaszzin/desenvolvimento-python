# Sistema bancário em POO: classes, herança, polimorfismo, encapsulamento e classe abstrata.

import re
from abc import ABC, abstractmethod

PADRAO_EMAIL = r"[\w.+-]+@[\w-]+(\.[\w-]+)+"


# Erro de regra de negócio: saque maior que o saldo disponível.
class SaldoInsuficienteError(Exception):
    pass


# Pessoa que pode ser titular de contas.
class Cliente:
    # Valida nome e e-mail pelos setters, então o objeto nunca fica inválido.
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def nome(self):
        return self._nome

    # Nome obrigatório: não pode ser vazio nem só espaços.
    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("nome não pode ser vazio")
        self._nome = valor.strip()

    @property
    def email(self):
        return self._email

    # E-mail precisa bater com o padrão (parte local, @, domínio com ponto).
    @email.setter
    def email(self, valor):
        if not isinstance(valor, str) or not re.fullmatch(PADRAO_EMAIL, valor):
            raise ValueError(f"e-mail inválido: {valor!r}")
        self._email = valor

    def __str__(self):
        return f"{self._nome} <{self._email}>"

    def __repr__(self):
        return f"Cliente(nome={self._nome!r}, email={self._email!r})"

    # Dois clientes são iguais quando têm o mesmo e-mail.
    def __eq__(self, outro):
        if not isinstance(outro, Cliente):
            return NotImplemented
        return self._email == outro._email

    def __hash__(self):
        return hash(self._email)


# Classe abstrata: define o contrato comum de todas as contas.
class Conta(ABC):
    # Titular é composição: a conta tem um Cliente.
    def __init__(self, titular, numero, saldo=0.0):
        if not isinstance(titular, Cliente):
            raise TypeError("titular deve ser um Cliente")
        self._titular = titular
        self.numero = numero
        self.saldo = saldo

    # Somente leitura: o titular não muda depois de criada a conta.
    @property
    def titular(self):
        return self._titular

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if not str(valor).strip():
            raise ValueError("número da conta não pode ser vazio")
        self._numero = str(valor).strip()

    @property
    def saldo(self):
        return self._saldo

    # Impede saldo negativo: o objeto nunca fica em estado inválido.
    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError(f"saldo não pode ser negativo: {valor}")
        self._saldo = float(valor)

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("valor do depósito deve ser maior que zero")
        self.saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("valor do saque deve ser maior que zero")
        if valor > self.saldo:
            raise SaldoInsuficienteError(
                f"saldo de R$ {self.saldo:.2f} insuficiente para sacar R$ {valor:.2f}"
            )
        self.saldo -= valor

    # Cada tipo de conta implementa o próprio cálculo (polimorfismo).
    @abstractmethod
    def calcular_rendimento_mensal(self):
        pass

    # Duas contas são iguais quando têm o mesmo número.
    def __eq__(self, outro):
        if not isinstance(outro, Conta):
            return NotImplemented
        return self._numero == outro._numero

    def __hash__(self):
        return hash(self._numero)

    # Permite ordenar contas pelo saldo com sorted().
    def __lt__(self, outro):
        if not isinstance(outro, Conta):
            return NotImplemented
        return self._saldo < outro._saldo

    def __repr__(self):
        return f"{type(self).__name__}({self._titular.nome!r}, {self._numero!r}, saldo={self._saldo})"


# Herda de Conta ("é um" tipo de conta) e cobra tarifa mensal.
class ContaCorrente(Conta):
    def __init__(self, titular, numero, saldo=0.0, tarifa=15.0):
        super().__init__(titular, numero, saldo)
        self.tarifa = tarifa

    @property
    def tarifa(self):
        return self._tarifa

    # Tarifa não pode ser negativa.
    @tarifa.setter
    def tarifa(self, valor):
        if valor < 0:
            raise ValueError(f"tarifa não pode ser negativa: {valor}")
        self._tarifa = float(valor)

    # Sobrescreve o método abstrato: conta corrente não rende, só cobra a tarifa.
    def calcular_rendimento_mensal(self):
        return -self._tarifa

    def __str__(self):
        return f"Conta corrente {self.numero} | {self.titular.nome} | R$ {self.saldo:.2f}"


# Herda de Conta e rende uma taxa mensal sobre o saldo.
class ContaPoupanca(Conta):
    def __init__(self, titular, numero, saldo=0.0, taxa_mensal=0.005):
        super().__init__(titular, numero, saldo)
        self.taxa_mensal = taxa_mensal

    @property
    def taxa_mensal(self):
        return self._taxa_mensal

    # Taxa precisa estar entre 0% e 100%.
    @taxa_mensal.setter
    def taxa_mensal(self, valor):
        if not 0 <= valor <= 1:
            raise ValueError(f"taxa mensal deve estar entre 0 e 1: {valor}")
        self._taxa_mensal = float(valor)

    # Sobrescreve o método abstrato com o rendimento da poupança.
    def calcular_rendimento_mensal(self):
        return self.saldo * self._taxa_mensal

    def __str__(self):
        return f"Poupança {self.numero} | {self.titular.nome} | R$ {self.saldo:.2f}"


# Agrega contas (composição: o banco contém contas).
class Banco:
    def __init__(self, nome, contas=None):
        if not nome:
            raise ValueError("nome do banco não pode ser vazio")
        self.nome = nome
        self._contas = []

        for conta in contas or []:
            self.adicionar_conta(conta)

    # Devolve uma cópia em tupla, para a lista interna não ser alterada de fora.
    @property
    def contas(self):
        return tuple(self._contas)

    # Não aceita conta duplicada (mesmo número).
    def adicionar_conta(self, conta):
        if not isinstance(conta, Conta):
            raise TypeError("só é possível adicionar objetos do tipo Conta")
        if conta in self._contas:
            raise ValueError(f"conta {conta.numero} já cadastrada")
        self._contas.append(conta)

    def buscar_conta(self, numero):
        for conta in self._contas:
            if conta.numero == str(numero):
                return conta
        return None

    # Soma os rendimentos de todas as contas, cada uma calculando do seu jeito.
    def rendimento_total(self):
        return sum(conta.calcular_rendimento_mensal() for conta in self._contas)

    def __str__(self):
        return f"{self.nome} ({len(self._contas)} contas)"

    def __repr__(self):
        return f"Banco({self.nome!r}, contas={len(self._contas)})"


def main():
    # Clientes
    ana = Cliente("Ana Souza", "ana@email.com")
    bruno = Cliente("Bruno Lima", "bruno@email.com")
    carla = Cliente("Carla Dias", "carla@email.com")
    diego = Cliente("Diego Mota", "diego@email.com")

    # Contas de classes diferentes, todas tratadas como Conta
    contas = [
        ContaCorrente(ana, "1001", saldo=500),
        ContaPoupanca(ana, "1002", saldo=2000),
        ContaCorrente(bruno, "2001", saldo=150),
        ContaPoupanca(bruno, "2002", saldo=800, taxa_mensal=0.006),
        ContaCorrente(carla, "3001", saldo=0),
        ContaPoupanca(diego, "4001", saldo=10000),
    ]

    banco = Banco("Banco Exemplo", contas)

    print(f"Banco criado: {banco}")
    print(f"Clientes: {[str(c) for c in (ana, bruno, carla, diego)]}")

    # Operações válidas
    contas[0].depositar(100)
    contas[0].sacar(50)
    print(f"\nApós depósito de 100 e saque de 50: {contas[0]}")

    # Polimorfismo: cada conta responde ao mesmo método de forma diferente
    print("\nContas e rendimento mensal:")
    for conta in banco.contas:
        print(f"  {conta} -> rendimento: R$ {conta.calcular_rendimento_mensal():+.2f}")

    print(f"\nRendimento total do banco: R$ {banco.rendimento_total():+.2f}")

    # Ordenação pelo saldo, usando __lt__
    print("\nContas ordenadas pelo saldo:")
    for conta in sorted(banco.contas):
        print(f"  {conta.numero}: R$ {conta.saldo:.2f}")

    # Busca
    encontrada = banco.buscar_conta("2002")
    print(f"\nBusca pela conta 2002: {encontrada}")
    print(f"Busca pela conta 9999: {banco.buscar_conta('9999')}")

    # Entradas inválidas: cada uma gera um erro tratado
    testes = [
        ("e-mail inválido", lambda: Cliente("Eva", "eva@dominio")),
        ("saldo negativo", lambda: ContaCorrente(ana, "1003", saldo=-10)),
        ("titular não é Cliente", lambda: ContaCorrente("Fulano", "1004")),
        ("depósito zero", lambda: contas[0].depositar(0)),
        ("saque acima do saldo", lambda: contas[0].sacar(999999)),
        ("taxa de poupança acima de 100%", lambda: ContaPoupanca(bruno, "2003", taxa_mensal=2)),
        ("conta com número repetido", lambda: banco.adicionar_conta(ContaPoupanca(carla, "1001"))),
    ]

    print("\nEntradas inválidas:")
    for descricao, acao in testes:
        try:
            acao()
        except (ValueError, TypeError, SaldoInsuficienteError) as erro:
            print(f"  [{descricao}] {type(erro).__name__}: {erro}")
        else:
            print(f"  [{descricao}] nenhum erro (inesperado)")

    # Tentar instanciar a classe abstrata também não é permitido
    try:
        Conta(ana, "9999")
    except TypeError as erro:
        print(f"  [classe abstrata] TypeError: {erro}")


if __name__ == "__main__":
    main()
