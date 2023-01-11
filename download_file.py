"""Download a file from iRODS"""

import os
import ssl
from argparse import ArgumentParser
from irods.session import iRODSSession
from irods.exception import DataObjectDoesNotExist

# helper function
def make_path_absolute(path):

    """Returns the absolute version of a path
    
    Argumuments
    -----------
    path: str
        path to be modified

    """

    if path.startswith("/"):
        return path
    elif path == '.':
        return os.getcwd()
    else:
        path = os.getcwd() + "/" + path
        return path

def download_file(session, source, destination):

    # transform destination to an absolute path, if necessary
    destination = make_path_absolute(destination)

    # when you use the 'get' method and specify a destination path, 
    # it downloads the file to that destination.

    session.data_objects.get(source, destination)




if __name__ == '__main__': 

    # Handling commandline arguments
    parser = ArgumentParser(usage=__doc__)
    parser.add_argument("--source", dest='source', required = True, help="The path to the data object you want to upload")
    parser.add_argument("--destination", dest='destination', required = True, help="Path of the directory you want to download the file to")
    args = parser.parse_args()
    
    source = args.source
    destination = args.destination

    # Creating an iRODS session
    try:
        env_file = os.environ['IRODS_ENVIRONMENT_FILE']
    except KeyError:
        env_file = os.path.expanduser('~/.irods/irods_environment.json')
    ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=None, capath=None, cadata=None)
    ssl_settings = {'ssl_context': ssl_context}
    with iRODSSession(irods_env_file=env_file, **ssl_settings) as session:

        # transform path of destination to absolute path,
        # if necessary
        destination = make_path_absolute(destination)

        # check if data object exists
        try: 
            # trying to instantiate data object as object in python
            obj = session.data_objects.get(source)

            # if that succeeded, we can run our main function
            download_file(session, source, destination)

        except DataObjectDoesNotExist:
            print("The data object you specified does not exist.")
            