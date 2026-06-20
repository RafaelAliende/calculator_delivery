from datetime import date, timedelta

produto = input('Digite o produto: ')
quantidade = int(input('Digite a quantidade: '))
dias_uteis = int(input('Digite quantos dias úteis: '))

hoje = date.today()
prazo = hoje + timedelta(days=dias_uteis)

print(f'\n--- PREVISÃO DE ENTREGA ---')
print(f'Produto: {produto}')
print(f'Quantidade: {quantidade}')
print(f'Data do pedido: {hoje.strftime("%d/%m/%Y")}')
print(f'Previsão de entrega: {prazo.strftime("%d/%m/%Y")}')