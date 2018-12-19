#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# conAcento.py
#  
#  Copyright 2018 Pedro Domingo Roman <historiadores@iMac-de-Pedro.local>
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



#  
import pdb
from subprocess import call
import random
import time


call("clear")

print('Este programa responderá si una palabra se escribe o no con acento.')
print('Por lo tanto, lo obvio... piense una palabra')
espera=raw_input("Cuando esté preparado, presione enter")

call("clear")

# Primeros datos

print("Primera pregunta: ¿es un adverbio terminado en 'mente', como:\n 'velozmente', 'sutilmente', etc?")
print(" presione 1 si la respuesta es 'Sí' o presione '0' si la respuesta es 'NO' ")

adverbio_terminado_en_mente=raw_input()

if adverbio_terminado_en_mente == 1:
	print("Considere de aquí en adelante solo la parte de la palabra que está antes de la terminación 'MENTE' ")

espera=raw_input("Cuando estés preparado, presiona enter")
call("clear")

enuncRespuesta = "La palabra se escribe con acento en la sílaba "
agudaConAcento = "La palabra se escribe con acento en la última sílaba."
agudaSinAcento = "Es una palabra aguda que se escribe sin acento!"
graveSinAcento = "Es una palabra grave que se escribe sin acento."
graveConAcento = "Es una palabra grave que se escribe con acento"
respuesta_esdrujula = " porque es esdrújula"

# primera categoría con acento
print("De ahora en adelante, use '1' como 'sí' y '0' como 'no'")
print('¿Tiene una vocal cerrada i o u tónica contigua a una vocal abierta?')
print("Tal como 'sería', 'caía', 'baúl', 'púa', 'búho', etc.!")
cerradaTonicaMasAbierta = int(input())
if cerradaTonicaMasAbierta == 1:
    print('La palabra se escribe con acento en la vocal cerrada.')
    print('No se haga más preguntas.')
elif cerradaTonicaMasAbierta == 0:
# Se determina si la palabra es grave, aguda o esdrújula

    print('¿Cuántas sílabas tiene esa palabra?')

    ndeSilabas = int(input())
    ndeSilabas_string = str(ndeSilabas)

    print('¿Cuál es la última letra de esa palabra?')
    print('Escríbela')

    letraFinal = raw_input()


    print('¿En qué sílaba se acentúa esta palabra?')

    silabaTonica = int(input())
    silabaTonica_string = str(silabaTonica)
  

  
    deltaTonicaFinal = ndeSilabas-silabaTonica
#  print(deltaTonicaFinal)
    if deltaTonicaFinal == 2:
        print(enuncRespuesta + silabaTonica_string + respuesta_esdrujula)

    if deltaTonicaFinal == 0:
        if letraFinal == "a":
            print(agudaConAcento)
        elif letraFinal == "e":
            print(agudaConAcento)
        elif letraFinal == "i":
            print(agudaConAcento)
        elif letraFinal == "o":
            print(agudaConAcento)
        elif letraFinal == "u":
            print(agudaConAcento)
        elif letraFinal == "n":
            print(agudaConAcento)
        elif letraFinal == "s":
            print(agudaConAcento)
        else:
            print(agudaSinAcento)

    if deltaTonicaFinal == 1:
        if letraFinal == "a":
            print(graveSinAcento)
        elif letraFinal == "e":
            print(graveSinAcento)
        elif letraFinal == "i":
            print(graveSinAcento)
        elif letraFinal == "o":
            print(graveSinAcento)
        elif letraFinal == "u":
            print(graveSinAcento)
        elif letraFinal == "n":
            print(graveSinAcento)
        elif letraFinal == "s":
            print(graveSinAcento)
        else:
            print(graveConAcento)
