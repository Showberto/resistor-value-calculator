# constants.py

# Dicionários de valores, multiplicadores e tolerâncias
color = [
    "Black", "Brown", "Red", "Orange", "Yellow",
    "Green", "Blue", "Violet", "Gray", "White"
]

value = {
    "Black": 0, "Brown": 1, "Red": 2, "Orange": 3, "Yellow": 4,
    "Green": 5, "Blue": 6, "Violet": 7, "Gray": 8, "White": 9
}

Multi = {
    "Black": 1, "Brown": 10, "Red": 100, "Orange": 1_000, "Yellow": 10_000,
    "Green": 100_000, "Blue": 1_000_000, "Violet": 10_000_000,
    "Gray": 100_000_000, "White": 1_000_000_000
}

Tol = {
    "Brown": "±1%", "Red": "±2%", "Green": "±0.5%", "Blue": "±0.25%",
    "Violet": "±0.1%", "Gray": "±0.05%", "Gold": "±5%", "Silver": "±10%"
}
