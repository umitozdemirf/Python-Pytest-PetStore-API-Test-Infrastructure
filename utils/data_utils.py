import json
import random

from faker import Faker


class DataUtils:

    @staticmethod
    def generate_name():
        return Faker().name()

    @staticmethod
    def generate_description():
        return Faker().paragraph(nb_sentences=5, variable_nb_sentences=False)

    @staticmethod
    def generate_title():
        return Faker().word()

    @staticmethod
    def generate_random_integer(min_int, max_int):
        return Faker().random.randint(min_int, max_int)

    @staticmethod
    def generate_pet_body(status):
        pet = json.load(open('../model/data/pet_body.json'))

        pet.update({"id": DataUtils.generate_random_integer(5000, 5030035)})
        pet.update({"category": {
            "id": DataUtils.generate_random_integer(5000, 5030035),
            "name": DataUtils.generate_name()
        }})
        pet.update({"name": DataUtils.generate_name()})
        pet.update({"photoUrls": [
            Faker().image_url()
        ]})
        pet.update({"tags": [
            {
                "id": DataUtils.generate_random_integer(5000, 5030035),
                "name": DataUtils.generate_name()
            }
        ]})
        pet.update({"status": status})

        return pet

    @staticmethod
    def generate_order_body(pet_id):
        order = json.load(open('../model/data/pet_body.json'))

        order.update({'id': DataUtils.generate_random_integer(5000, 5030035)})
        order.update({'petId': pet_id})
        order.update({'quantity': DataUtils.generate_random_integer(1, 20)})
        order.update({'shipDate': Faker().date()})
        order.update({'complete': random.choice([True, False])})

        return order
