*** Settings ***
Documentation  This is set of keywords which are going to be re use across all test suites
...             This page contains only the most general keywords needed for test suite

Library  SeleniumLibrary


*** Variables ***
#${URL}     http://http://blazedemo.com/
#${BROWSER}  Chrome
*** Keywords ***

Open Browser
    [Arguments]  ${BROWSER}  ${PATH}
     Create Webdriver   ${BROWSER}  executable_path=${PATH}

Close Browser
    Close All Browsers

Launc application url
    [Arguments]  ${URL}
    Go To   ${URL}

Select the departure city
    [Arguments]  ${city}
     Select From List By Value   xpath://select[@name='fromPort']   ${city}

Select the arrival city
    [Arguments]  ${city}
    Select From List by Value   xpath://select[@name='toPort']  ${city}

Submit the login
    Click Button    css:input[type='submit']



