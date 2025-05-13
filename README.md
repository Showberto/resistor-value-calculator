
# 🧮 Calculadora de Resistores

Este projeto é uma calculadora interativa de resistores que permite ao usuário determinar o valor de resistência com base nas cores das faixas de um resistor, segundo o padrão internacional de codificação de cores (Resistor Color Code).

---

## ⚙️ Requisitos para Execução

Para rodar o código, é necessário ter instalado:

- Python 3.8 ou superior
- Um terminal ou IDE (como VS Code, PyCharm, Thonny etc.)

### ▶️ Como Executar

1. **Clone o repositório:**

```bash
git clone https://github.com/seuusuario/nome-do-repositorio.git
```

2. **Acesse a pasta do projeto:**

```bash
cd nome-do-repositorio
```

3. **Execute o script principal:**

```bash
python main.py
```

---

## 💡 Como Funciona

O programa solicita ao usuário que selecione:

- O tipo de resistor:
  - **Resistor Padrão (4 faixas)**
  - **Resistor de Precisão (5 faixas)**

Depois disso, o usuário deve informar as cores das faixas usando números que representam as cores conforme o código internacional. O programa então converte essas cores em valores numéricos, aplica o cálculo da resistência com base na fórmula:

- **4 faixas**:  
  `(Dígito1 × 10 + Dígito2) × Multiplicador`

- **5 faixas (Precisão)**:  
  `(Dígito1 × 100 + Dígito2 × 10 + Dígito3) × Multiplicador`

A tolerância é aplicada conforme a cor da última faixa.

---

## 🔧 Arquivos

- `main.py`: Arquivo principal onde ocorre a interação com o usuário.
- `funcoes_resistor.py`: Contém os dicionários de referência e as funções auxiliares.
- `README.md`: Este documento de explicação.

---

## 📘 Sobre Resistores

Os resistores são componentes elétricos passivos que limitam ou regulam a passagem de corrente elétrica em circuitos. Sua principal função é **controlar tensões e correntes**, proteger componentes sensíveis e dividir tensões.

### ✳️ Codificação de Cores

Os resistores usam faixas coloridas para indicar seu valor em ohms (Ω) e a tolerância de fabricação. Isso permite uma leitura rápida e padronizada para engenheiros e técnicos eletrônicos.

| Faixa | Função |
|-------|--------|
| 1ª, 2ª, (3ª) | Dígitos significativos |
| 3ª ou 4ª     | Multiplicador |
| Última       | Tolerância |

---

## 📈 Aplicações em Engenharia

- Controle de corrente em circuitos eletrônicos
- Divisores de tensão
- Ajuste de níveis de sinal
- Proteção de LEDs e microcontroladores
- Filtros, temporizadores e osciladores

A correta seleção e leitura dos resistores é **fundamental para o bom funcionamento de circuitos analógicos e digitais**, sendo um dos pilares da eletrônica aplicada.

---

## 👨‍💻 Autor

Roberto Bruno  
Engenheiro | Estudante de Automação e Programação  
[LinkedIn](https://www.linkedin.com) • [GitHub](https://github.com)

---

## 📜 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
