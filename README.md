# Calculadora de Resistores

Este projeto é uma calculadora gráfica de resistores desenvolvida com **Tkinter**, permitindo que o usuário determine o valor de resistência com base nas cores das faixas de um resistor, conforme o padrão internacional de codificação (Resistor Color Code).

---

## ⚙️ Requisitos para Execução

* Python 3.8 ou superior
* Tkinter (já incluído por padrão na maioria das distribuições Python)
* IDE ou terminal (VS Code, PyCharm, Thonny etc.)

---

## ▶️ Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/Showberto/resistor-value-calculator
```

2. **Acesse a pasta do projeto:**

```bash
cd resistor-value-calculator
```

3. **Execute o script principal:**

```bash
python main.py
```

---

## 💡 Como Funciona

O programa abre uma interface gráfica com as seguintes opções:

* **Seleção do tipo de resistor:**

  * 4 faixas (resistores comuns)
  * 5 faixas (resistores de precisão)

* **Escolha das cores:**
  Menus suspensos permitem escolher as cores para cada faixa. As cores definem os dígitos significativos, o multiplicador e a tolerância.

* **Visualização gráfica:**
  O resistor é desenhado com as faixas coloridas correspondentes.

* **Cálculo automático do valor de resistência:**
  Com base na fórmula:

  * **4 faixas:**
    `(Dígito1 × 10 + Dígito2) × Multiplicador`

  * **5 faixas:**
    `(Dígito1 × 100 + Dígito2 × 10 + Dígito3) × Multiplicador`

---

## 🗂️ Estrutura de Arquivos

```
calculadora-resistores/
│
├── constants.py            # Dicionários de cores, valores, multiplicadores e tolerâncias
├── resistor_utils.py       # Funções auxiliares para cálculo e formatação do resistor
├── resistor_app.py         # Classe principal com a interface gráfica (Tkinter)
├── main.py                 # Ponto de entrada do programa
├── README.md               # Este arquivo
└── LICENSE                 # Licença do projeto (MIT)
```

---

## 📘 Sobre Resistores

Os resistores são componentes que limitam o fluxo de corrente elétrica. Eles são essenciais em circuitos analógicos e digitais para:

* Dividir tensões
* Controlar correntes
* Proteger componentes sensíveis
* Estabilizar sinais

### ✳️ Código de Cores

| Faixa        | Função                 |
| ------------ | ---------------------- |
| 1ª, 2ª, (3ª) | Dígitos significativos |
| 3ª ou 4ª     | Multiplicador          |
| Última       | Tolerância             |

---

## 📈 Aplicações em Engenharia

* Proteção de LEDs
* Circuitos de temporização e oscilação
* Filtros passivos
* Interfaces analógicas para sensores
* Divisores de tensão em medições

---

## 👨‍💼 Autor

**Roberto Franklin**
Engenheiro | Estudante de Automação e Programação
[LinkedIn](https://www.linkedin.com) • [GitHub](https://github.com)

---

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
