import pytest
from Aircraft import Aircraft, Boeing, Airbus
from Flight import Flight
from Passenger import Passenger

@pytest.fixture
def air():
    return Aircraft("G-EUAH", "Airbus A319", 22, 6)

# test_allocate_passenger
@pytest.mark.parametrize("seat, passenger_data", [("12A", ("Jack", "Shephard", "85994003S")), ("18F", ("Kate", "Austen", "12589756P")), ("18E", ("James", "Ford", "56278665F"))])

def test_allocate_passenger_invalid():
    flight = Flight("BA117", aircraft.Aircraft("G-EUAH", "Airbus A319", 22, 6))
    flight.allocate_passenger("12A", ("Jack", "Shephard", "85994003S"))
    with pytest.raises(ValueError) as exc:
        flight.allocate_passenger("12A", ("Jack", "Shephard", "85994003S"))
    assert "Asiento no disponible" == str(exc.value)

@pytest.mark.parametrize("numero, aircraft", [("BA117", Aircraft("G-EUAH", "Airbus A319", 22, 6)), ("AF92", Boeing("F-GSPS", "Emirates")), ("BA148", Airbus("G-EUPT", "A319-100"))])
def test_init_invalid_min():
    with pytest.raises(ValueError) as exc:
        Flight("BA10222", air)
    assert "Error en el número de vuelo. A partir del segundo caracter, debe de ser un número que 9999" == str(exc.value)

def test_init_invalid_letter():
    with pytest.raises(ValueError) as exc:
        Flight("B1222", air)
    assert "Error en el número de vuelo. Los dos primeros caracteres deben de ser letras" == str(exc.value)

def test_init_valid(numero, aircraft):
    assert Flight(numero, aircraft)

def test_init_invalid_min():
    with pytest.raises(ValueError) as exc:
        Flight("bA222", air)
    assert "Error en el número de vuelo. Los dos primeros caracteres deben de estar en mayúscula" == str(exc.value)

#  rellocate_passenger()
@pytest.mark.parametrize("seat, passenger_data", [("12A", ("Jack", "Shephard", "85994003S")), ("18F", ("Kate", "Austen", "12589756P")), ("18E", ("James", "Ford", "56278665F"))])
def test_rellocate_passenger(seat, passenger_data):
    flight = Flight("BA117", aircraft.Aircraft("G-EUAH", "Airbus A319", 22, 6))
    flight.allocate_passenger(seat, passenger_data)
    flight.reallocate_passenger(seat, "4D")
    data = flight.get_seating()
    assert data[4]["D"] == passenger_data

#  test_rellocate_passenger_invalid()
def test_rellocate_passenger_invalid():
    flight = Flight("BA117", aircraft.Aircraft("G-EUAH", "Airbus A319", 22, 6))
    with pytest.raises(ValueError) as exc:
        flight.reallocate_passenger("4D", "1D")
    assert "El asiento a reasignar no tiene pasajero" == str(exc.value)

#  test_num_available_seats
@pytest.mark.parametrize("seat, passenger_data", [("12A", ("Jack", "Shephard", "85994003S")), ("18F", ("Kate", "Austen", "12589756P")), ("18E", ("James", "Ford", "56278665F"))])
def test_num_available_seats(seat, passenger_data):
    flight = Flight("BA117", aircraft.Aircraft("G-EUAH", "Airbus A319", 22, 6))
    assert flight is not None 
    flight.allocate_passenger(seat, passenger_data)
    num_seats2 = flight.num_available_seats()
    assert num_seats2 == 125


def test_allocate_passenger(seat, passenger_data):
    flight = Flight("BA117", aircraft.Aircraft("G-EUAH", "Airbus A319", 22, 6))
    assert flight is not None 
    num_seats = flight.num_available_seats()
    flight.allocate_passenger(seat, passenger_data)
    num_seats2 = flight.num_available_seats()
    assert num_seats2 == (num_seats - 1)
