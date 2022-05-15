from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    genderChoice = [ 
        ('Male',"Male"),
        ('Female',"Female")
    ]

    maritialStatusChoice = [ 
        ('Single','Single'),
        ('Married','Married'),
        ('Divorced','Divorced'),
        ('Seperated','Seperated'),
        ('Widowed','Widowed')
    ]

    states = [
        ("No_State","NA"),
        ("Alabama","AL"),
        ("Alaska","AK"),
        ("Arizona","AZ"),
        ("Arkansas","AR"),
        ("California","CA"),
        ("Colorado","CO"),
        ("Connecticut","CT"),
        ("Delaware","DE"),
        ("District of Columbia","DC"),
        ("Florida","FL"),
        ("Georgia","GA"),
        ("Hawaii","HI"),
        ("Idaho","ID"),
        ("Illinois","IL"),
        ("Indiana","IN"),
        ("Iowa","IA"),
        ("Kansas","KS"),
        ("Kentucky","KY"),
        ("Louisiana","LA"),
        ("Maine","ME"),
        ("Maryland","MD"),
        ("Massachusetts","MA"),
        ("Michigan","MI"),
        ("Minnesota","MN"),
        ("Mississippi","MS"),
        ("Missouri","MO"),
        ("Montana","MT"),
        ("Nebraska","NE"),
        ("Nevada","NV"),
        ("New Hampshire","NH"),
        ("New Jersey","NJ"),
        ("New Mexico","NM"),
        ("New York","NY"),
        ("North Carolina","NC"),
        ("North Dakota","ND"),
        ("Ohio","OH"),
        ("Oklahoma","OK"),
        ("Oregon","OR"),
        ("Pennsylvania","PA"),
        ("Rhode Island","RI"),
        ("South Carolina","SC"),
        ("South Dakota","SD"),
        ("Tennessee","TN"),
        ("Texas","TX"),
        ("Utah","UT"),
        ("Vermont","VT"),
        ("Virginia","VA"),
        ("Washington","WA"),
        ("West Virginia","WV"),
        ("Wisconsin","WI"),
        ("Wyoming","WY")
        
    ]
    following = models.ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False
    )
    birthDate = models.DateField(null = True, blank=True)
    email = models.EmailField(max_length=254)
    website = models.URLField(max_length = 200, blank=True)
    phoneNumber = models.CharField(max_length=12, blank=True)
    country = models.CharField(max_length=50,blank=True)
    state = models.CharField(default="NA",max_length=20,choices=states)
    city = models.CharField(max_length=50,blank=True)
    description = models.TextField(blank=True)
    birthPlace = models.TextField(blank=True)
    gender = models.CharField(max_length=6, choices=genderChoice,default="Male")
    occupation = models.TextField(blank=True)
    maritialStatus = models.CharField(max_length=9, choices=maritialStatusChoice, default="Single")
    profileImage = models.ImageField(null = True,blank = True,upload_to='static/user_profile_page_settings/profileImages/')
    backgroundImage = models.ImageField(null = True,blank = True,upload_to='static/user_profile_page_settings/profileImages/')
    facebookAccount = models.URLField(blank=True)

    def __str__(self) -> str:
        return str(self.id) + '_' + self.first_name + '_' + self.last_name
