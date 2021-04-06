from bluepy.btle import Peripheral, UUID 
from bluepy.btle import Scanner, DefaultDelegate 
class ScanDelegate(DefaultDelegate): 
  def __init__(self): 
    DefaultDelegate.__init__(self) 
  def handleDiscovery(self, dev, isNewDev, isNewData): 
    if isNewDev: 
      print "Discovered device", dev.addr 
    elif isNewData: 
      print "Received new data from", dev.addr
      
scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(1.0)
n=0
for dev in devices: 
  print "%d: Device %s (%s), RSSI=%d dB" % (n, dev.addr, dev.addrType, dev.rssi) 
  n += 1
  for (adtype, desc, value) in dev.getScanData(): 
    print " %s = %s" % (desc, value) 
number = input('Enter your device number: ') 
print('Device', number) 
print(devices[number].addr) 
print "Connecting..." 
dev = Peripheral(devices[number].addr, 'random')
 
print "Services..." 
for svc in dev.services: 
  print str(svc)
print "\n%s\nRunning..." % (dev.services[2])
if dev.services[2].uuid == 0xb000:  
  try:
    idService = dev.getServiceByUUID(UUID(0xb000))
    for uuid in [0xb001, 0xb002, 0xb003]: 
      ch = dev.getCharacteristics(uuid=UUID(uuid))[0]
      print ''.join(ch.read())
  finally:
    dev.disconnect()  
elif dev.services[2].uuid == 0xa000:
  try:   
    buttonService = dev.getServiceByUUID(UUID(0xa000)) 
    ch = dev.getCharacteristics(uuid=UUID(0xa001))[0]
    counter = 1
    present = past = 0
    while counter < 100:
      present = ord(ch.read())
      if present == 1 and past == 0:
        print "Button Pressed."  
      past = present  
      counter += 1  
  finally:
    dev.disconnect()  
else:
  print "Error"  

'''
try:   
  testService = dev.getServiceByUUID(UUID(0xa000)) 
  for ch in testService.getCharacteristics(): 
    print str(ch) 
  ch = dev.getCharacteristics(uuid=UUID(0xa001))[0]
  if (ch.supportsRead()): 
    print ch.read() 
finally:
  
'''  