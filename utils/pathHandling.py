# this is because importing in python is crap
import pathlib




def getDataStructuresAbsPath():
    """
    getDataStructuresAbsPath is a function to retrieve the absolute path
    of dataStructures folder of AlgorithmsAndDataStructuresPy project.

    :return: returns a pathlib class with the 
    path flavour of the os this program is running on.
    """ 

    # get this file's abs path
    currDir = pathlib.Path(__file__)

    # go up two directories and append the dataStructures dir to the path
    dataStructuresAbsPath = pathlib.Path(str(currDir.parent.parent.resolve()) + "/dataStructures")

    return dataStructuresAbsPath