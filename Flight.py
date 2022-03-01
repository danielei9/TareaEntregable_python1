#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Daniel Burruchaga Sola 2022
# All rights reserved.

# Flight Class 
# flight = Flight("Pedro", "Garcia", 1) #Instance

from ast import IsNot
from ctypes import sizeof

class Flight(): #Creamos la clase Flight
    """
    Representación de un vuelo
    Attributes:
      number: numero de vuelo
      aircraft: tipo de avion
      seating: plan de asientos []

    Methods:
      allocate_passenger(seat,passenger): alojar pasajero
      reallocate_passenger(from_seat,to_seat): realojar pasajero
      num_available_seats(): Return number of available
      print_seating(): printear asientos 
      print_boarding_cards(): printear carta de abordo
      __parse_seat(seat): Divide a seat designator in row and letter
      __passenger_seats(self):A generator function to iterate the occupied seating locations

    """
    def __init__(self, number, aircraft):
        """ Inicializa un Flight con sus datos"""
        if (type(number[0]) == type("A") and type(number[1]) == type("A") ):
          self.__number = number 
        else: 
          raise ValueError('Number index 1 and 2 must be a character ')
        if(number[0]>='A'and number[0]<='Z'):
          self.__number = number 
        else: 
          raise ValueError('char at 1 Is not a capital letter')
        if(number[1]>='A'and number[1]<='Z'):
          self.__number = number 
        else:
          raise ValueError('char at 2 Is not a capital letter')
        if(int(number[2:len(number)]) > 9999):
          raise ValueError('should put less than 9999 values in number')
        else: 
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
    
    
    def allocate_passenger(self,seat,passenger):
        """
        --------------------------------------------------------
        Allocate a seat to a passenger
        Attributes:
        seat: A seat designator such as '12C' or '21F'
        passenger: The passenger data such as ('Jack', 'Shephard', '85994003S')
        --------------------------------------------------------
        """
        number = "" # number guarda el numero
        letter = '' # letter guarda la letra 
        number , letter = self.__parse_seat(seat)
        if ( self.__seating[int(number)][str(letter)] == None):  
          self.__seating[int(number)][letter] = passenger
        else:
          raise ValueError('Occupied seat')     
        return 1 

    
    def reallocate_passenger(self,from_seat,to_seat):
        """--------------------------------------------------------
        Reallocate a passenger to a different seat
        Attributes:
        from_seat: The existing seat designator for the passenger such as '12C'
        to_seat: The new seat designator
        --------------------------------------------------------
        """
        
        number_from , letter_from = self.__parse_seat(from_seat)
        number_to , letter_to = self.__parse_seat(to_seat)
        if ( self.__seating[int(number_from)][str(letter_from)] != None):  
          raise ValueError('NOT Occupied seat')   
        else:
          tmp_passenger_from =  self.__seating[int(number_from)][str(letter_from)]
          tmp_passenger_to =  self.__seating[int(number_to)][str(letter_to)]
          self.__seating[int(number_from)][str(letter_from)] = tmp_passenger_to
          self.__seating[int(number_to)][str(letter_to)] = tmp_passenger_from
          return 1 

    
       
    def num_available_seats(self):
      """--------------------------------------------------------
      Obtains the amount of unoccupied seats
      Returns:
      The number of unoccupied seats  
      --------------------------------------------------------
      """ 
      count = 0
      for dict in self.__seating:
        if dict is not None:
          for key in dict:
            if dict[key] == None:
              count += 1
      return count
    
   
    def print_seating(self):
      """
      --------------------------------------------------------
      Prints in console the seating plan
      Example of one row:
      {'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None}
      --------------------------------------------------------
    """
      for dict in self.__seating:
          print(dict)     
      return 1    
    
    def print_boarding_cards(self):
      """
      --------------------------------------------------------
      Prints in console the boarding card for each passenger 
      Examen of one boarding card:
       ----------------------------------------------------------
      |     Jack Sheppard 85994003S 15E BA758 Airbus A319      |
      ----------------------------------------------------------
      --------------------------------------------------------
      """
      res,seats = self.__passenger_seats()
      for i in range(1,len(res)):
        name, surname, id_card = res[i]
        print(name + " " + surname + " " + id_card + " " + seats[i] + " " + str( self.__aircraft ))
      return 1

    
    def __parse_seat(self,seat):
      """--------------------------------------------------------
      Divide a seat designator in row and letter
      Attributes:
      seat: The seat designator to be divided such as '12C'
      Returns:
      row: The row of the seat such as 12
      letter: The letter of the seat such as 'C'
      --------------------------------------------------------"""
      number = ""
      numberInt = 777
      for digit in seat:
        if digit.isdigit():
          number += digit
        else: 
          letter = digit
      model = self.__aircraft.get_model()
      if(model == "Airbus A319"):
        maxLetter = 'F'
      elif(model == "Boeing 777"):
        maxLetter = 'I'
      else:
        raise ValueError('You must assign a valid model')     
      if(letter > maxLetter):
        raise ValueError('This model cant take this letter')     
      numberInt = number
      try:
        if (type(int(numberInt)) != type(1)):
          raise ValueError('You must put Letter + numbers')
      except:
          raise ValueError('You must put Letter + numbers')
      if( int(self.__aircraft.get_rows()) <=  int(number)):
        raise ValueError('We  cannot use this number of rows in the plane')     
      return number ,letter
    
    def __passenger_seats(self):
      """--------------------------------------------------------
    A generator function to iterate the occupied seating locations
    Returns:
      generator: Tuple of the passenger data and the seat 
    --------------------------------------------------------"""
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