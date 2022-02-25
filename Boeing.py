#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Daniel Burruchaga Sola 2022
# All rights reserved.

# Passenger Class 
# passenger = Passenger("Pedro", "Garcia", 1) #Instance

class Boeing(): #Creamos la clase Passenger
    def __init__(self, airline=""): #Definimos el atributo
        self.model = "Boeing 777" # Definimos que el atributo name,sera el name asig
        self.num_rows = 56 # Definimos que el atributo surname, sera el surname asig
        self.num_seats_per_row = 9 # Definimos que el atributo id_card, sera el id_card asig
        self.airline = airline # Definimos que el atributo id_card, sera el id_card asig
# Definimos el metodo __str__
    def __str__(self):
        return ("airline: " + self.airline + " num_seats_per_row: " + self.num_seats_per_row + " num_rows: " + self.num_rows + " model: " + self.model)
# Definimos el metodo passenger_data
    def get_airline(self):
        return self.airline
