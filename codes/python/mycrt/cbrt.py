def crt(x,debug=False):
	
	
	if specialCases:
		if x==0.:
			return 0.
			
	
	s=1.00
	kmax=100
	tol=1.0e-10
	for k in range(kmax):
		if debug:
			print("iteration number %s, s= %12.10f" %(k,s))
		s0=s
		s = 0.33333*((2.00*s)+(x/(s**2)))
		delta_s=s-s0
		if(abs(delta_s/x))<tol:
	
	
			break
	if debug:
		print("After %s iterations,  s=%12.10f" %(k+1,s))
	return s



def test_main():
	from numpy import cbrt
	xvalues=[0.00, 27.00, 1000.00, -1331]
	for x in xvalues:
		print("Testing with x=%12.10e" %x)
		s=crt(x)
		s_numpy=cbrt(x)
		print("crt s = %12.10e, numpy s = %12.10e" %(s,s_numpy))
		assert abs(s-s_numpy) < 1e-14, "Your cube root does not agree with numpy cuberoot"
