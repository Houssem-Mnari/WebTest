*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${URL}            https://www.saucedemo.com/
${BROWSER}        Chrome
${USERNAME}       standard_user
${PASSWORD}       secret_sauce

*** Test Cases ***
Test de Connexion Standard User
    Open Browser    ${URL}    ${BROWSER}
    Input Text      id:user-name    ${USERNAME}
    Input Text      id:password    ${PASSWORD}
    Click Button    id:login-button
    Wait Until Page Contains Element    class:inventory_list    timeout=10s
    Close Browser
