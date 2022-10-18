<h1>PetStore Pytest API Automation Project</h1>
This project is prepared for the PetStore API Test.
<h2>Tool stack</h2>

* Python
* Pytest
* Requests
* Faker

<h3>Requirements</h3>

* Python 3 or higher must be installed (Version 3.10 preferred) <a href="https://www.python.org/downloads/"> Python
  download page
* Pytest must be installed <a href="https://pypi.org/project/pytest/">Pytest download</a>,

<h3>Project Tree</h3>

```
.
├── README.md
├── config
│   ├── base_config.py
│   └── service_config.py
├── conftest.py
├── model
│   ├── data
│   │   ├── order_body.json
│   │   └── pet_body.json
│   └── enum
│       └── pet_status_enum.py
├── pytest.ini
├── requirements.txt
├── service
│   ├── order_service.py
│   └── pet_service.py
├── test
│   ├── output
│   │   ├── assets
│   │   │   └── style.css
│   │   └── report.html
│   ├── test_pet_order.py
│   └── test_pet_store.py
└── utils
    ├── assertion_utils.py
    ├── data_utils.py
    └── http_utils.py
```

<h4>Config Folder</h4>
Used for environment variables. There are usually *_config.py files.

<h4>Model Folder</h4>
This will be used for variables implementation in the project. Json bodies should be define in the json file. Enum Variables should be defined in the class.

<h4>Service Folder</h4>
Requests to the service are managed here, methods are usually created using service utils.

<h4>Tests folder</h4>
Test files, that is, test cases in Pytest format will be located under this folder.

<h4>Utils Folder</h4>
The utils class and methods of the project will be defined in this folder.

<h4>conftest.py</h4>
File where decorators such as global fixtures are defined for pytest.

<h4>pytest.ini</h4>
Required file for pytest configuration. You can manage pytest attributes such as pytest-html report in here.

<h4>requirements.txt</h4>
The file required for the installation of project necessary libraries.

<h4>output/*</h4>
Generates pytest-html reports after each execution.

<h2>Naming Convention</h2>

Conditions are requested when naming. Names should be short and meaningful.

``directory names = my_directory (snake case)``

``variable name = my_variable (snake case)``

``method name = my_method (snake case)``

``class name = MyClass (Pascal case)``

``tag name = @MyTag (Pascal case)``



<h2> Execution </h2>
Install required libraries :
pip3 install -r requirements.txt

Python CLI command to run tests.

execution tests :

``
python3 -m pytest
``

execution tests via specific test file

``
python3 -m pytest 'file path'
``

execution tests via marks

**@pytest.mark.smoke** should be added on the test case

``
pytest -v -m smoke
``

execution tests via parallel

``
python3 -m pytest -n 4
``