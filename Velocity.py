if state = 'liquid':
	valveVelocity = 353.7(Q/di*di)
else:
	valveVelocity = 1,296*Qn*(T1/(di*di*p2))

return valveVelocity


'''where:

Q is fluid flowrate in M3H/HR

Qn is gas flowrate

T1 is the inlet temparature

di is the nominal valve diameter

'''
