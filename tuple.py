str1=input("Enter first String with space :: ")
print(str1.split()) #splits at space
str2=input("Enter second String with (,) :: ")
print(str2.split(',')) #splits at ','
str3=input("Enter third String with (:) :: ")
print(str3.split(':')) #splits at ':'
str4=input("Enter fourth String with (;) :: ")
print(str4.split(';')) #splits at ';'
str5=input("Enter fifth String without space :: ")
print([str5[i:i+2]for i in range(0,len(str5),2)]) #splits at position2