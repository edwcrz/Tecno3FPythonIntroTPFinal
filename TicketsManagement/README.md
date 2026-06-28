<p style="line-height: 75%;"># Tecno3FPythonIntro  </p>
<p style="line-height: 75%;"># Trabajo Practico Final Tickets  </p>
<p style="line-height: 75%;">## {</p>
<p style="line-height: 75%;">##    'Centro de estudios' : 'Tecno3F',</p>
<p style="line-height: 75%;">##    'Curso' : ' Introducción al Python',</p>
<p style="line-height: 75%;">##    'Profesor' : 'Gabriel Roman',</p>
<p style="line-height: 75%;">##    'Alumno' : 'Eduardo Cruz',</p>
<p style="line-height: 75%;">##    'Trabajo' : 'Trabajo Práctico Final Tickets Management'</p>
<p style="line-height: 75%;">## }</p>
Se ha pedido crear un modulo para generar ticktes que contenga lo siguiente:  
Un menu con 3 opciones :  
1 Alta ticket ,   
2 Leer ticket ,  
3 Mostrar tickets,  
4 Salir.  

1 Alta ticket :  
nombre,  
sector,  
asunto,  
problema,  
Al terminar de ingresar el ticket se debera mostrar por pantalla el mismo,  
sumandose el numero de ticket (que sera un numero random entre 1000,9999) y  
una leyenda que pida acordarse del numero  
  
un menu que nos pregunte si deseamos crear otro ticket,  
en caso de ser noque nos regrese al menu principal,  
de lo contrario que nos regrese a la pantalla de alta.  
  
2 Leer ticket: numero ticket  
al ingresar el numero nos mostrara por pantalla el ticket almacenado  
debajo del mismo aparece una leyanda que nos preguntara si deseamos leerotro ticket,  
teniendo la funcionalidad similar a la anteriormente mensionada.  
  
3 debe mostrar los numeros de tickets ingresados con el proposito de memorizar uno para leerlo con la función 2  
  
4 Salir : el programa finaliza y se cierra pidiendonos una confirmacion  

el programa comienza en main  
se ejecuta el ingreso de la primer pantalla de PantallasEC02.py

si ingreso un 1, es porque se quiere ingresar un ticket
entonces llama a la funcion ingresar_ticket de IngresarTicketEC02.py
la funcion llama a la funcion leer_json de JsonEC02.py
el archivo Ticket.json se debe encontrar creado en el directorio del proyecto
el archivo tiene una lista, donde cada entrada es un diccionario
es decir es una lista de diccionarios
el archivo json se guarda en la lista Tickets
la funcion leer tickets toma cada elemento de la lista de ticket que es un diccionario
de cada diccionario toma la key numero_ticket hasta encontrar el valor del numero de ticket ingresado

