import random

import pytest
from faker import Faker

from service.pet_service import PetService
from model.enum.pet_status_enum import PetStatusEnum
from utils.assertion_utils import Assertion
from utils.data_utils import DataUtils


class TestPetStore:
    """Pet Operations tests - """

    @pytest.mark.smoke
    def test_create_pet(self):
        pet_body = DataUtils.generate_pet_body(PetStatusEnum.AVAILABLE)

        resp = PetService.create_pet(pet_body)

        Assertion.status_check(resp, 200)  # The resp code should normally be 201, but they are using 200!
        Assertion.null_check("Response", resp)
        Assertion.value_check("name", resp['name'], pet_body['name'])

    @pytest.mark.smoke
    def test_get_pets_by_status(self):
        resp = PetService.get_pets_by_status(PetStatusEnum.PENDING)

        Assertion.status_check(resp, 200)
        Assertion.value_check("status", resp[random.randint(0, len(resp.json()))]['status'],
                              PetStatusEnum.PENDING)

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_update_pet(self):
        pet_body = DataUtils.generate_pet_body(PetStatusEnum.AVAILABLE)

        PetService.create_pet(pet_body)

        new_pet_name = Faker().name()
        pet_body['name'] = new_pet_name
        pet_body['status'] = PetStatusEnum.PENDING

        resp = PetService.update_pet(pet_body)

        Assertion.value_check("status", resp['status'],
                              PetStatusEnum.PENDING)
        Assertion.value_check("name", resp['name'],
                              new_pet_name)

    @pytest.mark.regression
    def test_delete_pet(self):
        pet_body = DataUtils.generate_pet_body(PetStatusEnum.AVAILABLE)

        PetService.create_pet(pet_body)

        resp = PetService.delete_pet(pet_body['id'])

        Assertion.value_check("Deletion Message", resp['message'], str(pet_body['id']))
        return True
