from beans.Cuenta import Cuenta

cuenta_1 = Cuenta("DiscoDurodeRoer",0)
cuenta_2 = Cuenta("Fernando", 300)
         
#Ingresa dinero en las cuentas
cuenta_1.ingresar(300)
cuenta_2.ingresar(400)
         
#Retiramos dinero en las cuentas
cuenta_1.retirar(500)
cuenta_2.retirar(100)
         
#Muestro la informacion de las cuentas
#print(cuenta_1) # 0 euros
#print(cuenta_2) #600 euros