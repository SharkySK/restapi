from django.db import models


class Test(models.Model):
    uid_Tag = models.CharField(max_length=20)
    auth = models.BooleanField()


class Bridge(models.Model):
    bridge_Name = models.CharField(max_length=50)
    pairing_Key = models.CharField(max_length=20)


class Opening_hours(models.Model):
    opt_Name = models.CharField(max_length=20)
    opt_Week = models.BooleanField()
    opt_Evening = models.BooleanField()
    opt_Time = models.DurationField()


class Billing_opt(models.Model):
    default_Tax = models.IntegerField()
    invoice_Prefix = models.CharField(max_length=20)
    invoice_Deadline = models.DateField()
    invoice_Header = models.TextField()
    invoice_Footer = models.TextField()
    card_Statement = models.TextField()


class Booking_opt(models.Model):
    booking_Allows = models.BooleanField()
    booking_Advance = models.TimeField()
    booking_Limit = models.IntegerField()
    booking_Overwrite = models.TimeField()
    booking_Refund = models.BooleanField()
    booking_Lock = models.IntegerField()
    booking_Info = models.TextField()


class Package_opt(models.Model):
    package_Name = models.CharField(max_length=30)
    package_Describ = models.CharField(max_length=50)
    package_Note = models.TextField()
    package_Price_Reccuring = models.IntegerField()
    package_Price_Onetime = models.IntegerField()
    package_duration = models.DateField()
    package_Cancelation = models.BooleanField()
    package_Booking = models.BooleanField()
    package_Access_Rules = models.IntegerField()


class Facility(models.Model):
    facility_Name = models.CharField(max_length=50, null=False)
    invite_New = models.BooleanField()
    currency = models.CharField(max_length=50)
    data_Retention = models.DateField()

    # Foreign Keys

    billing_Opt = models.ForeignKey(Billing_opt, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    opening_Hours = models.ForeignKey(Opening_hours, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    booking_Opt = models.ForeignKey(Booking_opt, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    package_Opt = models.ForeignKey(Package_opt, on_delete=models.SET_NULL, null=True, blank=True, default=None)

    # Contact info

    contact_Email = models.EmailField()
    contact_Website = models.CharField(max_length=50)
    contact_Phone = models.IntegerField()


class Training(models.Model):
    training_Name = models.CharField(max_length=20)
    note = models.TextField()


class Equipment(models.Model):
    # Basic info

    equipment_Name = models.CharField(max_length=50)
    equipment_Desc = models.TextField()
    equipment_Fee = models.IntegerField()
    power_Consumption = models.IntegerField()
    busy_Time = models.TimeField()
    idle_Time = models.TimeField()
    require_Training = models.BooleanField()
    visible = models.BooleanField()

    # Booking specification

    bookable = models.BooleanField()
    booking_Fee = models.IntegerField()
    booking_Granul = models.TimeField()

    # Foreign Key

    equipment_Bridge = models.ForeignKey(Bridge, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    training = models.ManyToManyField(Training)


class User_account(models.Model):
    # Basic info
    role = models.BooleanField()
    first_Name = models.CharField(max_length=20)
    last_Name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    phone = models.IntegerField()
    date_Birth = models.DateField()
    Company = models.CharField(max_length=20)
    note = models.TextField()
    tax_Exempt = models.BooleanField()
    uid_Tag = models.IntegerField()

    # Adress info

    address = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    zip_Code = models.IntegerField()
    country = models.CharField(max_length=20)
    region = models.CharField(max_length=20)

    # Foreign Key section

    billing_Opt = models.ForeignKey(Billing_opt, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    training = models.ForeignKey(Training, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    package_Opt = models.ForeignKey(Package_opt, on_delete=models.SET_NULL, null=True, blank=True, default=None)


class Activity_log(models.Model):
    log_Date = models.DateTimeField()
    log_Time = models.TimeField()
    log_Equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    log_User = models.ForeignKey(User_account, on_delete=models.SET_NULL, null=True, blank=True, default=None)


class Booking_schedule(models.Model):
    booking_Start = models.DateTimeField()
    booking_End = models.DateTimeField()
    booking_Equipment = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    booking_User = models.ForeignKey(User_account, on_delete=models.SET_NULL, null=True, blank=True, default=None)
