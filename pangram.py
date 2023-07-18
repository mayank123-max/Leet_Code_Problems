s = "qmExzBIJmdELxyOFWv LOCmefk TwPhargKSPEqSxzveiun"
s = s.lower()
d = {}
for i in s:
    d[i] = d.get(i,0)+1
if len(d) == 27:
    print("pangram")
else:
    print("not pangram")