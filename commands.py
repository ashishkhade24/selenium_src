options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options,service=ChromeService(ChromeDriverManager().install()))

pytest -vv -s --disable-pytest-warnings .\src\test_arithmetic_functions.py
test_arithmetic_functions.py::test_multiplication
pytest -vv -s --disable-pytest-warnings .\src\test_arithmetic_functions.py::test_multiplication
#Pattern matching
pytest -vv -s -k "arithmetic and pytest" --disable-pytest-warnings .\src\
pytest -vv -s -k "arithmetic or pytest" --disable-pytest-warnings .\src\

#Marking
pytest -vv -s -m Smoke --disable-pytest-warnings .\src\
pytest -vv -s -m One --disable-pytest-warnings .\src\
pytest -vv -s -x --disable-pytest-warnings .\src\test_arithmetic_functions.py
pytest - vv - s - -maxfail = 2 - -disable - pytest - warnings.\src\test_arithmetic_functions.py











