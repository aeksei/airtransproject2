from django.db import models


# Create your models here.


class Booking(models.Model):
    book_ref = models.AutoField(primary_key=True)
    book_date = models.DateField()
    total_amount = models.FloatField(null=False)

    def __str__(self):
        return "{} - {}".format(self.book_ref,
                                self.book_date)


class Ticket(models.Model):
    ticket_no = models.AutoField(primary_key=True)
    book_ref = models.ForeignKey(Booking,
                                 on_delete=models.CASCADE)

    passenger_id = models.PositiveIntegerField(null=False)
    passenger_name = models.CharField(max_length=100)
    contact_data = models.CharField(max_length=100)

    def __str__(self):
        return "{} - {}".format(self.ticket_no,
                                self.passenger_name)


class Flight(models.Model):
    flight_id = models.PositiveIntegerField(primary_key=True)
    departure_airport = models.ForeignKey('Airport',
                                          related_name='departure_airport',
                                          on_delete=models.CASCADE)
    arrival_airport = models.ForeignKey('Airport',
                                        related_name='arrival_airport',
                                        on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.flight_id)


class TicketFlight(models.Model):
    ticket_no = models.ForeignKey(Ticket,
                                  on_delete=models.CASCADE)
    flight_id = models.ForeignKey(Flight,
                                  on_delete=models.CASCADE)

    class Meta:
        unique_together = (('ticket_no', 'flight_id'),)

    def __str__(self):
        return "{} - {}".format(self.ticket_no,
                                self.flight_id)


class Airport(models.Model):
    airport_code = models.CharField(max_length=4)
    airport_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=100)
    timezone = models.IntegerField()

#
# departure_airport__airport_code = 'DME'
# Flight.objects.all().filter(departure_airport__airport_code=departure_airport__airport_code)
# Flight.objects.all().filter(departure_airport__airport_code='LED')