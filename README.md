# python-irodsclient-examples
Example scripts for the Python-irodsclient

The scripts in this repository have two goals:
- To serve as an example for users who want to write their own scripts with the python-irodsclient
- To be easily usable from the command line for those who can't 

## Prerequisites

- python >= 3.7
- python-irodsclient >= 1.1.5

## Logging in to the python-irodsclient

The easiest way to log in with the Python client is actually to log in via iCommands.
However, users of the iRODS installation of the KU Leuven who don't have access to iCommands, have two alternative options:
- Copy the code snippet on the iRODS portal site under 'Python Client on Windows' in your python interpreter.
    - This method is designed for Windows (since windows users don't have access to iCommands except via WSL), but can be used by Mac and Linux users as well.
- Use [iinit.exe](https://github.com/kuleuven/iRODS-User-Training/blob/main/06_PRC_Handson_User-Training.md#using-the-prc-on-a-windows-machine)

## Usage