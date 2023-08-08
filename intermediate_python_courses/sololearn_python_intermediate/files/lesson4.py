with open("books.txt") as f:
   lines=f.readlines()
   x=0
   for i in lines:
      x+=1
      words=i.split()
      print(f'Fline {x}: {len(words)} words')
   