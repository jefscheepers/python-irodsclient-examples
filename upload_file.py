"""Upload a file to iRODS"""

import os
import ssl
from argparse import ArgumentParser
from irods.session import iRODSSession
from irods.exception import CollectionDoesNotExist

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
    else:
        path = os.getcwd() + "/" + path
        return path

# main function
def upload_file(session, filepath, destination):
    """Upload file to the destination collection
    
    Arguments
    ---------
    session: object
        An iRODSSession object
    filepath: str
        The path to the file
    destination: str
        The path to the destination collection in iRODS
          
    Returns
    -------
    Nothing
    """

    # check if destination exists
    try:
        collection = session.collections.get(destination)
    except CollectionDoesNotExist:
        print(f"The collection {destination} doesn't exist.")
        return 

    # the put() method requires the full path of the destination,
    # including the name the dataobject should get
    filename = os.path.basename(filepath)
    destination = destination + "/" + filename

    # uploading the file
    session.data_objects.put(source, destination)


if __name__ == '__main__':
    # Handling commandline arguments
    parser = ArgumentParser(usage=__doc__)
    parser.add_argument("--source", dest='source', help="The path to the directory/file you want to upload")
    parser.add_argument("--destination", dest='destination', help="Path of the collection you want to put the data in")
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

        # transform path of source to absolute path,
        # if necessary
        source = make_path_absolute(source)
        if os.path.isfile(source):
            upload_file(session, source, destination)
        else:
            print("The source you specified is not a file.")
            




