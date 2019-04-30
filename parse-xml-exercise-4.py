import xml.etree.ElementTree as ET

tree = ET.parse('opencim3sub.xml')
root = tree.getroot()

cim = "{http://iec.ch/TC57/2008/CIM-schema-cim14#}"
rdf = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"

for sub in root.iter(cim+'Substation'):
  print(sub.get(rdf+'ID'))
  for name in sub.iter(cim+'IdentifiedObject.name'):
    print(name.text)

print('\n')

for voltage_level in root.iter(cim+'VoltageLevel'):
  print(voltage_level.get(rdf+'ID'))
  for name in voltage_level.iter(cim+'IdentifiedObject.name'):
    print(name.text)

print('\n')

for synchronous_machine in root.iter(cim+'SynchronousMachine'):
  print(synchronous_machine.get(rdf+'ID'))
  for name in synchronous_machine.iter(cim+'IdentifiedObject.name'):
    print(name.text)
