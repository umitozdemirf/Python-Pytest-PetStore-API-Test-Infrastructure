import random

import pytest
from faker import Faker

from service.pet_service import PetService
from service.order_service import OrderService
from model.enum.pet_status_enum import PetStatusEnum
from utils.assertion_utils import Assertion
from utils.data_utils import DataUtils


class TestPetOrder:
    """Pet Operations tests - """

    @pytest.mark.smoke
    def test_create_order(self):
        pet = PetService.create_pet(DataUtils.generate_pet_body(PetStatusEnum.AVAILABLE))
        order_body = DataUtils.generate_order_body(pet['id'])
        resp = OrderService.create_order(order_body)

        Assertion.value_check("petId", resp['petId'], pet['id'])
