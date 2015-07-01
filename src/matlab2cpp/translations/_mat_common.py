from _variables import *
from _arma_common import configure_arg

def Get(node):

    assert len(node) in (1,2)

    # Single argument
    if len(node) == 1:

        arg, dim = configure_arg(node[0], 0)

        if dim == -1:
            return "%(name)s(%(0)s)"

        if dim == 0:
            node.dim = 0

        return "%(name)s(" + arg + ")"

    # Double argument
    elif len(node) == 2:

        arg0, dim0 = configure_arg(node[0], 0)
        arg1, dim1 = configure_arg(node[1], 1)

        if -1 in (dim0, dim1):
            return "%(name)s(", ", ", ")"

        # Configure dimensions
        if dim0:
            if dim1:
                node.dim = 3
            else:
                node.dim = 1
        else:
            if dim1:
                node.dim = 2
            else:
                node.dim = 0

        return "%(name)s(" + arg0 + ", " + arg1 + ")"


def Set(node):
    # Single argument
    if len(node) == 1:

        arg, dim = configure_arg(node[0], 0)
        if dim == 0:
            node.dim = 0

        if dim == -1:
            return "%(name)s(", ", ", ")"

        return "%(name)s(" + arg + ")"


    # Double argument
    elif len(node) == 2:

        arg0, dim0 = configure_arg(node[0], 0)
        arg1, dim1 = configure_arg(node[1], 1)

        if -1 in (dim0, dim1):
            return "%(name)s(", ", ", ")"

        # Configure dimensions
        if dim0:
            if dim1:
                node.dim = 3
            else:
                node.dim = 1
        else:
            if dim1:
                node.dim = 2
            else:
                node.dim = 0

        return "%(name)s(" + arg0 + ", " + arg1 + ")"