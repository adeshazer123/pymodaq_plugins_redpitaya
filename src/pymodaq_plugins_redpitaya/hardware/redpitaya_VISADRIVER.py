import logging
import pyvisa 
logger = logging.getLogger(__name__)


# things we need: 
# - reset method 
# - get the device ID
# - get frequency
# - set frequency
# - get amplitude
# - set amplitude
# - get offset
# - set offset
# - get voltage 
# - set voltage
# - open the device
# - close the device
# - get the device status 

class REDPITAYAVISADRIVER:
    """ Class to control the Red Pitaya VISA device. Controls through SPCI commands
        Check the Red Pitaya documentation for more information.""" 
    
    def __init__(self, resource_name): 
        self.resource_name = resource_name
        self.rm = pyvisa.ResourceManager()
        self.device = self.rm.open_resource(self.resource_name)
        

    def reset(self): 
        """ Reset the device and sets to default values"""
    
    