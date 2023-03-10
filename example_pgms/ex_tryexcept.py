def tryfunc(divideby):
        try:
            return 42/divideby
        except:
            print("you entered unexpected value")

print(tryfunc(2))
print(tryfunc(3))
print(tryfunc(0))
print(tryfunc(4))
