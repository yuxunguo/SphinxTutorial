# This is the module2 under the root folder

def Module2_TestFunc1(test):
    """This is the Test function 1 under the module2 in the root folder

    Args:
        test (N/A): N/A 

    Returns:
        int : N/A
    """
    return 0

def TFF_Fancy(arg1, args_other):
    r"""The Transition form factor (TFF) :math:`\mathcal{F}(\xi, t)`
    
    | This is a fancier version of the previous :func:`module1.TFF`
    | Some more description there
    | Line break can be enforced by '|'
    
    Args:
        arg1: array in the form of [arg1_1,arg1_2,...]
    
            - arg1_1 = some descriptions
            - | arg1_2 = some descriptions
              | force a line break here
            - ...
            
        args_other: other arguments
        
    Returns:
        complex : TFF :math:`\mathcal{F}(\xi, t)`
    """

    return 0