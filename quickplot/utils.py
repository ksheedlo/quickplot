import numpy

def split_dict(keys, dict_elt):
    '''
    Splits a dictionary into two using the specified key set.

    '''
    key_set = set(keys)
    dict_items = dict_elt.items()
    with_keys = dict([(k, v) for (k, v) in dict_items
                        if k in key_set
                    ])
    without_keys = dict([(k, v) for (k, v) in dict_items
                        if k not in key_set
                    ])
    return with_keys, without_keys

def mod2pi(theta):
    modulus = int(numpy.floor(theta / (2*numpy.pi)))
    return theta - (modulus*2*numpy.pi)

