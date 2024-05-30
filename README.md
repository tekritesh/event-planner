# event-planner

Python Lib for event planning


## Features

| Feature                 | Status            |
| ----------------------- | ----------------- |
| Base WA Messenger            | &#9745; Completed |
| Personalised WA Message Compose          | &#9745; Completed |
| Selective Map to Number  | &#9744; To do     |
| Financial Planner   | &#9744; To do     |
| Hotel/Flight Price Optimizer  | &#9744; To do     |
| XX                      | &#9744; In progress|
| YY                      | &#9744; To do     |


## Folder Structure

**event_planner/:** Contains Functions and definition

**tests:** Contains Unit Test Case and dummy timeseries dataset

## Installation

#### Install Python Dependency Manager

Refer : https://python-poetry.org/docs/


#### Install Local Dependencies
This should create a local env variable and install all the libs
```
cd ~
poetry install
```

#### Build Package
This should create *tar or *whl for us to invoke in any application under ```dist``` directory 
```
poetry build
```

#### Test Package
Local Test of the package
```
cd tests
poetry run pytest
```

## Usage

#### Using the poetry env to use for Jupyter
Get the env variable name
```
poetry env info
```
- Use this variable for your py-kernel when you launch your jupyter instance in vscode. 
- If you cant find this, then:
- Ctrl/Cmd + P
- Select Python Interpreter
- Enter Interpreter Path
- Use the path as per ```poetry env info``` to add your ``venv`` to vs code


#### Using the poetry cli to run wa_messenger

```bash
 # For Local Unit Check 
poetry run waMessenger 
 ```


```bash
 # example with custom path for contact list and message txt
poetry run waMessenger --input_contact_list tests/test_list.csv --input_msg_txt tests/test.txt
 ```

...

## Contributing

...