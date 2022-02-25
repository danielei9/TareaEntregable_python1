#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Daniel Burruchaga Sola 2022
# All rights reserved.

# Flight Class 
# flight = Flight("Pedro", "Garcia", 1) #Instance

class Flight(): #Creamos la clase Flight
    def __init__(self, number, aircraft,seating):
        self.number = number 
        self.aircraft = aircraft 
        self.seating = seating 
# Definimos el metodo __str__
    def __str__(self):
        return ("number: " + self.number + " aircraft: " + self.aircraft + " seating: " + self.seating)
# Definimos el metodo passenger_data
    def get_number(self):
        return self.number
    def get_aircraft_model(self):
        return self.aircraft
    def allocate_passenger(self):
        return self.aircraft
    def num_available_seats(self):
        return self.aircraft
    def print_seating(self):
        return self.aircraft
    def print_boarding_cards(self):
        return self.aircraft
    def __parse_seat(self):
        return self.aircraft
    def __passenger_seats(self):
        return self.aircraft