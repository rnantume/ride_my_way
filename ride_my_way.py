#Encapsulation
class Users:
    def __init__(self, user_id, name, phone):
    # Private attributes
        self._user_id = user_id
        self._name = name
        self._phone = phone

     # Public methods to access private attribute
    def get_name(self):
        return self._name
    
    def get_phone(self):
        return self._phone
    
#Inheritance: sub class drivers fron superclass Users   
class Driver(Users):
    def __init__(self, user_id, name, phone, driver_rating):
        super().__init__(user_id, name, phone)
        self.driver_rating = driver_rating

#Inheritance: sub class passenger from super class Users
class Passenger(Users):
    def __init__(self, user_id, name, phone, language_preference, passenger_rating):
        super().__init__(user_id, name, phone)
        self.language_preference = language_preference
        self.passenger_rating = passenger_rating

allRides = []
allrequests = []

# Abstraction: the Ride class hides ride data and provides methods to interact with it
class Ride:
    def __init__(self, ride_id, date, licenseNo, fro, destination, time, fare, seats_available):
        self.ride_id = ride_id
        self.date = date
        self.licenseNo = licenseNo
        self.fro = fro
        self.destination = destination
        self.time = time
        self.fare = fare
        self.seats_available = seats_available

    def add_ride(self):
        ride = {
            "id": self.ride_id,
            "date": self.date,
            "licenseNo": self.licenseNo, 
            "fro": self.fro,
            "destination": self.destination,
            "time": self.time,
            "fare": self.fare,
            "seats_available": self.seats_available
        }
        allRides.append(ride)
        return ride
    
    def get_rides():
        if allRides:
            return allRides
        return "No ride offers found"

    def get_a_ride(ride_id):
        for ride in allRides:
            if ride['id'] == ride_id and ride['seats_available'] > 0:
                return ride
        return "Ride with that ID not found"

class Requests:
    def __init__(self, request_id, user_id, ride_id):
        self.request_id = request_id
        self.user_id = user_id
        self.ride_id = ride_id
        self.status = "pending"

    def create_request(self):
        request = {
            "id": self.request_id,
            "user_id": self.user_id,
            "ride_id": self.ride_id,
            "status": self.status
        }
        allrequests.append(request)
        return request

    def get_requests():
        if allrequests:
            return allrequests
        return "No ride requests found"
        
    def get_request(request_id):
        for request in allrequests:
            if request["id"] == request_id:
                return request
        return "Sorry, request not found"
    
# Creating driver, passenger, ride and ride request objects
driver1 = Driver(user_id=1, name="Racheal Bantu", phone="0750-000-000", driver_rating=4.5)
passenger1 = Passenger(user_id=2, name="Mark Ooja", phone="0788-999-111", language_preference="Alur",passenger_rating=2)

ride1 = Ride(
    ride_id=101,
    date="2024-10-08",
    licenseNo="UBG123X",
    fro="8th Street",
    destination="Jinja",
    time="10:00 AM",
    fare=25000,
    seats_available=3,
)

# Polymorphism: Same method name of add_ride() is used to add multiple rides
# Driver adds a ride 
ride1.add_ride()

# Shows number and list of all ride offers
print(f"-----------------------------")
print(f"")
print(f"{len(Ride.get_rides())} Ride(s) Available: {Ride.get_rides()}")

# Passenger makes a request
request1 = Requests(request_id=201, user_id=passenger1._user_id, ride_id=ride1.ride_id)
request1.create_request()

# Shows all ride requests
print(f"{len(Requests.get_requests())} Ride(s) Requests Found: {Requests.get_requests()}")

# Shows a specific ride offer 
ride_search = Ride.get_a_ride(101)
print(f"Ride from {ride_search["fro"]} heading to {ride_search["destination"]} found by Driver: {driver1.get_name()}!")

# Shows a specific ride request and passenger who requested it by id
request_search = Requests.get_request(201)
print(f"Request No: {request_search["id"]} requested by passenger ID: {request_search['user_id']}, contact:{passenger1.get_phone()} found!")
print(f"")
print(f"-----------------------------")
