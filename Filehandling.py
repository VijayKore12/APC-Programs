f = open("demo.txt", "w")  
f.write("My name is Vijay...")
f.close()


f = open("Demo.txt", "r") 
data = f.read()
print("File have :", data)
f.close()


f = open("Demo.txt", "a")
f.write("I am an Engineering Student...")
f.close()



