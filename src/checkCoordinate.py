#!/usr/bin/python3

import vcf
from src.checkType import checkType

def checkCoordinate(inputRecord):

    outputKey = 'None'
    outputDict = {}

    inputChr = inputRecord.CHROM
    inputPos = inputRecord.POS
    inputRef = inputRecord.REF
    inputAlt = str(inputRecord.ALT).replace('[','').replace(']','').replace(' ','').strip()
    inputType, inputEnd = checkType(inputPos, inputRef, inputAlt)

    outputKey = 'GRCh37-{0}-{1}-{2}-{3}'.format(inputChr, str(inputPos), inputRef, inputAlt)
    outputDict = {'chromosome': inputChr,
                  'start_postion': inputPos,
                  'end_position': inputEnd,
                  'reference_allele': inputRef,
                  'alternate_allele': inputAlt,
                  'hgvs.g': '{0}:g.{1}{2}>{3}'.format(inputChr, inputPos, inputRef, inputAlt),
                  'variant_type': inputType
                  }

    return outputKey, outputDict
