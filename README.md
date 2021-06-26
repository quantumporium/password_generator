![img](Password_Gen.png)
![badge](https://img.shields.io/github/license/quantumporium/password_generator)

### ```Password Generator``` allow you to create a password trough your terminal.


## Install Requirement
```bat
pip install requirements.txt
```
__make sure to be in the parent folder and to have a virtual envrionment__

## Usage
Use without interactive command line interface
```python
python app/password_generator.py [password lenght] #if you are in the parent folder
python password_generator.py [password lenght] #if you are in the app folder
passowrd_generator.py [password lenght] #if you are in the app folder
```

Use with interactive command line interface
```python
python app/password_generator.py #if you are in the parent folder
python password_generator.py #if you are in the app folder
passowrd_generator.py #if you are in the app folder
```

__The passowrd can not be shorter than 5 characters, if giving a lenght shorter than 5 it will default to a lenght of 5.__
## Acknowledgements
- [This article](https://www.geeksforgeeks.org/generating-strong-password-using-python/) was used as a reference.

## License
[MIT](https://github.com/quantumporium/password_generator/blob/main/LICENSE)
