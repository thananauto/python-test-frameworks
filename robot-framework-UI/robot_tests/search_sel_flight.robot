*** Settings ***
Documentation    Suite description
Library  ../sel_flight_test//SearchFlightPage.py  Chrome
Suite Setup  Open
Suite Teardown  Close

*** Test Cases ***
The user can search for flights
    [Tags]  flights_sel
    Select Departure City   Paris
    Select Destination City    London
    Submit the login
    @{flights}=     Get Found Flights
    Should Not Be Empty     ${flights}