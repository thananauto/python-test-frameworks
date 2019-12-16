## **pytest-BDD-framework**

If we use `-U` the installation will be done in global level, always try to avoid
the global installation, always run the script with `venv`

By default pytest only identifies the file names starting with `test_` or ending with `_test` as the test files. We can explicitly mention other filenames though (explained later).
 Pytest requires the test method names to start with `"test."` All other method names will be ignored even if we explicitly ask to run those methods.

#### Step's to install
1. `pip install pytest`
2. `pip install selenium`

Or simply run the `pip install -r requirements.txt`

#### To Run test
1. `py.test` will execute the all the test methods
2. `py.test -k <method name> -v`, the method name will substring of methods
3. `py.test -m <set name>`
4. Run the test using marker as well `py.test -m <name>`
5. Run the test with following commands to know more about `py.test -s`


#### Run test in parallel
1. Install `pytest-xdist`

Run `py.test -n 4` -> N represent's the number of threads


#### Syntax and comments

Refer pytest documentation for more details
Always try to use `Fixtures` for setup or precondition

#### For report generation
Install allure report in the local installation
during execution use

`py.test --alluredir=<folder_name> -k <method_name> -v`


To see all trace  back o/p
`py.test -k <method_name> -s -v

conftest.py is used to store all fixtures needed for data setup and execution`