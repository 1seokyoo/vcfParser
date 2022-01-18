#!/usr/bin/python3

import vcf
from src.checkCoordinate import checkCoordinate
from src.checkAllele import checkAllele
from src.checkAnn import checkAnn
from src.checkCsq import checkCsq
from src.checkPopulationFreq import check1kgp, checkGnomad
from src.checkClinical import checkClinvar, checkCosmic

def parseRecord(inputRecord):

    outputDict = {}

    outputKey, tmpDict = checkCoordinate(inputRecord)
    if not tmpDict == {}: outputDict['genomic_coordinate'] = tmpDict

    tmpDict = checkAllele(inputRecord.samples[0])
    if not tmpDict == {}: outputDict['allele'] = tmpDict

    inputInfoKey = inputRecord.INFO.keys()
    # check transcript - SnpEff(RefSeq) & VEP(Ensembl)
    if 'ANN' in inputInfoKey:
        tmpDict = checkAnn(inputRecord.INFO['ANN'])
        if not tmpDict == {}: outputDict['refseq'] = tmpDict

    if 'CSQ' in inputInfoKey:
        tmpDict = checkCsq(inputRecord.INFO['CSQ'])
        if not tmpDict == {}: outputDict['ensembl'] = tmpDict

    # check population frequency - 1KGP, gnomAD
    populationFrequency = {}
    if '1KGP_ALL_AF' in inputInfoKey:
        tmpDict = check1kgp(inputRecord.INFO)
        if not tmpDict == {}: populationFrequency['1kgp'] = tmpDict
    if 'gnomAD_AF_ALL' in inputInfoKey:
        tmpDict = checkGnomad(inputRecord.INFO)
        if not tmpDict == {}: populationFrequency['gnomad'] = tmpDict
    if not populationFrequency == {}: outputDict['population_frequency'] = populationFrequency

    # check clinical database - clinvar
    clincal = {}
    if 'CLNID' in inputInfoKey:
        tmpDict = checkClinvar(inputRecord.INFO)
        if not tmpDict == {}: clincal['clinvar'] = tmpDict
    if 'COSMIC_ID' in inputInfoKey:
        tmpDict = checkCosmic(inputRecord.INFO)
        if not tmpDict == {}: clincal['cosmic'] = tmpDict
    if not clincal == {}: outputDict['clincal'] = clincal

    return outputKey, outputDict