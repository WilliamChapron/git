
def c(x,y,z,w)
  return x+y,z-w
print(c(1,2,3,4))


def add(x,y)
  return x+y

def sub(x,y)
  return x-y
print(sub(5,5))

def multiply(x,y)
  return x*y
print(multiply(5,5))

def divide(x,y)
  return x/y
print(divide(5,5))

def calculSalaireParSeconde(salaireHoraire,heureParJour,nbJour)
  return (((salaireHoraire*heureParJour*nbJour)/360)/24)/3600

print(calculSalaireParSeconde(15,10,260))

def CalculSalaireNet(SalaireBrut,Coeff)
  return SalaireBrut * (1-Coeff)


print(CalculSalaireNet(1000,0.24))