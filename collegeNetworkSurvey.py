def get_data():
    
    # read file
    input_f = open("partial_data.csv", "rt")
    st = input_f.read()
    input_f.close()

    # initializes the beginning of the dot files
    output_f = open("bowdoinTemp.dot", "wt")
    output_str = "digraph bowdoin_network {\n"

    big_list = st.split("\r")

    # gets each row of the csv
    for row_index in range(2,len(big_list)):
        row = big_list[row_index]
        row_list = row.split(",") #one row of data: list elements are separated by commas
        row_len = len(row_list) #number of elements in the list

        name = row_list[0]
        friends = row_list[2:row_len-34] #list of friends
        rest = row_list[row_len-34:]
        
        #get this for the attribute (in the process)
        dorm = row_list[row_len-34]
        
        friends[0] = friends[0][1:] #Delete start quotation
        friends[-1] = friends[-1][:-1] #Delete end quotation
        for friend_index in range(1, len(friends)):
            friends[friend_index] = friends[friend_index][1:]
    
        #add attribute of dorm
        if dorm != "":
            output_str += '\"' + name + '\"' + " [Hall=" + dorm + "];\n"
        
        for friend in friends:
            if friend != "":
                output_str += '\"' + name + '\"' + " -> " + '\"' + friend + '\"' + ";\n" 
        
        #print name, "-->", friends
        #print rest

    output_str += "}"
    output_f.write(output_str)
    output_f.close()



get_data()


# assignment: look into modifying dot file to account to attributes of the node
