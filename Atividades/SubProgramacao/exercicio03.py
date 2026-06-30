def permitir_acesso(ano_nascimento):
    idade = 2026 - ano_nascimento
    if idade >= 18:
        return True
    else:
        return False
    
print("--- VALIDADOR DE SISTEMA ---")
ano = int(input("Em qual ano você nasceu? "))

if permitir_acesso(ano):
    print("Acesso liberado ao sistema. Bem-vindo!")
else:
    print("Acesso bloqueado. Apenas para maiores de 18 anos")