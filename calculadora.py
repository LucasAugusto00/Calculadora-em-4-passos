print("---------CALCULADORA---------")

n=int(input("Digite 1 para soma, 2 para subtração,3 para multiplicação,4 para divisão:"))
x=float(input("Digite o primeiro número: "))
y=float(input("Digite o segundo número: "))

if n==1:
 print("RESULTADO:",x+y)
if n==2:
 print("RESULTADO:",x-y)
if n==3:
 print("RESULTADO:",x*y)
if n==4:
  if y==0:
   print("Não existe divisão por zero!")
  else:
    print("RESULTADO:",x/y) 