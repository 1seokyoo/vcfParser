#!/usr/bin/python3

import vcf

def checkGnomad(inputInfo):
    
    outputDict = {}
    populationsDict = {'ALL': 'All',
                       'AFR': 'African',
                       'AMI': 'Amish',
                       'AMR': 'Admixed American',
                       'ASJ': 'Ashkenazi Jewish',
                       'EAS': 'East Asian',
                       'FIN': 'Finnish',
                       'NFE': 'Non-Finnish European',
                       'OTH': 'Others',
                       'SAS': 'South Asian'
                      }

    for key in populationsDict.keys():
        oneKey = 'gnomAD_AF_{0}'.format(key)
        oneDec = populationsDict[key].replace(' ','_').lower()

        if oneKey in inputInfo:
            oneFreq = inputInfo[oneKey][0]
            outputDict[oneDec] = {'allele_frequency': oneFreq,
                                  'code': key,
                                  'population': populationsDict[key]
                                 }

    return outputDict


def check1kgp(inputInfo):
    
    outputDict = {}
    populationsDict = {'ALL': 'All',
                       'AFR': 'African',
                       'AMR': 'American',
                       'EAS': 'East Asian',
                       'EUR': 'European',
                       'SAS': 'South Asian'
                      }

    for key in populationsDict.keys():
        oneKey = '1KGP_{0}_AF'.format(key)
        oneDec = populationsDict[key].replace(' ','_').lower()

        if oneKey in inputInfo:
            oneFreq = inputInfo[oneKey]
            outputDict[oneDec] = {'allele_frequency': oneFreq,
                                  'code': key,
                                  'population': populationsDict[key]
                                 }

    return outputDict