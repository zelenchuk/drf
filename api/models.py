from django.db import models


class Profession(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class DataSheet(models.Model):
    description = models.CharField(max_length=200)
    historical_data = models.TextField()

    def __str__(self):
        return self.description


class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    profession = models.ManyToManyField(Profession)
    data_sheet = models.OneToOneField(DataSheet, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Document(models.Model):
    PP = 'PP'
    ID = 'ID'
    DOC_TYPES = (
        (PP, 'Passport'),
        (ID, 'Identity card'),
    )
    type = models.CharField(choices=DOC_TYPES, max_length=2)
    doc_number = models.CharField(max_length=50)
    document = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.doc_number
