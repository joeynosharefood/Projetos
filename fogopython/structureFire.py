heightFire = widthFire = 5
temp = list()
boxFire = list()

boxArea = heightFire * widthFire
for c in range(0, boxArea):
   temp.append(0)
   temp.append(c)
   boxFire.append(temp[:])
   temp.clear()
for k in range(0, boxArea):
   print(boxFire[k], end='')
   if k+1 == widthFire:
      widthFire += widthFire