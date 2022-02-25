#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Daniel Burruchaga Sola 2022
# All rights reserved.

# Passenger Class 
# passenger = Passenger("Pedro", "Garcia", 1) #Instance

class Passenger(): #Creamos la clase Passenger
    def __init__(self, name, surname,id_card): #Definimos el atributo
        self.name = name # Definimos que el atributo name,sera el name asig
        self.surname = surname # Definimos que el atributo surname, sera el surname asig
        self.id_card = id_card # Definimos que el atributo id_card, sera el id_card asig
# Definimos el metodo __str__
    def __str__(self):
        return ("name: " + self.name + " surname: " + self.surname + " id_card: " + self.id_card)
# Definimos el metodo passenger_data
    def passenger_data(self):
        return self
