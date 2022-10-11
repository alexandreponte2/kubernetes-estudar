# # read -> para arquivos simples (senhas,tokens, informações únicas)

# with open("email.txt", "r") as arquivo:
#     arquivo = arquivo.read()
# print(arquivo)

# # readlines -> para arquivos maiores

# with open("mensagem.txt", "r", encoding="utf-8") as arquivo:
#     mensagem = arquivo.readlines()
# # print(mensagem)


# for linha in mensagem:
#     if "faturamento" in linha:
#         print(linha)


# # with open("senha.txt", "r") as arquivo:
# #     senha = arquivo.read()
# # print(senha)



with open("nova_senha.txt", "w") as arquivo:
    senha = arquivo.write("goku123")
print(senha)