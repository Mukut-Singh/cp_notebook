t='pqrst'
a=list(t)
print(a[0])


#output techniques
results = ['10', '5', '4']

# "Glue" them with a newline
final_string = '\n'.join(results)

The result is ONE single string:
"10\n5\n4"

#" ".join(results) >Puts a space between items: "10 5 4"
#"\n".join(results) > Puts a new line between items: 
10
5
4
",".join(results) >Puts a comma between items: "10,5,4
# print(*results) is interpreted by Python as:
print('10', '5', '4')

10 5 4   <-- Clean output, no brackets!
Why use it? It's lazy and convenient! It works with integers too (unlike .join). If you want newlines, you combine it with sep:
print(*results, sep='\n') 
Equivalent to: print('10', '5', '4', sep='\n')
you used sys.stdout.write. This function is "dumb"—it only accepts one single string. It doesn't know how to unpack *or handle lists. That is why you must use .join() to turn your list into that single string first.
for x in results: print(x)  NEVER USE THIS
