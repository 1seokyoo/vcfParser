#!/usr/bin/python3

import vcf

def checkAllele(inputSample):

    outputDict = {}

    if not inputSample['AD'] == '':
        outputDict['reference_allele_observation'] = int(inputSample['AD'][0])
        outputDict['alternate_allele_observation'] = int(inputSample['AD'][1])
        outputDict['total_read_depth'] = outputDict['reference_allele_observation'] + outputDict['alternate_allele_observation']
        outputDict['allele_fraction'] = round((outputDict['alternate_allele_observation'] / outputDict['total_read_depth']) * 100, 2)

    if not inputSample['GT'] == '':
        if inputSample['GT'] == '0/0':
            outputDict['zygosity'] = 'reference_homozygous'
        if inputSample['GT'] == '0/1':
            outputDict['zygosity'] = 'heterozygous'
        if inputSample['GT'] == '1/1':
            outputDict['zygosity'] = 'alternate_homozygous'

    return outputDict