"""You are working at Met Eireann. Their climatology software system needs  to add a feature 
relating to the wind chill index.  
 
When  the  wind  blows  in  cold  weather  the  air  feels  cooler  than  it  actually  is  because  the 
movement of air increases the rate of cooling for warm objects (like people). This is known as 
wind chill. In 2001, a formula was adopted for computing the wind chill index.  
 
WCI = 13.12 + 0.6215Ta − 11.37V0.16 + 0.3965TaV0.16 
 
Ta is the air temperature in degrees Celsius and V is the wind speed in kilometres per 
hour."""

#TempAir (variable) is the air temperature in degrees Celsius
TempAir = float(input("Enter Air Temperature in Celsius:"))

#Vel (variable) is the wind speed in kilometres per hour. 
Vel = float(input("Enter Wind Speed in kilometres per hour:"))

WindChillIndex = ( 13.12 + 0.6215*TempAir - 11.37*(Vel**0.16) + (0.3965*(TempAir*(Vel**0.16))))

#converting to the nearest integer, we call the round function 
print (int(round(WindChillIndex)))


def calcWindChillIndex(Ta, V):
    """calcWindChillIndex is a function that  expects  two  input  parameters
    - Param_1 = Ta - Air  temperature
    - Param_2 = V - Wind speed function should be invoked and print the result. 
    - Returns  the  wind  chill  index  rounded  to  the  closest  integer."""

    #TempAir (variable) is the air temperature in degrees Celsius
    TempAir = float(Ta)

    #Vel (variable) is the wind speed in kilometres per hour. 
    Vel = float(V)

    #Wind Chill Index is calcualted using the input parameters, and the given equation
    WindChillIndex = ( 13.12 + 0.6215*TempAir - 11.37*(Vel**0.16) + (0.3965*(TempAir*(Vel**0.16))))

    #converting to the nearest integer, we call the round function 
    return (int(round(WindChillIndex)))

# Invoke the function using the print, when the function returns output. 
# When the print function is contained within the function, just call / invoke the function without print
# Otherwise print will return "None" by default.

print(calcWindChillIndex(10,10))
