import os
import ssl
from irods.session import iRODSSession
from argparse import ArgumentParser


if __name__ == '__main__':
    try:
        env_file = os.environ['IRODS_ENVIRONMENT_FILE']
    except KeyError:
        env_file = os.path.expanduser('~/.irods/irods_environment.json')

    ssl_context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH, cafile=None, capath=None, cadata=None)
    ssl_settings = {'ssl_context': ssl_context}
    with iRODSSession(irods_env_file=env_file, **ssl_settings) as session:

        # Handling command line arguments
        parser = ArgumentParser(usage=__doc__)
        parser.add_argument("--data_object",
                            dest = 'data_object',
                            required = True, 
                            help = "The path of the data object you want to add metadata to")
        parser.add_argument("--attribute",
                            dest = 'attribute',
                            required = True,
                            help = "The attribute of the AVU")
        parser.add_argument("--value",
                            dest = 'value',
                            required = True,
                            help = "The value of the AVU")
        parser.add_argument("--units",
                            dest = 'units',
                            help = "The units of the AVU (optional)")
        args = parser.parse_args()

        data_object = args.data_object
        attribute = args.attribute
        value = args.value
        if args.units:
            units = args.units
        else:
            units = ''

        # instantiate the data object as python object
        obj = session.data_objects.get(data_object)
        
        # add our metadata to the data object
        obj.metadata.add(attribute, value, units)

        # list all metadata on the object
        for item in obj.metadata.items():
            # in the python client, the attribute of an AVU is called 'name'
            print(item.name, item.value, item.units)


