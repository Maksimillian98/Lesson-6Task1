N = int(input('Vvedite koli4estvo 4isel: '))
count_null = 0
for i in range(N):
   P = int(input('ccedite celoe 4islo: '))
   if P == 0:
       count_null += 1
print(f"koli4estvo nulley= {count_null}")