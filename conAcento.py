#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  usocomas.py
#  
#  Copyright 2018 imac <imac@iMac-de-imac.local>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


# Algoritmo para decidir si una palabra se escribe con o sin acento
# Solo resuelve casos relacionados con leyes generales

print('Este programa el dará la respuesta a su pregunta \n si una palabra se escribe o no con acento.')


# Primeros datos


print('¿Cuántas sílabas tiene esa palabra?')

ndeSilabas = int(input())

ndeSilabas_string = str(ndeSilabas)

inic_01 ="La palabra tiene "

fin_01 = " sílabas"

print(inic_01 + ndeSilabas_string + fin_01)



print('¿Cuál es la última letra de esa palabra?')

print('Use comillas, por favor; por ejemplo, "m" ')

letraFinal = input()

enuncRespuesta = "La palabra se escribe con acento en la sílaba "


# primera categoría con acento
print("De ahora en adelante, use '1' como 'sí' y '0' como 'no'")
print('¿Tiene una vocal cerrada i o u tónica contigua a una vocal abierta?')
print("Tal como 'sería', 'caía', 'baúl', 'púa', 'búho', etc.!")
cerradaTonicaMasAbierta = int(input())
if cerradaTonicaMasAbierta == 1:
  print('La palabra se escribe con acento en la vocal cerrada.')
  print('No se haga más preguntas. El caso está resuelto.')
elif cerradaTonicaMasAbierta == 0:
# Se determina si la palabra es grave, aguda o esdrújula
  print('¿En qué sílaba se acentúa esta palabra?')
  silabaTonica = int(input())
  
  silabaTonica_string = str(silabaTonica)
  
  respuesta_esdrujula = " porque es esdrújula"
  
  deltaTonicaFinal = ndeSilabas-silabaTonica
#  print(deltaTonicaFinal)
  if deltaTonicaFinal == 2:
    print(enuncRespuesta + silabaTonica_string + respuesta_esdrujula)

  if deltaTonicaFinal == 0:
    if letraFinal == "a":
        print('La palabra se escribe con acento en la última sílaba.')
    elif letraFinal == "e":
        print('La palabra se escribe con acento en la última sílaba.')
    elif letraFinal == "i":
        print('La palabra se escribe con acento en la última sílaba.')
    elif letraFinal == "o":
        print('La palabra se escribe con acento en la última sílaba.')
    elif letraFinal == "u":
        print('La palabra se escribe con acento en la última sílaba.')
    elif letraFinal == "n":
        print('La palabra se escribe con acento en la última sílaba.')
    elif letraFinal == "s":
      print('La palabra se escribe con acento en la última sílaba.')
    else:
      print('Es una palabra aguda que se escribe sin acento!')

  if deltaTonicaFinal == 1:
    if letraFinal == "a":
      print('Es una palabra grave que se escribe sin acento.')
    elif letraFinal == "e":
      print('Es una palabra grave que se escribe sin acento.')
    elif letraFinal == "i":
      print('Es una palabra grave que se escribe sin acento.')
    elif letraFinal == "o":
      print('Es una palabra grave que se escribe sin acento.')
    elif letraFinal == "u":
      print('Es una palabra grave que se escribe sin acento.')
    elif letraFinal == "n":
      print('Grave que se escribe sin acento.')
    elif letraFinal == "s":
      print('Es una palabra grave que se escribe sin acento.')
    else:
      print('Es una palabra grave que se escribe con acento.')
