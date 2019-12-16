@web
Feature: This is sample feature to test the google application

  Scenario: This is sample test to demo purpose - google application
    Given Launch the application url 'https://google.com'
    When I search for the keyword 'python'
    Then I can see the results wih links


  Scenario: This is sample test to demo purpose - amazon web application
    Given Launch the application url 'https://amazon.de'
    When I search for the keyword 'dresses'
    Then I can see the product information pages


