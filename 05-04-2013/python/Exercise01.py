from pyplasm import *

#function for round pillars
def roundPillar():
    pillar = CYLINDER([1.25,26])(36)
    centeredPillar = T([1,2])([1.25,1.25])(pillar)
    return centeredPillar

#function GRID    
GRID = COMP([INSR(PROD),AA(QUOTE)])

#pillars 0
roundPillars0 = STRUCT(NN(5)([roundPillar(),T([1])([27.5])]))
roundPillars0a = T([2])([50])(roundPillar())
roundPillars0b = T([1,2])([110,50])(roundPillar())
squarePillars0 = GRID([[-13.75, 2.5, -11.25, 2.5, -25, 2.5, -25, 2.5, -25], [-50, 2.5, -12.5], [-1,25]])
pillars0 = STRUCT([squarePillars0,roundPillars0,roundPillars0a,roundPillars0b])

#pillars 1
squarePillarsLine1AA = GRID([[2.5,-25,2.5],[2.5],[-27,49]])#fila sotto
squarePillarsLine1AB = GRID([[-2.5,-25,-2.5,-25,2.5,-25,2.5,-25,2.5],[2.5],[-27,24]])#fila sotto
squarePillarsLine1BA = GRID([[2.5,-25,2.5],[-50,2.5],[-27,49]])#fila sopra
squarePillarsLine1BB = GRID([[-2.5,-25,-2.5,-25,2.5,-25,-2.5,-25,2.5],[-50,2.5],[-27,24]])#fila sopra
roundPillar1t = T([1,2,3])([2.5+25+2.5+25+2.5+25+1.25,50+1.25,27])(CYLINDER([1.25,24])(36))
pillars1 = STRUCT([squarePillarsLine1AA,squarePillarsLine1AB,squarePillarsLine1BA,squarePillarsLine1BB,roundPillar1t])

#pillars 2
squarePillars2a = GRID([[-55, 2.5, -52.5, 2.5], [2.5, -62.5], [-52, 24, -26]])
squarePillars2b = GRID([[-55, 2.5, -25, 2.5, -25, 2.5], [-50, 2.5, -12.5], [-52, 24, -26]])
pillars2 = STRUCT([squarePillars2a,squarePillars2b])

#pillars 3
smallSquarePillars3a = GRID([[1.25, -111.25], [1.25, -62.5], [-77, 23, -2]])
smallSquarePillars3b = GRID([[1.25, -26.25, 1.25], [-51.25, 1.25], [-77, 23, -2]])
squarePillars3a = GRID([[-55, 2.5, -52.5, 2.5],[2.5, -47.5, 2.5],[-77, 23, -2]])
squarePillars3b = GRID([[-55, 2.5, -25, 2.5, -25, 2.5],[-50, 2.5],[-77, 23, -2]])
pillars3 = STRUCT([squarePillars3a,squarePillars3b,smallSquarePillars3a,smallSquarePillars3b])

#the groups of pillars are organized in a STRUCT
pillars = STRUCT ([pillars0,pillars1,pillars2,pillars3])

VIEW(pillars)