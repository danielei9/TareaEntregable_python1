#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Daniel Burruchaga Sola 2022
# All rights reserved.

# Flight Class 
# flight = Flight("Pedro", "Garcia", 1) #Instance

from ast import IsNot

class Flight(): #Creamos la clase Flight
    def __init__(self, number, aircraft):
        self.__number = number 
        self.__aircraft = aircraft 
        #self.__seating = self._aircraft.seating_plan()
        rows, seats = self.__aircraft.seating_plan()
        self.__seating = []
        self.__seating.append(None)
        for i in rows:  
          dictionary = dict()
          for letter in seats:
            dictionary[str(letter)] = None
          self.__seating.append(dictionary)
# Definimos el metodo __str__
    def __str__(self):
        return ("number: " + self.__number + " aircraft: " + self.__aircraft + " seating: " + self.__seating)
    
    """--------------------------------------------------------
    Allocate a seat to a passenger
    Args:
      seat: A seat designator such as '12C' or '21F'
      passenger: The passenger data such as ('Jack', 'Shephard', '85994003S')
    --------------------------------------------------------"""
    def allocate_passenger(self,seat,passenger):
        number = "" # number guarda el numero
        letter = '' # letter guarda la letra 
        number , letter = self.__parse_seat(seat)
        self.__seating[int(number)][letter] = passenger
        return 1 

    """--------------------------------------------------------
    Reallocate a passenger to a different seat
    Args:
      from_seat: The existing seat designator for the passenger such as '12C'
      to_seat: The new seat designator
    --------------------------------------------------------"""
    def reallocate_passenger(self,from_seat,to_seat):
        number_from , letter_from = self.__parse_seat(from_seat)
        number_to , letter_to = self.__parse_seat(to_seat)
       
        tmp_passenger_from =  self.__seating[int(number_from)][str(letter_from)]
        tmp_passenger_to =  self.__seating[int(number_to)][str(letter_to)]

        self.__seating[int(number_from)][str(letter_from)] = tmp_passenger_to
        self.__seating[int(number_to)][str(letter_to)] = tmp_passenger_from
        return 1 
    
    """--------------------------------------------------------
    Obtains the amount of unoccupied seats
    Returns:
      The number of unoccupied seats  
    --------------------------------------------------------"""    
    def num_available_seats(self):
      count = 0
      for dict in self.__seating:
        if dict is not None:
          for key in dict:
            if dict[key] == None:
              count += 1
      return count
    
    """--------------------------------------------------------
    Prints in console the seating plan
    Example of one row:
      {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}
    --------------------------------------------------------"""
    def print_seating(self):
      for dict in self.__seating:
          print(dict)     
      return 1    
    """--------------------------------------------------------
    Prints in console the boarding card for each passenger 
    Examen of one boarding card:
    ----------------------------------------------------------
    |     Jack Sheppard 85994003S 15E BA758 Airbus A319      |
    ----------------------------------------------------------
    --------------------------------------------------------"""
    def print_boarding_cards(self):
      res,seats = self.__passenger_seats()
      for i in range(1,len(res)):
        name, surname, id_card = res[i]
        print(name + " " + surname + " " + id_card + " " + seats[i] + " " + str( self.__aircraft ))
      return 1

    """--------------------------------------------------------
    Divide a seat designator in row and letter
    Args:
      seat: The seat designator to be divided such as '12C'
    Returns:
      row: The row of the seat such as 12
      letter: The letter of the seat such as 'C'
    --------------------------------------------------------"""
    def __parse_seat(self,seat):
      number = ""
      for digit in seat:
        if digit.isdigit():
          number += digit
        else: 
          letter = digit
      return number ,letter
    """--------------------------------------------------------
    A generator function to iterate the occupied seating locations
    Returns:
      generator: Tuple of the passenger data and the seat 
    --------------------------------------------------------"""
    def __passenger_seats(self):
      res = []
      count = 0
      seats = []

      for dictionary in self.__seating:
        count =+ 1 #
        if dictionary != None:
          for key in dictionary:
            if dictionary[key] != None:
              res.append(dictionary[key]) 
              seats.append(str(count)+str(key)) 
      return (res,seats)