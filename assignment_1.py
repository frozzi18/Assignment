print('hello')

class base_voltage:
  def __init__(self, rdf_ID, nominal_value):
    self.rdf_ID = rdf_ID
    self.nominal_value = nominal_value

class substation:
  def __init__(self, rdf_ID, 
  name, region_rdf_ID):
    self.rdf_ID = rdf_ID
    self.name = name
    self.region_rdf_ID = region_rdf_ID

class voltage_level:
  def __init__(self, rdf_ID, name, substation_rdf_ID, base_voltage_rdf_ID):
    self.rdf_ID = rdf_ID
    self.name = name
    self.substation_rdf_ID = substation_rdf_ID
    self.base_voltage_rdf_ID = base_voltage_rdf_ID

class generating_unit:
   def __init__(self, rdf_ID, name, max_P, min_P,  equipment_container_rdf_ID):
    self.rdf_ID = rdf_ID
    self.name = name
    self.max_P = max_P
    self.min_P = min_P
    self.equipment_container_rdf_ID = equipment_container_rdf_ID

class synchronous_machine:
  def __init__(self, rdf_ID, name, rated_S, active_power, reactive_power, 
  generator_unit_rdf_ID, reg_control_rdf_ID, equipment_container_rdf_ID,
  base_voltage_rdf_ID):
    self.rdf_ID = rdf_ID
    self.name = name
    self.rated_S = rated_S
    self.active_power = active_power
    self.reactive_power = reactive_power
    self.generator_unit_rdf_ID = generator_unit_rdf_ID
    self.equipment_container_rdf_ID = equipment_container_rdf_ID
    self.base_voltage_rdf_ID = base_voltage_rdf_ID

class regulating_control:
  def __init__(self, rdf_ID, target_value):
    self.rdf_ID = rdf_ID
    self.name = name
    self.target_value = target_value
   

class power_transformer:
  def __init__(self, rdf_ID, equipment_container_rdf_ID):
    self.rdf_ID = rdf_ID
    self.name = name
    self.equipment_container_rdf_ID = equipment_container_rdf_ID 

class energy_consumer_load:
  def __init__(self, rdf_ID, name, active_power, reactive_power, 
  equipment_container_rdf_ID, base_voltage_rdf_ID):
    self.rdf_ID = rdf_ID
    self.name = name
    self.active_power = active_power
    self.reactive_power = reactive_power
    self.equipment_container_rdf_ID = equipment_container_rdf_ID
    self.base_voltage_rdf_ID = base_voltage_rdf_ID

class power_transformer_end_transformer_winding:
  def __init__(self, rdf_ID, name, transformer_r, transformer_x, 
  transformer_rdf_ID, base_voltage_rdf_ID):
    self.rdf_ID = rdf_ID
    self.name = name
    self.transformer_r= transformer_r
    self.transformer_x = transformer_x
    self.transformer_rdf_ID = transformer_rdf_ID
    self.base_voltage_rdf_ID = base_voltage_rdf_ID

class breaker:
  def __init__(self, rdf_ID, name, state, equipment_container_rdf_ID, 
  base_voltage_rdf_ID):
    self.rdf_ID = rdf_ID
    self.name = name
    self.state = state
    self.equipment_container_rdf_ID = equipment_container_rdf_ID
    self.base_voltage_rdf_ID = base_voltage_rdf_ID

class breaker:
  def __init__(self, rdf_ID, name, step):
    self.rdf_ID = rdf_ID
    self.name = name
    self.step = step

                                                                                                     
import xml.etree.ElementTree as ET

tree_EQ = ET.parse('Assignment_EQ_reduced.xml')
tree_SSH = ET.parse('Assignment_SSH_reduced.xml')

root_EQ = tree_EQ.getroot()
root_SSH = tree_SSH.getroot()

print(root_EQ.tag, root_SSH.tag)
