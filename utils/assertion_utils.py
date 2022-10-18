import sys


class Assertion:

    @staticmethod
    def status_check(resp, exc_value):
        sys.stdout.write(
            f'Checking Response status. Expected status code: {exc_value} and response status code:{resp.status_code}\n')

        assert resp.status_code == exc_value, f"Status code is not match!"

    @staticmethod
    def null_check(field, value):
        sys.stdout.write(f'Asserting {field} is not null (value ={value})\n')
        assert value is not None, f"{field} is Null!"

    @staticmethod
    def type_check(key, value_type, value):
        sys.stdout.write(f'\nAsserting field type {key} type==={value_type} and value==={value}\n')

        assert value_type == type(value), f"{key} type is not match!"

    @staticmethod
    def value_check(field, value, exc_value):
        sys.stdout.write(f'The field: {field}, Expected value is: {exc_value}, and response value is: {value}\n')
        assert value == exc_value, f"{field} is not match with response"
