*** Settings ***
Documentation    Test to check on GET API service of testingworldapi.com
Library  RequestsLibrary
Library  Collections

Test Teardown  Delete All Sessions

*** Variables ***
${BASE_URL}  http://thetestingworldapi.com/
${STUDENT_ID}   1012


*** Test Cases ***
TC_001 get the student details
     [Tags]  smoke
     [Documentation]  Validate the student details using API
     create session  student_details  ${BASE_URL}
     ${response}=  get request  student_details  api/studentsDetails/${STUDENT_ID}
     should be equal as strings   ${response.status_code}  200
     Dictionary Should Contain Value  ${response.json()}  true
     dictionary should contain item  ${response.json()}  status  true
     ${list_output}=  get dictionary values  ${response.json()}  false
     ${dic_output}=  get from list  ${list_output}  1
     ${dic_output}=  convert to dictionary  ${dic_output}
     dictionary should contain item  ${dic_output}  id  1012
     dictionary should contain item  ${dic_output}  first_name  Sunil
     dictionary should contain item  ${dic_output}  middle_name  Kumar


TC_002 get the student techical details
     [Tags]  regression
     [Documentation]  Validate the student technocals skills
     create session  student_technical_detail  ${BASE_URL}
     ${response}=  get request  student_technical_detail  api/technicalskills/${STUDENT_ID}
     should be equal as strings   ${response.status_code}  200
     Dictionary Should Contain Value  ${response.json()}  true
     ${dict_output}=  get from dictionary  ${response.json()}  data
     ${dict_output}=  get from dictionary   ${dict_output}  language
     ${list_output}=  convert to list  ${dict_output}
     list should contain value  ${list_output}  sample string 2




