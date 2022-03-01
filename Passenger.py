#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Daniel Burruchaga Sola 2022
# All rights reserved.

# Passenger Class 
# passenger = Passenger("Pedro", "Garcia", 1) #Instance

class Passenger(): #Creamos la clase Passenger
    """
    Representación de un Passenger
    Attributes:
      __name: Nombre de persona
      __surname: surname 
      __id_card: id card asignado
    Methods:
      passenger_data(): get data
    """
    def __init__(self, name, surname,id_card): #Definimos el atributo
        """ Inicializa un Passenger con sus datos"""

        self.__name = name # Definimos que el atributo name,sera el name asig
        self.__surname = surname # Definimos que el atributo surname, sera el surname asig
        self.__id_card = id_card # Definimos que el atributo id_card, sera el id_card asig
# Definimos el metodo __str__
    def __str__(self):
        return ("name: " + self.__name + " surname: " + self.__surname + " id_card: " + self.__id_card)
    # Definimos el metodo passenger_data
    
    def passenger_data(self):
        """
        --------------------------------------------------------
        Obtains the data of a passenger
        Returns:
        name: The passenger's name such as 'Jack'
        family_name: The passenger's family name such as 'Shephard'
        id_card: The passenger's id card such as '85994003S'
        --------------------------------------------------------
        """
        return (self.__name, self.__surname, self.__id_card)
