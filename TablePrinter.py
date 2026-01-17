#Sample Data
tableData = [['apples', 'oranges', 'cherries', 'banana', 'Aldritch'],
             ['Alice', 'Bob', 'Carol', 'David' ,'Solaire'],
             ['dogs', 'cats', 'moose', 'goose', 'Gwynevere']]


#Main function
def printTable(table):


    #Initializing an empty list for the col width of each column
    colWidths = [0] * len(table)

    #Rows
    rows = [''] * len(table[0])


    #Loop to calculate the highest value of characters in a string 
    #Looping through the overall list
    for l in table:
        #Variable holding the value of the longest string
        longestString = 0
        
        #Looping through the inner list
        for i in l:

            #If the length of the current item is longer, update the variable above
            if len(i) > longestString:
                longestString = len(i)
        
        #Add the longest length to the colWidth list
        colWidths[table.index(l)] = longestString

    
    #Organizing the information in rows
    for t in table:
        for i in t:
            rows[t.index(i)] =  rows[t.index(i)] + ' ' + i
    
    for s in rows:
        rows[rows.index(s)] = s.split()


    for r in rows:
        for i in r:
            r[r.index(i)] = i.rjust(colWidths[r.index(i)])
        rows[rows.index(r)] = ' '.join(r)
    
    
    for r in rows:
        print(r)
    
    return

    

#Calling main function
printTable(tableData)