*** Settings ***
Library            /home/than/robotFramework/test1/libraries/checkPattern.py



*** Variables ***
${path}
*** Test Cases ***
Test my text
	Just a Keyword       ${path}
	
	
*** Keywords ***
Just a Keyword
	[Arguments]    	${path}
	checkMe     	${path}

       
	
	
