import time
import random

usuarios = []  

def menu_principal():
    while True:
        print("\n=== PLATAFORMA DE EDUCAÇÃO DIGITAL – ONG TECHNE ===")
        print("1. Cadastrar novo usuário")
        print("2. Ensino de Lógica de Programação")
        print("3. Segurança Digital (LGPD e Boas Práticas)")
        print("4. Estatísticas (Média de Idade dos Usuários)")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            cadastrar_usuario()
        elif escolha == "2":
            desafio_tabuada()  
        elif escolha == "3":
            seguranca_digital()
        elif escolha == "4":
            mostrar_estatisticas()
        elif escolha == "5":
            print("Obrigado por utilizar a plataforma!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def cadastrar_usuario():
    print("\n=== CADASTRO DE USUÁRIO ===")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    consentimento = input("Você autoriza o uso dos seus dados de forma anônima para fins educacionais? (sim/nao): ").lower()

    if consentimento == 'sim':
        usuarios.append({"nome": nome, "idade": idade})
        print("Usuário cadastrado com sucesso!")
    else:
        print("Cadastro cancelado por falta de consentimento (LGPD).")

def desafio_tabuada():
    print("\n=== DESAFIO: TABUADA PERSONALIZADA ===")
    nome = input("Qual seu nome, programador(a)? ")
    numero = int(input("Digite um número inteiro para ver a tabuada dele (1 a 10): "))
    
    print(f"\nMuito bem, {nome}! Aqui está a tabuada do {numero}:\n")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
        time.sleep(0.3)

    print("\nAgora é sua vez de responder uma pergunta...")

    multiplicador = random.randint(1, 10)

    resposta = int(input(f"Quanto é {numero} x {multiplicador}? "))
    if resposta == numero * multiplicador:
        print(" Parabéns! Você acertou!")
    else:
        print(f" Ops! Resposta errada. O correto era {numero * multiplicador}. Continue praticando!")

    print("Fim do desafio.\n")

def seguranca_digital():
    print("\n=== BOAS PRÁTICAS DE SEGURANÇA DIGITAL ===")
    print("- Use senhas fortes e diferentes para cada site.")
    print("- Não clique em links suspeitos recebidos por e-mail ou redes sociais.")
    print("- Mantenha seus dispositivos atualizados.")
    print("- Nunca compartilhe informações sensíveis com estranhos.")

    print("\n=== QUIZ DE SEGURANÇA ===")
    pergunta = input("É seguro usar a mesma senha em todos os sites? (sim/não): ").lower()
    if pergunta == "não":
        print(" Corretíssimo! Senhas únicas reduzem o risco de invasão.")
    else:
        print("Errado! Usar a mesma senha é um risco sério.")

def mostrar_estatisticas():
    print("\n=== ESTATÍSTICAS DOS USUÁRIOS ===")
    if not usuarios:
        print("Nenhum usuário cadastrado ainda.")
        return
    idades = [u["idade"] for u in usuarios]
    media = sum(idades) / len(idades)
    print(f"Média de idade dos usuários: {media:.1f} anos")


menu_principal()
