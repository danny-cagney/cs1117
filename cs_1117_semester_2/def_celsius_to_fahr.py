def celsius_to_fahr (temp_c):
    """This function is to convert celsius to fahrenheit"""
    #Returns the fahrenheit equivalent of a given celsius temperature
    temp_f = temp_c * 9 / 5 + 32
    return temp_f

#Main Program
temp = float(input("Enter temperature in Celsius: "))
convertedTemp = celsius_to_fahr (temp)
print ("Equivalent temperature in fahrenheit is: ", convertedTemp)

#print 