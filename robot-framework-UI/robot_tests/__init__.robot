*** Settings ***
Documentation    Suite description
Library  SeleniumLibrary
Suite Setup   Open Browser   ${BROWSER}  ${PATH}
Suite Teardown  Close Browser
Library  SeleniumLibrary
Library  OperatingSystem
Resource  ${CURDIR}/../robot_keywords/search_flights_keyword.robot

*** Variables ***
${PATH}    C:\\projects\\python-workspace\\drivers\\chromedriver.exe
${BROWSER}   Chrome


