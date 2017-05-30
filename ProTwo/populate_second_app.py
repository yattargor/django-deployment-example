import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

from AppTwo.models import User
from faker import Faker

fakegen = Faker()
#user = ['Userinfo1', 'Userinfo2', 'Userinfo3','Userinfo4','Userinfo5']

#def add_user():
#    u = User.objects.get_or_create(first_name=random.choice(user))[0]
#    u.save()
#    return u

def populate(N=5):
    for entry in range(N):
        #get the topic for the entry
        #useradd = add_user()

        #create fake data for the entry
        fake_name = fakegen.name().split()
        fake_firstname = fake_name[0]
        fake_lastname = fake_name[1]
        fake_email = fakegen.email()

        #create new entry in db
        userwb = User.objects.get_or_create(first_name= fake_firstname,
                                            last_name=fake_lastname,
                                            email=fake_email)[0]

if __name__ == '__main__':
    print("populating db!")
    populate(20)
    print("Populating complete!")
