a={"a",'b','c','g'}
b={'j','k','g','b'}
c={'m','n','a','b'}

rep= len(a.intersection(b))+ len(a.intersection(c))+len(b.intersection(c))

unique= (a.symmetric_difference(b).union((b.symmetric_difference(c)).union((a.symmetric_difference(c))
