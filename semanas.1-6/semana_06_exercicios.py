import re
import math
from abc import ABC, abstractmethod


# Exercício Guiado 1: Classe Cliente
class Cliente:
    def __init__(self, nome, email, cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf

    def validar_email(self):
        padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$" # Regex para validação de e-mail
        return bool(re.match(padrao, self.email))

    def validar_cpf(self):
        padrao = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$" # Regex para validação de CPF
        return bool(re.match(padrao, self.cpf))

    def __str__(self):
        return f"{self.nome} <{self.email}>"


# Exercício Guiado 2: Herança com Animais
class Animal:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som

    def emitir_som(self):
        return f"{self.nome} faz {self.som}"


class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Au au!") # Repassa argumentos para a classe mãe

    def buscar(self):
        return f"{self.nome} está buscando a bolinha"


class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome, "Miau!")

    def arranhar(self):
        return f"{self.nome} arranhou o sofá"


# Exercício Guiado 3: Conta com Encapsulamento
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo # Atributo protegido
        self._historico = []

    @property
    def saldo(self): # Permite leitura controlada do saldo
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        self._saldo += valor
        self._historico.append(f"+{valor}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        if valor > self._saldo: # Impede saldo negativo
            raise ValueError("Saldo insuficiente")
        self._saldo -= valor
        self._historico.append(f"-{valor}")

    def extrato(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R$ {self._saldo:.2f}")
        for h in self._historico:
            print(f"  {h}")


# Exercício Guiado 4: Formas com Classe Abstrata
class Forma(ABC):
    @abstractmethod
    def area(self): # Método abstrato obrigatório nas filhas
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def descricao(self):
        nome = self.__class__.__name__
        return f"{nome}: área={self.area():.2f}, perímetro={self.perimetro():.2f}"


class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raio


class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)


# Exercício Guiado 5: Produtos com Polimorfismo
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def calcular_preco_final(self):
        return self.preco

    def __str__(self):
        return f"{self.nome}: R$ {self.calcular_preco_final():.2f}"


class ProdutoFisico(Produto):
    def __init__(self, nome, preco, frete):
        super().__init__(nome, preco)
        self.frete = frete

    def calcular_preco_final(self):
        return self.preco + self.frete # Polimorfismo com acréscimo de frete


class ProdutoDigital(Produto):
    def calcular_preco_final(self):
        return self.preco * 0.9 # Polimorfismo com desconto de 10%


# Exercício: Sistema Biblioteca
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self._disponivel = True

    def emprestar(self):
        if not self._disponivel:
            raise ValueError("Livro já emprestado")
        self._disponivel = False

    def devolver(self):
        self._disponivel = True

    def __str__(self):
        status = "Disponível" if self._disponivel else "Emprestado"
        return f"'{self.titulo}' - {self.autor} ({status})"


class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def pegar_emprestado(self, livro):
        livro.emprestar()
        self.livros.append(livro)

    def devolver_livro(self, livro):
        if livro in self.livros:
            livro.devolver()
            self.livros.remove(livro)
