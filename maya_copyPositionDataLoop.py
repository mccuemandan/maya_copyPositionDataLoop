import maya.cmds as cmds

quantity = 10

# Parent Parameters:
parentPrefix = "parentObj"
parentStartNum = 1
parentSuffix = ""
onlyParent = False      # True if parenting multiple things to single obj

# Child Parameters:
childPrefix = "childObj"
childStartNum = 1
childSuffix = ""

# Point Constraint Parameters:
pointWeight = 1.0 # default is 1.0
skipPosition = []   # "x", "y", "z", or "none". "none" is default

# Orient Constraint Parameters:
orientWeight = 1.0
skipRotation= []    # "x", "y", "z", or "none". "none" is default

# define loop parameters:
parentNum = parentStartNum
childNum = childStartNum

for i in range(quantity):
    currentParent = parentPrefix + str(parentNum) + parentSuffix
    currentChild = childPrefix + str(childNum) + childSuffix

    # Copy Position Data
    pointConstraintName = str(currentChild) + "_pointConstraint1"
    cmds.pointConstraint( currentParent, currentChild, w= pointWeight, sk= skipPosition, name= pointConstraintName )
    cmds.delete(pointConstraintName)

    # Copy Rotation Data
    orientConstraintName = str(currentChild) + "_orientConstraint1"
    cmds.orientConstraint( currentParent, currentChild, w= orientWeight, sk= skipRotation, name= orientConstraintName)
    cmds.delete(orientConstraintName)

    if onlyParent == True:
        parentNum = 1
    else:
        parentNum += 1

    childNum += 1