# REST Countries API
REST Countries API is home assignments 


## Function Description
REST Countries API Automation Tests

This script performs automated testing for the "GET /all, GET /name/{name}, GET /alpha/{code}, GET /region/{region}" on https://restcountries.com/ 
using PyTest and the requests librarys.

# Instructions:


## Installation

	1. Clone or download the Python script containing the functions (link to code [https://github.com/walidatorkh/qa_automation_home_assignment.git](https://github.com/walidatorkh/rest_countries_api.git)).
	2. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
	3. cd rest_countries_api
  	4. Activate virtual enviroment using CMD 
  	### venv\Scripts\activate.bat
  	5. Install the required dependencies using
  	### pip: pip install -r requirements.txt

## Execution

	1. Open CMD and navigate to file location
	2. Execute:
 	### pytest --html=report.html
        3. Open using browser created report.html to validate test results

# High-Level Test Plan for REST Countries API

| Test Case ID | Test Case Description                                      | Expected Outcome                                             | Status  |
|--------------|-----------------------------------------------------------|-------------------------------------------------------------|---------|
| TC-001       | Retrieve All Countries                                    | Response contains data for all countries and status code 200 | Passed  |
| TC-002       | Retrieve Country by Name (valid)                         | Correct data is returned for valid country name             | Passed  |
| TC-003       | Retrieve Country by Name (invalid)                       | Appropriate error message is returned                        | Passed  |
| TC-004       | Retrieve Country by Code (valid CCA2)                    | Correct data is returned for valid country code (CCA2)     | Passed  |
| TC-005       | Retrieve Country by Code (valid CCN3)                    | Correct data is returned for valid country code (CCN3)     | Passed  |
| TC-006       | Retrieve Country by Code (valid CIOC)                    | Correct data is returned for valid country code (CIOC)     | Passed  |
| TC-007       | Retrieve Country by Code (invalid)                       | Appropriate error message is returned                        | Passed  |
| TC-008       | Retrieve Countries by Region (valid region)              | Only countries from specified region are returned           | Passed  |
| TC-009       | Retrieve Countries by Region (invalid region)            | Appropriate error message is returned                        | Passed  |
| TC-010       | Retrieve All Countries (invalid endpoint)            | Appropriate error message is returned     | Passed  |
| TC-011       |  Validate JSON Schema for specific Country (e.g., USA)    | Response matches the expected JSON schema                    | Passed  |
   

## Limitations:
1. Lack of documentation regarding errors that may occur during API calls, including specific error codes and their meanings.
2. JSON schema validation for countries is not feasible due to inconsistency (each entry must be tested individually).
3. Insufficient data on several countries that returned results, preventing a reliable count of returned values.
4. The expected response time and system load behavior have not been described.

