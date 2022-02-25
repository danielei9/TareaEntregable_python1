#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Daniel Burruchaga Sola 2022
# All rights reserved.

# Flight Class 
# flight = Flight("Pedro", "Garcia", 1) #Instance

class Flight(): #Creamos la clase Flight
    def __init__(self, number, aircraft):
        self.number = number 
        self.aircraft = aircraft 
        self.seating = seating 
        #rows, seats = self._aircraft.seating_plan()
# Definimos el metodo __str__
    def __str__(self):
        return ("number: " + self.number + " aircraft: " + self.aircraft + " seating: " + self.seating)
 """
   Allocate a seat to a passenger
    Args:
      seat: A seat designator such as '12C' or '21F'
      passenger: The passenger data such as ('Jack', 'Shephard', '85994003S')
    """
    def allocate_passenger(self):
        return self.aircraft

    """Reallocate a passenger to a different seat
    Args:
      from_seat: The existing seat designator for the passenger such as '12C'
      to_seat: The new seat designator
    """
    def reallocate_passenger(self):
        return self.aircraft
    
    """Obtains the amount of unoccupied seats
    Returns:
      The number of unoccupied seats  
    """    
    def num_available_seats():
        return self.aircraft
    
    """Prints in console the seating plan
    Example of one row:
      {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}
    """
    def print_seating(self):
        return self.aircraft
    
    """Prints in console the boarding card for each passenger 
    Examen of one boarding card:
    ----------------------------------------------------------
    |     Jack Sheppard 85994003S 15E BA758 Airbus A319      |
    ----------------------------------------------------------
    """
    def print_boarding_cards(self):
        return self.aircraft

    """Divide a seat designator in row and letter
    Args:
      seat: The seat designator to be divided such as '12C'
    Returns:
      row: The row of the seat such as 12
      letter: The letter of the seat such as 'C'
    """
    def __parse_seat(self):
        row_numbers, seat_letters = self._aircraft.seating_plan()
        return self.aircraft
    """A generator function to iterate the occupied seating locations
    Returns:
      generator: Tuple of the passenger data and the seat 
    """
    def __passenger_seats(self):
        return self.aircraft