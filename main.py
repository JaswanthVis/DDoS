import os
import argparse

from mininet.topo import Topo

print('Started')

class DDoSTopology(Topo):

    def build(self):
        # Create custom topology for desired configuration
        IN_FOLDER = 'out'
        IN_FILE = 'routes.txt'

        _network_matrix = {}
        with open(os.path.join(os.getcwd(), IN_FOLDER, IN_FILE), 'r') as _network_paths:
            # Build node connections
            for _entry in _network_paths:
                _source, _sink = int(entry[0]), int(entry[1])
                
                if _source in _network_matrix.keys():
                    _network_matrix[_source].append(_sink)
                else:
                    _network_matrix[_source] = [_sink]

        for _key, _value in _network_matrix.items():
            # Add hosts and switches
            _switch = self.addSwitch(str(_key))

            for _host in _value:
                self.addLink(self.addHost(str(_host)), _switch)

        
if __name__ == "__main__":

    IN_FOLDER = 'in';
    INPUT_FILE = 'routers_data_undirected.txt'
    _source_file = os.path.join( os.getcwd(), IN_FOLDER, INPUT_FILE);      
    _matrix = []

    DEFAULT_GROUP_START = ( 18 - 1 ) * 50
    DEFAULT_GROUP_END = 18 * 50

    try:
        # Create data array for all nodes in landscape
        with open(_source_file, 'r') as _network_paths:
            for entry in _network_paths:
                _source, _sink = int(entry.strip('\n').split('\t')[0]), int(entry.strip('\n').split('\t')[1])

                _matrix.append([_source, _sink])

        _actual_matrix = _matrix[DEFAULT_GROUP_START: DEFAULT_GROUP_END]

        print('DDoS Matrix', _actual_matrix)
        print('Size: ' + str(len(_actual_matrix)))

        OUT_FOLDER = 'out'
        OUT_FILE = 'routes.txt'

        # Output desired nodes to local repository
        with open(os.path.join(os.getcwd(), OUT_FOLDER, OUT_FILE), 'w') as _network_paths:
            for entry in _actual_matrix:
                _network_paths.write(str(entry[0]) + ',' + str(entry[1]) + '\n')


        _topo =  DDoSTopology()
        _topo.build()

    except Exception as err:
            print(err)

print('Completed')