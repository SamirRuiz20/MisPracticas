import re


a = re.compile(r"(?P<tipo>clase)")

print(a.search("y Laclasec").group("tipo"))

b = re.match(r"([cba])+", "cba")
print(b.groups(), b)


InternalDate = re.compile(r'INTERNALDATE  '
        r'(?P<day>[ 123][0-9])-(?P<mon>[A-Z][a-z][a-z])-'
        r'(?P<year>[0-9][0-9][0-9][0-9])'
        r' (?P<hour>[0-9][0-9]):(?P<min>[0-9][0-9]):(?P<sec>[0-9][0-9])'
        r' (?P<zonen>[-+])(?P<zoneh>[0-9][0-9])(?P<zonem>[0-9][0-9])'
        )
print(InternalDate)
        
        
x = re.compile(".*[.]([^b]..|.[^a].|..[^t])$")

print(x.search("hola.ba"))

m = re.compile(".*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$")

print(m.search("hola.ba") ) 	


p = re.compile(".*[.](?=bat$)([^.]*$)")

print(p.search("hola.bat"))
  
        


g = re.compile(r"[.^]+")
print(g.search(""))	

b = re.compile(r"x*")
print(b.sub("-", "abxd"))


p = re.compile('section{ ( [^}]* ) }', re.VERBOSE)

print(p.sub(r'subsection{\1}','section{First} section{second}'))
		