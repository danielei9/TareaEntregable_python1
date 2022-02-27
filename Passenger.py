#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Daniel Burruchaga Sola 2022
# All rights reserved.

# Passenger Class 
# passenger = Passenger("Pedro", "Garcia", 1) #Instance

class Passenger(): #Creamos la clase Passenger
    def __init__(self, name, surname,id_card): #Definimos el atributo
        self.__name = name # Definimos que el atributo name,sera el name asig
        self.__surname = surname # Definimos que el atributo surname, sera el surname asig
        self.__id_card = id_card # Definimos que el atributo id_card, sera el id_card asig
# Definimos el metodo __str__
    def __str__(self):
        return ("name: " + self.__name + " surname: " + self.__surname + " id_card: " + self.__id_card)
    # Definimos el metodo passenger_data
    """--------------------------------------------------------
    Obtains the data of a passenger
    Returns:
      name: The passenger's name such as 'Jack'
      family_name: The passenger's family name such as 'Shephard'
      id_card: The passenger's id card such as '85994003S'
    --------------------------------------------------------"""
    def passenger_data(self):
        return (self.__name, self.__surname, self.__id_card)
