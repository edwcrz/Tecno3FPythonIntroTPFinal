{
    'Centro de Estudios' : 'Tecno 3F',
    'Curso' : 'Introducción al Python',
    'Profesor' : 'Gabriel Roman'
}  
El programa se encuentra en el subtree PaswordGenerator de repositorio Tecno3FPythonIntroTPFinal,  
lo trabajo como un repositorio independiente con su correspondiente directorio local,  
y luego los consolido en el repositorio de entrega Tecno3FPythonIntroTPFinal,  
con el objetivo de conservar el historial,  
tiene la rama main,  

El objetivo del programa es generar un password aleatorio,  
debe evitar hardcodear cantidades,  
el probrama solicita la cantidad de caracteres de la password a generar,  
adicionalmente solicita los siguientes criterios de seguridad para generar la password,  
el largo de caracteres especiales recordando que el minimo a ingresar es 2,  
el largo de numeros recordando que el minimo a ingresar es 3,  
el largo de letras mayusculas recordando que el minimo es 2,  
el largo de letras minusculas lo calcula automáticamente segun los valores ingresados,  

se controla que se le ingrese estrictamente un numero entero,  
no debe permitir que se le ingrese un numero separado por coma, por punto, una letra o un caracter especial,  

se genera una lista de digitos elegidos aleatotiamente respescto de los digitos disponiebles por cada uno de los 4 criterios,  
luego lo agrupo las 4 listas correspondientes a los elegidos,  
luego los vuelvo a elegir aleatoriamente de dicha lista para generar un orden aleatorio y que no queden los criterios agrupados,  

al final informa el password generado aleatoriamente,  

Eduardo Cruz  