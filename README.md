# AirBnB Clone

## Project Description
This project is a clone of AirBnB, implemented as part of the ALU Software Engineering curriculum. The goal is to eventually build a web application that mimics the core functionality of AirBnB.

The project will be built step by step, starting with a command-line interpreter to manage AirBnB objects. This is the first step towards building the full web application and will be used to validate the storage engine.

## Command Interpreter

### How to Start It
The command interpreter can be started in two modes:

**Interactive Mode**:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

**Non-Interactive Mode**:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### How to Use It
The command interpreter supports the following commands:
- `create`: Creates a new instance of a class
- `show`: Prints the string representation of an instance
- `destroy`: Deletes an instance based on the class name and id
- `all`: Prints all string representation of all instances
- `update`: Updates an instance based on the class name and id

### Examples
```
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2022, 10, 28, 21, 3, 54, 52298), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2022, 10, 28, 21, 3, 54, 52302)}"]
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2022, 10, 28, 21, 3, 54, 52298), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2022, 10, 28, 21, 3, 54, 52302)}
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb) quit
$
``` 