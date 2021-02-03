from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.SeqFeature import SeqFeature, FeatureLocation
from Bio import SeqIO

sequence = Seq('TCGATCAGCTAGCATGCATCA')#sequencia de DNA
print(sequence.complement()) #complemento da sequencia acima
print(sequence.reverse_complement()) #sequencia complementar lida no sentido oposto
print(sequence.transcribe()) #sequencia de RNA equivalente
print(sequence.translate()) # traduzindo como se fossem códons
print(sequence[0:4]) #separando parte da sequencia

sequence= Seq('ATGGCAAAAGAGTGA')
features= [
    SeqFeature(FeatureLocation(0,15,strand=1),type='gene', qualifiers={'locus_tag':['omx_0001'],'gene':['omX']})
]

record= SeqRecord(
    sequence,
    id='OMX0001.1',
    name='omX',
    description='omixicin',
    annotations={'molecule_type':'DNA'},
    features=features
)
print(record)
print(record.format('genbank'))

with open('annotation.gb', 'w') as writer:
    SeqIO.write([record], writer,'genbank')
writer.close()

with open('annotation.gb', 'r') as reader:
    parser=SeqIO.parse(reader,'genbank')
    for record in parser:
        print(record.id)
        for feature in record.features:
            print(feature.type, feature.location.start,
            feature.location.end)