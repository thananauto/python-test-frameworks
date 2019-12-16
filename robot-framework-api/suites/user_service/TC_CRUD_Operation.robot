*** Settings ***
Documentation    Suite description
Library  RequestsLibrary
Library  Collections
Library  OperatingSystem

*** Variables ***
${BASE_URL}     https://reqres.in
${ID}           ${EMPTY}

*** Test Cases ***
TC_001 Create a user
    [Tags]    CREATE SMOKE
    create session  users_service   ${BASE_URL}     headers={'Content-Type':'application/json'}     verify=True
    ${json}=  get file  ./test_data/user.json
    ${object}=  Evaluate  json.loads('''${json}''')  json
    ${response}=    post request  users_service   /api/users  data=${json}
    should be equal as strings  ${response.status_code}     201
    dictionary should contain item  ${response.json()}  name  ${object["name"]}
    dictionary should contain item  ${response.json()}  job  ${object["job"]}
    ${ID}=  get from dictionary  ${response.json()}  id
    ${ID}=  convert to string  ${ID}
    should match regexp  ${ID}    [0-9]*

