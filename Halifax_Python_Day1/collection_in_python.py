# tuple, set, dictionary
t_1 = () # empty
t_2 = tuple();
t_3 = (1,4,7,9,True,"One")
l_1 = [1,3,6,8]
t_4 = tuple(l_1)
#t_4[0] = 100 error of assignment

x, y, z = (3,6,7) # unpacking
print(x)
# Set
s_1 = {2,3,4,4,5,5,6,6,6,7} 
print(type(s_1))
print(s_1)

l_2 = ["one","two","one",1,1,5,7,9,9]
s_2 = set(l_2)
print(s_2)

#Dictionary
d_1 = {"one":1,"two":2}
print(d_1["one"])
d_1["name"] = "Mary"
d_1["age"] = 25
print(d_1)