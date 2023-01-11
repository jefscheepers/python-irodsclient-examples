# python-irodsclient-examples
Example scripts for the Python-irodsclient

The scripts in this repository have two goals:
- To serve as an example for users who want to write their own scripts with the python-irodsclient
- To be easily usable from the command line for those who can't 

## Prerequisites

- python >= 3.7
- python-irodsclient >= 1.1.5

you can install the python-irodsclient with pip:  

`pip3 install python-irodsclient`  

## Logging in to the python-irodsclient

The easiest way to log in with the Python client is actually to log in via iCommands.
However, users of the iRODS installation of the KU Leuven who don't have access to iCommands, have two alternative options:
- Copy the code snippet on the iRODS portal site under 'Python Client on Windows' in your python interpreter.
    - This method is designed for Windows (since windows users don't have access to iCommands except via WSL), but can be used by Mac and Linux users as well.
- Use [iinit.exe](https://github.com/kuleuven/iRODS-User-Training/blob/main/06_PRC_Handson_User-Training.md#using-the-prc-on-a-windows-machine)

## Usage  

### List a collection  


`python3 list_collection_contents.py --path <collection_path>`  

Lists the contents of a collection by using the `session.collections.get()` method to instantiate a collection as python object, then printing its `subcollections` and `data_objects` attributes.  


### Upload a file

`python3 upload_file.py --source <path_to_local_file> --destination <path_to_collection_in_irods>`  

Uploads a file with the `session.data_objects.put()` method.  


### Download a data object 

`python3 download_file.py --source <path_to_data_object_in_irods> --destination <path_to_local_directory>`  

Downloads a file with the `session.data_objects.get()` method.  
This method is to instantiate data objects as python object.  
However, when given a local destination as second argument, this method also downloads the object.  