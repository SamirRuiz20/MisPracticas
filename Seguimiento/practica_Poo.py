import operator
from fractions import Fraction
import numbers as nbs

def opera( x, y ) :
	
	def forward(a, b) :
		
		if isinstance(b, (int, Fraction )) :
			print("__")
			return x(a, b)
			
		elif isinstance(b, float) :
			
			return y(float(a), b)
			
		elif isinstance(b, complex) :
			
			return y(complex(a), b)
			
		else :
			
			return NotImplemented 
			
			
			
	forward.__name__ = "_" + y.__name__ + "_"
	forward.__doc__ = x.__doc__ 
	
	def reverse(b, a) :
		
		if isinstance(a, nbs.Rational) :
			print("_")
			return x(a, b)
			
		elif isinstance( a, nbs.Real ) :
			
			return y(float(a), float(b))
			
		elif isinstance(a, nbs.Complex) :
			
			return y(complex(a), complex(b))
			
		
		else :
			
			return NotImplemented
			
	reverse.__name__ = "_" + y.__name__ + "_"
	reverse.__doc__ = x.__doc__
	
	return forward , reverse
	
	
	
def _add( a, b) :
	
	''' Return La Fraccion a/b '''
	
	return Fraction( a.numerator*b.denominator + b.numerator*a.denominator )

#x = _add(6, 7) 

__add__, __radd__ = opera(_add, operator.add)

print(__radd__.__doc__)