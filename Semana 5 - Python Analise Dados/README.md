# Semana 5 – Sistema de Análise de Dados (Python)

O `analise_dados.py` lê um arquivo CSV com dados de contatos, valida cada campo com expressões regulares (módulo `re`), separa os registros válidos e inválidos e gera um relatório. O relatório é impresso no terminal e salvo em `relatorio.txt`.

## Como executar

```bash
python analise_dados.py              # usa dados.csv
python analise_dados.py outro.csv    # usa outro arquivo
```

## Validações aplicadas

Cada campo tem uma regra. Os padrões ficam em raw strings (`r"..."`) para que os `\` não sejam interpretados como escape do Python.

| Campo | Padrão | Justificativa |
|-------|--------|---------------|
| `email` | `^[\w.+-]+@[\w-]+(\.[\w-]+)+$` | Parte local com letras, números, `.`, `+` e `-`; domínio com pelo menos um ponto, o que barra `bruno@dominio`. |
| `cpf` | `^\d{3}\.\d{3}\.\d{3}-\d{2}$` | Formato fixo `000.000.000-00`, com 11 dígitos. Não valida os dígitos verificadores. |
| `telefone` | `^\(\d{2}\) \d{4,5}-\d{4}$` | DDD entre parênteses, espaço, 4 ou 5 dígitos, hífen e 4 dígitos. |
| `data` | `^\d{2}/\d{2}/\d{4}$` + `strptime` | O regex garante o formato; o `strptime` confere se a data existe (rejeita `31/02`). |
| `idade` | `int()` + faixa 0 a 120 | `int()` rejeita texto; a faixa é uma regra de negócio. |
| `nome` | não vazio | Campo obrigatório. |

O `fullmatch` é usado com os padrões `^...$`, então o valor inteiro precisa bater com o padrão, sem sobras.

## Exceções tratadas

- **`FileNotFoundError`:** arquivo inexistente. O `main()` mostra uma mensagem em vez de quebrar.
- **`KeyError`:** coluna obrigatória ausente no CSV. A checagem é feita no cabeçalho com `verificar_colunas()`, antes de ler as linhas.
- **`ValueError`:** conversão inválida (`idade = "abc"`) ou data impossível (`31/02/1995`). Cada linha é validada dentro de um `try`, então o erro vira um motivo no relatório e o processamento continua.
- **`FormatoInvalidoError` (personalizada):** campo que não bate com o padrão regex. Herda de `Exception`.
- **`IdadeInvalidaError` (personalizada):** idade fora da faixa 0 a 120. Herda de `Exception`.

O `main()` usa `try/except/else/finally`: o `else` só roda quando a análise termina sem erro de arquivo, e o `finally` sempre imprime o encerramento.

## Exemplo de entrada (`dados.csv`)

```csv
nome,email,cpf,telefone,data,idade
Ana Souza,ana.souza@email.com,123.456.789-01,(11) 91234-5678,15/03/1990,34
Bruno Lima,bruno@dominio,123.456.789-02,(21) 98765-4321,01/01/2000,25
Carla Dias,carla.dias@email.com,123.456.789-03,(31) 98765-4321,31/02/1995,40
Diego Mota,diego.mota@email.com,123.456.789-04,(41) 91111-2222,20/07/1988,150
Elisa Rocha,elisa@email.com,123.456.789-05,11 91234-5678,10/10/2001,22
Felipe Alves,felipe.alves@email.com,123.456.789-06,(51) 99999-0000,05/12/1975,abc
Gabriela Nunes,gabriela.nunes@email.com,123.456.789-07,(71) 98888-7777,25/08/1999,29
```

## Exemplo de saída (`relatorio.txt`)

```text
============================================================
RELATÓRIO DE ANÁLISE DE DADOS
============================================================
Total de registros: 7
Válidos: 2 (28.6%)
Inválidos: 5

Registros válidos:
  Ana Souza            ana.souza@email.com            123.456.789-01
  Gabriela Nunes       gabriela.nunes@email.com       123.456.789-07

Registros inválidos:
  Linha 3: email em formato inválido: 'bruno@dominio'
  Linha 4: data impossível: 31/02/1995
  Linha 5: idade fora da faixa 0-120: 150
  Linha 6: telefone em formato inválido: '11 91234-5678'
  Linha 7: idade não é número: 'abc'
```

Com um arquivo sem a coluna `idade`, a saída é `Erro no CSV: colunas ausentes: nome, idade.`. Com um arquivo inexistente, é `Erro: arquivo '...' não encontrado.`.
