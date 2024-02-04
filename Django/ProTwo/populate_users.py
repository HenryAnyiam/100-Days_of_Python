#!/usr/bin/python3

from faker import Faker

import django

django.setup()

user_gen = Faker()

from first_app.models import User
for i in range(5):
    new_user = User(first_name=user_gen.first_name(),
                    last_name=user_gen.last_name(),
                    email=user_gen.email())
    new_user.save()