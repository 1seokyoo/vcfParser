#!/usr/bin/python3

import sys
import vcf
import os
import re
import json
import argparse
from src.parseRecord import parseRecord

class VcfParser(object):

    def __init__(self, inputName, outputName):

        self._inputName = inputName
        self._outputName = outputName

    def run(self):
        
        outputJson = {}
        
        inputReader = vcf.Reader(open(self._inputName, 'r'))
        for i, record in enumerate(inputReader):
            oneKey, oneDict = parseRecord(record)
            outputJson[oneKey] = oneDict

        outputFile = open(self._outputName,"w")
        for key in sorted(outputJson.keys(), key=str.lower):
            tmpJson={}
            tmpJson[key]=outputJson[key]
            tmpJson=json.dumps(tmpJson, sort_keys=True)
            outputFile.write(tmpJson+"\n")

        outputFile.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='BreaKmer Output Filtering')
    parser.add_argument('-i', '--input', type=str, help='Input vcf file name')
    parser.add_argument('-o', '--output', type=str, help='Output json file name')
    args = parser.parse_args()

    myWorkflow=VcfParser(args.input, args.output)
    myWorkflow.run()