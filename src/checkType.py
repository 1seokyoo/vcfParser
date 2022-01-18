#!/usr/bin/python3

def checkType(inputStart, inputRef, inputAlt):

    outputEnd = 0
    outputType = 'None'

    inputStart = int(inputStart)
    refLength = len(inputRef)
    altLength = len(inputAlt)

    if refLength == altLength:
        if refLength == 1:
            outputType = 'SNV'
            outputEnd = inputStart
        else:
            outputType = 'MNV'
            outputEnd = inputStart + altLength - 1

    else:
        if refLength < altLength:
            outputType = 'INS'
            outputEnd = inputStart + altLength - 1
        else:
            outputType = 'DEL'
            outputEnd = inputStart + altLength - 1

    return outputType, outputEnd