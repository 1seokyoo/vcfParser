#!/usr/bin/python3

# Format
# 00: Allele
# 01: Annotation
# 02: Annotation_Impact
# 03: Gene_Name
# 04: Gene_ID
# 05: Feature_Type
# 06: Feature_ID
# 07: Transcript_BioType
# 08: Rank
# 09: HGVS.c
# 10: HGVS.p
# 11: cDNA.pos/cDNA.length
# 12: CDS.pos/CDS.length
# 13: AA.pos/AA.length
# 14: Distance
# 15: ERRORS/WARNINGS/INFO

def checkAnn(inputInfo):

    outputDict = {}
    outputTranscript = {}
    outputTranscriptNum = 0

    for num in range(len(inputInfo)):
        oneTranscript = inputInfo[num].split('|')
        oneDict = {}

        if not oneTranscript[5] == 'transcript':
            continue
        if not oneTranscript[7] == 'protein_coding':
            continue
        
        if not oneTranscript[1] == '':
            oneDict['consequence'] = oneTranscript[1].lower()
        if not oneTranscript[2] == '':
            oneDict['impact'] = oneTranscript[2].lower()
        if not oneTranscript[3] == '':
            oneDict['gene'] = oneTranscript[3]
        if not oneTranscript[6] == '':
            oneDict['transcript_id'] = oneTranscript[6]
        if not oneTranscript[8] == '':
            oneDict['exon/intron_num'] = int(oneTranscript[8].split('/')[0].lower())
            oneDict['exon/intron_total'] = int(oneTranscript[8].split('/')[1].lower())
        if not oneTranscript[9] == '':
            oneDict['hgvs.c'] = oneTranscript[9]
        if not oneTranscript[10] == '':
            oneDict['hgvs.p'] = oneTranscript[10]

        if not oneDict == {}:
            outputTranscript[str(outputTranscriptNum)] = oneDict
            if outputTranscriptNum == 0:
                outputDict['canonical_transcript'] = oneDict['transcript_id']
                outputDict['canonical_gene'] = oneDict['gene']
                outputDict['canonical_consequence'] = oneDict['consequence']
    
            outputTranscriptNum = outputTranscriptNum +1

    if not outputTranscript == {}:
        outputDict['transcript'] = outputTranscript

    return outputDict