
''' forma no optimizada '''
cs = [(a,b,c) for a in range(1, 10) for b in range(1, 10) for c in range(1, 10) if int(str(a)+str(b)+str(c))*3 == int(str(c)+str(c)+str(c)) ]
print(cs)


''' forma optimizada ''' 

vc = [c for c in range(1, 10) if str(3*c).endswith(str(c))]

va = [str(37*i)[0] for i in vc if 37*i>=100 ]

vb = [str(37*i)[1] for i in vc if 37*i>=100 ]



for j in range(len(vc)) :
	
	print(f"solucion {j+1} :  A = {va[j]}  B = {vb[j]}  C = {vc[j]} ")
	
