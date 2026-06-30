def verificar_status(media):
    if media >=6:
        return "Aprovado"
    elif media >= 4:
        return "verificação suplementar"
    else:
        return "Reprovado"
    
nota = float(input("Digite a média do aluno: "))
print(f"Status do aluno: {verificar_status(nota)}")