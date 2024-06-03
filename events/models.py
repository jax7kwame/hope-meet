from django.db import models
from custom_user.models import User
from phone_field import PhoneField
from datetime import date, datetime
from tinymce.models import HTMLField



# events category model
class EventCategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    svg = models.TextField(blank=True, default="<svg xmlns='http://www.w3.org/2000/svg' width='40' fill='currentColor' class='bi bi-calendar4-event' viewBox='0 0 16 16'><path d='M3.5 0a.5.5 0 0 1 .5.5V1h8V.5a.5.5 0 0 1 1 0V1h1a2 2 0 0 1 2 2v11a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V3a2 2 0 0 1 2-2h1V.5a.5.5 0 0 1 .5-.5M2 2a1 1 0 0 0-1 1v1h14V3a1 1 0 0 0-1-1zm13 3H1v9a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1z'/><path d='M11 7.5a.5.5 0 0 1 .5-.5h1a.5.5 0 0 1 .5.5v1a.5.5 0 0 1-.5.5h-1a.5.5 0 0 1-.5-.5z'/></svg>")

    def __str__(self):
        return self.title
    

    class Meta:
        ordering=("-title",) 
        verbose_name_plural = "Categories"


# Venue type model
class VenueType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

# Venue modes
class Venue(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    image1 = models.ImageField(upload_to='uploads/venue', blank=True, null= True)
    image2 = models.ImageField(upload_to='uploads/venue', blank=True, null= True)
    image3 = models.ImageField(upload_to='uploads/venue', blank=True, null= True)
    type = models.CharField('Venue type', max_length=100, blank=True)
    venue_type = models.ForeignKey(VenueType, related_name="venue_types", blank=True, null=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    email = models.EmailField(blank=True)
    website_url = models.URLField(blank=True)
    fb_link = models.CharField('facebook link', max_length=255, blank=True)
    ig_link = models.CharField('instagram link', max_length=255, blank=True)
    x_link = models.CharField('x link', max_length=255, blank=True)
    description = HTMLField()
    created_by = models.IntegerField(blank=False, default=1)

    def __str__(self):
        return self.name


class ChurchOrGroup(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    logo = models.ImageField(upload_to='uploads/group_logos', blank=True)
    website_url = models.URLField(blank=True)
    fb_link = models.CharField('facebook link', max_length=255, blank=True)
    ig_link = models.CharField('instagram link', max_length=255, blank=True)
    x_link = models.CharField('x link', max_length=255, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)

# county
class County(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        ordering=("name",) 
        verbose_name_plural = "Counties"


# events model table
class Event(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to='uploads/events', blank=True)
    category = models.ForeignKey(EventCategory, related_name="events", null=True, on_delete=models.SET_NULL)
    
    starting_date = models.DateField()
    ending_date = models.DateField(blank=True, null=True)
    starting_time = models.TimeField(auto_now=False, auto_now_add=False)
    church_or_group = models.ForeignKey(ChurchOrGroup, related_name='events', null=True, on_delete=models.SET_NULL)

    district = models.CharField(max_length=100)
    conference = models.CharField(max_length=100)
    description = HTMLField()
    venue = models.ForeignKey(Venue, blank=True, related_name="events", null=True, on_delete=models.SET_NULL)
    location = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    county_local = models.ForeignKey(County, blank=True, null=True, related_name="events", on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    featured = models.BooleanField(default=False)
    post_event = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)


    def __str__(self):
        return self.title
    
    @property
    def remaining_days(self):
        d1 = datetime.strptime(str(self.starting_date), "%Y-%m-%d")
        d2 = datetime.now()
        days_till = d1 - d2

        if int(days_till.days) > 0:
            return f"({days_till.days} days remaining)"
        elif int(days_till.days) == 0:
            return "(today)"
        else:
            return "(Passed)"
    @property
    def days_till(self):
        d1 = datetime.strptime(str(self.starting_date), "%Y-%m-%d")
        d2 = datetime.now()
        days_to = int((d1 - d2).days)

        return days_to

    @property
    def event_duration(self):
        if self.ending_date:
            d1 = datetime.strptime(str(self.starting_date), "%Y-%m-%d")
            d2 = datetime.strptime(str(self.ending_date), "%Y-%m-%d")

            duration = int((d2 - d1).days) + 1

            if duration > 1:
                return f"{duration} days event"
            elif duration == 1:
                return f"{duration} day event"
            else:
                return "duration not defined"
        else:
            return "1 day event"



