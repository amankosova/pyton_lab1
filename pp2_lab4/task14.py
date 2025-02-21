import json
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
with open ("sample-data.json") as i:
    data=json.load(i)
a=data["imdata"][0]["l1PhysIf"]["attributes"]["dn"]
b=data["imdata"][0]["l1PhysIf"]["attributes"]["speed"]
c=data["imdata"][0]["l1PhysIf"]["attributes"]["mtu"]
print(a,"                              ",b,"   ",c)
a1=data["imdata"][1]["l1PhysIf"]["attributes"]["dn"]
b1=data["imdata"][1]["l1PhysIf"]["attributes"]["speed"]
c1=data["imdata"][1]["l1PhysIf"]["attributes"]["mtu"]
a2=data["imdata"][2]["l1PhysIf"]["attributes"]["dn"]
b2=data["imdata"][2]["l1PhysIf"]["attributes"]["speed"]
c2=data["imdata"][2]["l1PhysIf"]["attributes"]["mtu"]
print(a1,"                              ",b1,"   ",c1)
print(a2,"                              ",b2,"   ",c2)

"""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 
"""