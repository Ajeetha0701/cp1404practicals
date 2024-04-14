from taxi import Taxi


def drive_and_print(taxi, distance):
    taxi.drive(distance)
    print(f"Taxi Details:\n{taxi}\nCurrent Fare: ${taxi.get_fare():.2f}")


my_taxi = Taxi("Prius 1", 100, 1.23)
drive_and_print(my_taxi, 40)
my_taxi.start_new_fare()
drive_and_print(my_taxi, 100)

