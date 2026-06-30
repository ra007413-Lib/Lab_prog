def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius +1.8)+32

print("--- CONVERSOR DE TEMPERATURA ---")
C = float(input("Digite a temperatura em C.: "))
print(f"A temperatura correspondente é: {celsius_para_fahrenheit(C)}")