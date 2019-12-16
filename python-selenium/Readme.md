### Test Automation framework - **BDD - Python**

This demo project is implemented with help of behave

Steps to configure:
1. Install Jbehave and Selenium commands from terminal
    ``pip install Jbehave`` and  ``pip install selenium``
    
2. Run this command to find the missing step definitions in the `step` folders
    ``behave feature/<fileName.feature>``
    
3. `context` keyword is used to share state between all step or all scenarios
for good practise, initialise the `environment.py` module in the framework

4. `Behave` always look for the `steps` folder inside the `features` folder

###### Way to start the test from behave
```# Run all scenarios in the project
behave
 
# Run all scenarios in a specific feature file
behave features/web.feature
 
# Filter tests by tag
behave --tags-help
behave --tags @web
behave --tags ~@unit
behave --tags @basket --tags @add,@remove
 
# Write a JUnit report (useful for Jenkins and other CI tools)
behave --junit
 
# Don't print skipped scenarios
behave -k```