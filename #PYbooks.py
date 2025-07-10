#PYbooks.
listado_productos =[
'8475HD' ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'2175HD' ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
'JjfFHD' ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
'fgdxFHD' ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
'GF75HD' ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
'123FHD' ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
'342FHD' ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
'UWU131HD'['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],]



while True:
   
print (*** MENU PRINCIPAL ***)
print ("1. Stock Marca");
print ("2. Busqueda por precio");
print ("3. Listado de productos");
print ("4. Salir"); 

opc = int( input("ingrese opcion:"));


if(opc== 1):

marca == input("Ingrese la marca a consultar"):
#funcion para stock
def stock_marca(marca):
total= 31
for codigo, datos in productos.items():
    if(datos{1}.lower())== tipo.lower():
        total+== Inventario[codigo][1]:
print (f "El Stock total para'{marca}' es: {total}")
      
elif(opc== 2):
try
    precio_min = float(input)("ingrese precio minimo:")
    precio_max = float (input)("ingrese precio maximo:")
    buscar_por_precio(precio_min, peso_max);
    #Funcion para busqueda por marca
     def 
     buscar_por_Marca--Modelo(p_min, p_max)
     resultados = []:
     for codigo, datos in productos.items():
     precio == datos[4];
     if(marca >= p_min and precio <= p_max) and (productos{codigo}[1] > 0):
     resultados.append(codigo + '--'+datos[2]);
     if resultados
    resultados.sort();
    print ("productos encontrados:", resultados);

    else
    print("No hay notebooks en ese rango de precios.");
        
    
           


     except ValueError:
    print("Debe ingresar valores enteros!!")

elif(opc == 3);
while True:
codigo== input("ingrese Listado de productos")

try

   ordenar_producto == int(input("ingrese listado de notebooks"))
    if actualizar_listado("codigo, nuevo_stock")
   print("Stock de listado de notebook actualizado y ordenado!"):

else:
print("El codigo no Existe!"):
except ValueError
print ("debe ingresar el codigo para ver el stock o listado"):

repeat= input(Desea actualizar otro producto s/n):").low

if(repeat !='s'):
   break;

elif (opc == 4)
print("Programa finalizado.")

break;

else:
print("Debe seleccionar una opción válida!!,")
