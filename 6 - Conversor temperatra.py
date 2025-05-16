# 1 - Celsius para Fahrenheit, use a fórmula:  
# (temp_inicial * 9 / 5) + 32 
# 2 - Celsius para Kelvin, use a fórmula: 
# temp_inicial + 273.15 

print("========== Conversor ==========")

temperatura_celcius = int(input("Digite a temperatura: "))

cel_fahrenheit = (temperatura_celcius * 9) + 32
cel_kelvin = temperatura_celcius + 273.15

print("===============================")
print("=== Escolha sua temperatura ===")
print("[1] - Fahrenheit")
print("[2] - Kelvin")
print("[3] - Encerrar")
print("===============================")

escolha = 0

while escolha != 3:
    
    escolha = int(input("Digite para qual deseja converter: "))
    
    if escolha == 1:
        
        print(f"{temperatura_celcius}° para Fahrenheit = {cel_fahrenheit}°F")
        
    if escolha == 2:
        
        print(f"{temperatura_celcius}° para Kelvin = {cel_kelvin}°")
    
