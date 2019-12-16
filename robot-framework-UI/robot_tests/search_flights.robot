*** Settings ***
Documentation    This is sample test case from blaze demo application https://blazedemo.com


Library  SeleniumLibrary
Library  OperatingSystem
Resource  ${CURDIR}/../robot_keywords/search_flights_keyword.robot

*** Variables ***
${URL}    http://blazedemo.com

*** Test Cases ***
The User can search for flights
    [Tags]    search_flights
    Launc application url   ${url}
    Select the departure city  Paris
    Select the arrival city   London
    Submit the login
    @{flights}=  Get WebElements    css:table[class='table']>tbody tr
    Should Not Be Empty     ${flights}



