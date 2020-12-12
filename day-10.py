data = [ 128, 6, 152, 16, 118, 94, 114, 3, 146, 44, 113, 83, 46, 40, 37, 72, 149, 155, 132, 9, 75, 1, 82, 80, 111, 124, 66, 122, 129, 32, 30, 136, 112, 65, 90, 117, 11, 45, 161, 55, 135, 17, 159, 38, 51, 131, 12, 123, 81, 64, 50, 43, 19, 63, 13, 153, 110, 27, 23, 104, 145, 18, 125, 86, 10, 76, 26, 142, 59, 47, 160, 79, 139, 54, 121, 97, 162, 36, 107, 56, 25, 99, 24, 31, 69, 137, 33, 138, 130, 158, 91, 2, 74, 101, 73, 20, 98, 154, 89, 62, 100, 39 ]
#data = [ 16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4 ]
#data = [ 28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3 ]
size = len(data)


## part one ##
cur = 0
data.sort()

i = 0
diffs = {1:0, 2:0, 3:0}
while True:
  diff = data[i] - cur;
  diffs[diff] += 1

  cur = data[i]
  i += 1

  if i >= size:
    # the last diff is 3, going to the final device
    diffs[3] += 1
    break

print( diffs[1] * diffs[3] )

## part two ##
data.sort(reverse=True)

adapters = dict()
for d in data:
  adapters[d] = [set(), set(), 0] # [ parents, children, "score" ]
  # "score" is the number of paths stemming from this adapter (which is the sum of all its parents' scores)

adapters[data[0]][2] = 1 # highest value adapter always has 1 parent, the final device

i = 0
while i < size:
  cur = data[i]

  # see if any of the next 3 adapters are within 3 volts
  for j in [1,2,3]:
    if i+j >= size:
      break

    test = data[i+j]
    if cur - test <= 3:
      # its a child
      adapters[cur][1].add(test)
      # set the parent
      adapters[test][0].add(cur)
      
    else:
      break

  i += 1

# all parents and children are constructed
# now "score" each node
for volts, adapter in sorted( adapters.items(), reverse=True ):
  for parent in adapter[0]:
    adapter[2] += adapters[parent][2]

# any adapters of value 1, 2, or 3 can reach the 0 volt charging outlet
total = 0
for i in [1,2,3]:
  if i in adapters:
    total += adapters[i][2]

print( total )


