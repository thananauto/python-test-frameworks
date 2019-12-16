*** Settings ***
Documentation    Suite description
Library  RequestsLibrary
Library  Collections
Library  OperatingSystem


*** Variables ***
${BASE_URL}     http://thetestingworldapi.com/
${ID}       1014


*** Test Cases ***
TC_002 to delete the techincal details of student
    [Tags]  DELETE   PUT
    [Documentation]  To delete the technical details of user
    create session  student_delete  ${BASE_URL}
    ${RESPONSE}=    delete request  student_delete  api/technicalskills/${ID}
    should be equal as strings  ${RESPONSE.status_code}  200



TC_002 to update the skills of student using api
    [Tags]    PUT
    [Documentation]  Validate the user for updating the skills
    create session  student_details     ${BASE_URL}     headers={'Content-Type':'application/json'}
    ${JSON}=    get file    ./test_data/put_data.json
    ${RESPONSE}=    put request  student_details    api/technicalskills/${ID}    data=${JSON}
    should be equal as strings   ${RESPONSE.status_code}  200
    dictionary should contain item  ${RESPONSE.json()}  status  true
    dictionary should contain item  ${RESPONSE.json()}  msg  Update\ \ \data\ \success

