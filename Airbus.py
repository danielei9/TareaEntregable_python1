#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Daniel Burruchaga Sola 2022
# All rights reserved.

# Passenger Class 
# passenger = Passenger("Pedro", "Garcia", 1) #Instance

class Airbus(): #Creamos la clase Passenger
    def __init__(self, variant=""): #Definimos el atributo
        self.model = "Airbus A319" # Definimos que el atributo name,sera el name asig
        self.num_rows = 23 # Definimos que el atributo surname, sera el surname asig
        self.num_seats_per_row = 6 # Definimos que el atributo id_card, sera el id_card asig
        self.variant = variant # Definimos que el atributo id_card, sera el id_card asig
# Definimos el metodo __str__
    def __str__(self):
        return ("variant: " + self.variant + " num_seats_per_row: " + self.num_seats_per_row + " num_rows: " + self.num_rows + " model: " + self.model)
# Definimos el metodo passenger_data
    def get_variant(self):
        return self.variant
