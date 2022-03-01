"""Q3. Assume  you  have  a  list  called  counties  and  a  list  called  population.  The  positions  in  each  list 
correspond to each other e.g. Cork has a population of 190384, Dublin 1.228M etc.  
Print out every county and the corresponding population. Try this with the enumerate command 
and try it using the range command."""
 
counties = ["Cork", "Dublin", "Kerry", "Waterford"] 
population = [190384, 1228000, 148717, 49213]

#Using range (class)
for i in range(len(counties)):
    print (counties[i], population[i])


#Using the enumerate (class). By putting counties in the bracket 
for index, pop in enumerate(counties):
    print(counties[index], population[index])

