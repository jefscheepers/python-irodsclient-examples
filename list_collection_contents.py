"""Print the contents of a collection"""

import os
import ssl
from argparse import ArgumentParser
from irods.session import iRODSSession
from irods.exception import CollectionDoesNotExist


def list_collection_contents(session, path):

    """Print contents of a collection
    
    Arguments:
    ---------
    session: object
        An iRODSSession object
    path: str
        The path to the collection
    
    Returns
    -------
    Nothing
    """
    # instantiate the collection as python object
    try:
        collection = session.collections.get(path)
    except CollectionDoesNotExist:
        print("The collection you specified does not exist.")
        print("Please check if you have any mistakes in your path")
        return
    
    print(f"Collection path: {collection.path}")

    # printing subcollections
    print("\nSubcollections:")
    for subcollection in collection.subcollections:
        print("\t" + subcollection.name)


    # printing data objects
    print("\nData objects:")
    for data_object in collection.data_objects:
        print("\t" + data_object.name)


if __name__ == "__main__":

    # Handling commandline arguments
    parser = ArgumentParser(usage=__doc__)
    parser.add_argument("--path", dest='path', nargs = '?', help="The path of the collection")
    args = parser.parse_args()

    # Creating an iRODS session
    try:
        env_file = os.environ['IRODS_ENVIRONMENT_FILE']
    except KeyError:
        env_file = os.path.expanduser('~/.irods/irods_environment.json')
    ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=None, capath=None, cadata=None)
    ssl_settings = {'ssl_context': ssl_context}
    with iRODSSession(irods_env_file=env_file, **ssl_settings) as session:

        # If no path is given, default to the user's home directory.
        if args.path:
            path = args.path
        else:
            path = f"/{session.zone}/home/{session.username}"
            

        # Invoking main function
        list_collection_contents(session, path)
