#!/usr/bin/python3

def checkClinvar(inputInfo):

    outputDict = {}
    clinvarReveiwStatus = {'criteria_provided,_conflicting_interpretations': 1,
                           'criteria_provided,_multiple_submitters,_no_conflicts': 2,
                           'criteria_provided,_single_submitter': 1,
                           'no_assertion_criteria_provided': 0,
                           'no_assertion_provided': 0,
                           'no_interpretation_for_the_single_variant': 0,
                           'practice_guideline': 4,
                           'reviewed_by_expert_panel': 3
                           }

    if 'CLNSIG' in inputInfo:
        outputDict['classification'] = inputInfo['CLNSIG'][0]
    if 'CLNREVSTAT' in inputInfo:
        outputDict['reveiw_status'] = inputInfo['CLNREVSTAT'][0]
        outputDict['star'] = clinvarReveiwStatus[outputDict['reveiw_status']]
    if 'CLNVC' in inputInfo:
        outputDict['variant_type'] = inputInfo['CLNVC']
    if 'CLNID' in inputInfo:
        outputDict['id'] = inputInfo['CLNID']
    if 'CLNDN' in inputInfo:
        outputDict['disease_name'] = inputInfo['CLNDN'][0].replace('|',',')

    return outputDict


def checkCosmic(inputInfo):

    outputDict = {}

    if 'COSMIC_ID' in inputInfo:
        outputDict['id'] = inputInfo['COSMIC_ID']
    if 'COSMIC_CNT' in inputInfo:
        outputDict['count'] = inputInfo['COSMIC_CNT']
    if 'COSMIC_OCCURENCE' in inputInfo:
        outputDict['occurence'] = inputInfo['COSMIC_OCCURENCE'][0].replace('|',',')

    return outputDict