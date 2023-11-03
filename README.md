# AirBnB_clone hbnb

This is the first step towards building our first full web application: the AirBnb clone. This first step is very important because we will use what we build during this project with all other following projects.

In this task we will:

-put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of our future instances

-creating a simple flow of serialization/deserialization: Instances <-> Dictionary <-> JSON string <-> file

-creating all classes used for AirBnb (User, State, City, Place...) that inherit from BaseModel

-creating the first abstracted storage engine of the project: File Storage

-creating all unittests to validate all our classes and storage engine

# The command interpreter

The command interpreter is used to manage the whole application's functionality from the command line, such as:

-creating a new object

-retrieving an object from a file, database, etc...

-do operations on objects (count, compute stats, etc...)

-update attributes of an object

-destroy an object

## How to Start It

To start the command interpreter, simply run the `console.py` file.

```bash
python console.py

## Usage

Your console should work like this in interactive mode:

```bash
$ ./console.py

(hbnb)
(hbnb) help

Documented commands (type help <topic>):

EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```bash

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):

EOF  help  quit
(hbnb)
$
```

## Commands

| Command | Syntax | Output |
| ------- | ------ | ------ |

help | help [option] | List available commands with "help" or detailed help with "help cmd".

quit | quit | Exit command interpreter.

EOF | EOF | Exit command interpreter.

create | create [class] | Creates a new instance of class, saves it (to the JSON file) and prints the id.

show | show [class] [id] | Prints the string representation of an instance based on the class name and id.

list | list [class] | Print all instances based on the class name.

update | update [class] [id] [attribute=value ...] | Update attributes for an existing instance by its ID.

delete | delete [class] [id] | Deletes an existing instance from the database.

all | all [class] | Prints all string representation of all instances based or not on the class name.

count | count [class] | Retrieve the number of instances of a class.

## Testing

Unittests for the command interpreter are defined in the tests directory. To run the entire test suite simultaneously, execute the following command:

```bash
$ python3 -m unittest discover tests
```

## Authors

Juan Rodriguez

Nadja Miranda
