try:
    x=7       
    print(x)
except NameError:
    print("define x")
except:
    print("an error occured") 
else: #error illatha samaunna blockath work ava
    print("no exception")
finally: #work error ondegilum illegilum
    print("worked successfully")   

#     
s=-2
if s<0:
    raise Exception("num less than 0 not accepted")


