#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Daniel Burruchaga Sola 2022
# All rights reserved.
#*----------------------------------------------------------------*
#*----------------------------------------------------------------*
#*----------------------------------------------------------------*
# Aircraft Class 
class Aircraft(): #Creamos la clase 
    """
    Representación de un Aircraft
    Attributes:
      __model: Modelo de avion
      __registration: registro 
      __num_rows: rows of plane
      __num_seats_per_row: num seat per row 
    Methods:
      get_registration():  get registration
      reallocate_passenger(from_seat,to_seat): reallocate passenger
      get_model(): gert model
      seating_plan(): Generates a seating plan for the number of rows and seats per row
      num_seats(): Calculates the number of seats
    """
    def __init__(self, registration,model,num_rows,num_seats_per_row): #Definimos el atributo
        self.__model = model # Definimos que el atributo name,sera el name asig
        self.__registration = registration # Definimos que el atributo name,sera el name asig
        self.__num_rows = num_rows # Definimos que el atributo surname, sera el surname asig
        self.__num_seats_per_row = num_seats_per_row # Definimos que el atributo id_card, sera el id_card asig   
    def __str__(self):
        return ( str(self.__registration) + " "+ str(self.__model) )
    """
    Definimos el metodo get_registration
    """
    def get_registration(self):
        return self.__registration

    """
    Definimos el metodo get_model
    """
    def get_model(self):
        return self.__model

    """Definimos el metodo seating_plan
        Generates a seating plan for the number of rows and seats per row
    Returns:
        rows: A list of rows: None, 1, 2, etc.
        seats: A string of letters such as 'ABCDEF'
 """
    def seating_plan(self):
        template = "ABCDEFGHJKLMÑOPQRSTUVWYZ"
        res = ""
        for i in range(int(self.__num_seats_per_row)): # TODO: this Change
            res += template[i]
        return range(1, self.__num_rows+1), res
    """
    Definimos el metodo num_seats
    Calculates the number of seats
    Returns:
    seats: The number of seats
    """
    def num_seats(self):
        rows, rowSeats = self.seating_plan()
        return len(rows) * len(rowSeats)
    def get_rows(self):
        """
        Definimos el metodo get_rows
        return: n rows
        """
        return self.__num_rows
#*----------------------------------------------------------------*
#*----------------------------------------------------------------*
#*----------------------------------------------------------------*
# Airbus Class 
# Airbus = Airbus() #Instance
class Airbus(Aircraft): #Creamos la clase Passenger
    """
    Representación de un Aircraft
    Attributes:
      __model: Modelo de avion
      __registration: registro 
      __num_rows: rows of plane
      __num_seats_per_row: num seat per row 
      __variant: variant
    Methods:
      get_registration():  get registration
      reallocate_passenger(from_seat,to_seat): reallocate passenger
      get_model(): gert model
      seating_plan(): Generates a seating plan for the number of rows and seats per row
      num_seats(): Calculates the number of seats
      get_variant(): get variant
    """
    def __init__(self,registration, variant): #Definimos el atributo
        """ Inicializa un Airbus con sus datos"""
        self.__model = "Airbus A319" # Definimos que el atributo __model,sera el __model asig
        self.__num_rows = 23 # Definimos que el atributo __num_rows, sera el __num_rows asig
        self.__num_seats_per_row = 6 # Definimos que el atributo __num_seats_per_row, sera el __num_seats_per_row asig
        self.__variant = variant # Definimos que el atributo __variant, sera el __variant asig
        super().__init__(registration,self.__model,self.__num_rows,self.__num_seats_per_row) 

# Definimos el metodo __str__
    def __str__(self):
        return ("Airbus variant: " + self.__variant + " num_seats_per_row: " + str(self.__num_seats_per_row) + " num_rows: " + str(self.__num_rows) + " model: " + self.__model)
    
    def get_variant(self):
        """
        Definimos el metodo passenger_data
        return: variant
        """
        return self.__variant
    
#*----------------------------------------------------------------*
#*----------------------------------------------------------------*
#*----------------------------------------------------------------*

# Boeing Class 
# Boeing = Airbus() #Instance
class Boeing(Aircraft): #Creamos la clase Passenger
    """
    Representación de un Aircraft
    Attributes:
      __model: Modelo de avion
      __registration: registro 
      __num_rows: rows of plane
      __num_seats_per_row: num seat per row 
      __variant: variant
    Methods:
      get_registration():  get registration
      reallocate_passenger(from_seat,to_seat): reallocate passenger
      get_model(): gert model
      seating_plan(): Generates a seating plan for the number of rows and seats per row
      num_seats(): Calculates the number of seats
      get_airline(): get airline
    """
    def __init__(self, registration,airline): #Definimos el atributo
        """ Inicializa un Boeing con sus datos"""
        self.__model = "Boeing 777" # Definimos que el atributo __model,sera el __model asig
        self.__num_rows = 56 # Definimos que el atributo __num_rows, sera el __num_rows asig
        self.__num_seats_per_row = 9 # Definimos que el atributo __num_seats_per_row, sera el __num_seats_per_row asig
        self.__airline = airline # Definimos que el atributo __airline, sera el __airline asig
        super().__init__(registration,self.__model,self.__num_rows,self.__num_seats_per_row) 

# Definimos el metodo __str__
    def __str__(self):
        return ("Boeing airline: " + self.__airline + " num_seats_per_row: " + str(self.__num_seats_per_row) + " num_rows: " + str(self.__num_rows) + " model: " + self.__model)
# Definimos el metodo passenger_data
   
    def get_airline(self):
        """
         Definimos el metodo get_airline
         return: airline
        """
        return self.__airline
#*----------------------------------------------------------------*
#*----------------------------------------------------------------*
#*----------------------------------------------------------------*
