#!/usr/bin/python3

# Format
# 00: Allele
# 01: Consequence
# 02: IMPACT
# 03: SYMBOL
# 04: Gene
# 05: Feature_type
# 06: Feature
# 07: BIOTYPE
# 08: EXON
# 09: INTRON
# 10: HGVSc
# 11: HGVSp
# 12: cDNA_position
# 13: CDS_position
# 14: Protein_position
# 15: Amino_acids
# 16: Codons
# 17: Existing_variation
# 18: DISTANCE
# 19: STRAND
# 20: FLAGS
# 21: PICK
# 22: SYMBOL_SOURCE
# 23: HGNC_ID
# 24: CANONICAL
# 25: HGVS_OFFSET

def checkCsq(inputInfo):

    outputDict = {}
    outputTranscript = {}
    outputTranscriptNum = 0

    for num in range(len(inputInfo)):
        oneTranscript = inputInfo[num].split('|')
        oneDict = {}

        if not oneTranscript[5] == 'Transcript':
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
            oneDict['exon_num'] = int(oneTranscript[8].split('/')[0].lower())
            oneDict['exon_total'] = int(oneTranscript[8].split('/')[1].lower())
        if not oneTranscript[9] == '':
            oneDict['intron_num'] = int(oneTranscript[9].split('/')[0].lower())
            oneDict['intron_total'] = int(oneTranscript[9].split('/')[1].lower())
        if not oneTranscript[10] == '':
            if oneTranscript[10].split(':')[1][0] == 'c':
                oneDict['hgvs.c'] = oneTranscript[10].split(':')[1]
            elif oneTranscript[10].split(':')[1][0] == 'n':
                oneDict['hgvs.n'] = oneTranscript[10].split(':')[1]
        if not oneTranscript[11] == '':
            oneDict['hgvs.p'] = oneTranscript[11].split(':')[1]
        if oneTranscript[19] == 1:
            oneDict['strand'] = '+'
        elif oneTranscript[19] == -1:
            oneDict['strand'] = '-'

        if oneTranscript[24] == 'YES':
            outputDict['canonical_transcript'] = oneDict['transcript_id']
            outputDict['canonical_gene'] = oneDict['gene']
            outputDict['canonical_consequence'] = oneDict['consequence']

        if not oneDict == {}:
            outputTranscript[str(outputTranscriptNum)] = oneDict
            outputTranscriptNum = outputTranscriptNum +1

    if not outputTranscript == {}:
        outputDict['transcript'] = outputTranscript

    return outputDict