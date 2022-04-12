import os
import argparse


print('Started')

if __name__ == "__main__":

    IN_FOLDER = 'in';
    INPUT_FILE = 'routers_data_undirected.txt'
    _source_file = os.path.join( os.getcwd(), IN_FOLDER, INPUT_FILE);      
    _matrix = []

    DEFAULT_GROUP_START = ( 18 - 1 ) * 50
    DEFAULT_GROUP_END = 18 * 50

    try:
        # Create data dictionary & histogram data entries
        with open(_source_file, 'r') as _network_paths:
            for entry in _network_paths:
                _source, _sink = int(entry.strip('\n').split('\t')[0]), int(entry.strip('\n').split('\t')[1])

                _matrix.append([_source, _sink])

        _actual_matrix = _matrix[DEFAULT_GROUP_START: DEFAULT_GROUP_END]

        print('DDoS Matrix', _actual_matrix)
        print('Size: ' + str(len(_actual_matrix)))

        OUT_FOLDER = 'out'
        OUT_FILE = 'routes.txt'
        

    except Exception as err:
            print(err)

print('Completed')