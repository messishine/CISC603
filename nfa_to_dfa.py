import pandas as pd

nfa = {'A': {'0': ['A', 'B'], '1': ['A']}, 
       'B': {'0': ['C'], '1': ['C']}, 
       'C': {'0': ['D'], '1': ['D']}, 
       'D': {'0': [], '1': []}}

t = 2                                         #number of Transitions

print("\nNFA : \n")
print(nfa)                                    #printing NFA
print("\nPrinting NFA table :- ")
nfa_table = pd.DataFrame(nfa)
print(nfa_table.transpose())

###################################################                 
    
new_states_list = []                          #holds all the new states created in dfa
dfa = {}                                      #dfa dictionary/table or the output structure we needed

keys_list = []
keys_list.append(list(nfa.keys())[0])         #conatins all the states in nfa plus the states created in dfa are also appended further

print("\n", "keys list before")
print(keys_list)

path_list = list(nfa[keys_list[0]].keys())    #list of all the paths eg: [a,b] or [0,1]

print("\n","path list before")
print(path_list)

###################################################

# Computing first row of DFA transition table

dfa[keys_list[0]] = {}                        #creating a nested dictionary in dfa 
for y in range(t):
    var = "".join(nfa[keys_list[0]][path_list[y]])   #creating a single string from all the elements of the list which is a new state
    dfa[keys_list[0]][path_list[y]] = var            #assigning the state in DFA table
    
    # print("\n","check var")
    # print(var)

    if var not in keys_list:                         #if the state is newly created 
        new_states_list.append(var)                  #then append it to the new_states_list
        keys_list.append(var)                        #as well as to the keys_list which contains all the states
        
###################################################
print("\n","key list later")
print(keys_list)

print("\n","path list later")
print(path_list)

print("\n","new states list")
print(new_states_list)

print("\n","new dfa")
print(dfa)

# Computing the other rows of DFA transition table

while len(new_states_list) != 0:                     #consition is true only if the new_states_list is not empty
    dfa[new_states_list[0]] = {}                     #taking the first element of the new_states_list and examining it
    for _ in range(len(new_states_list[0])):
        for i in range(len(path_list)):
            temp = []                                #creating a temporay list
            for j in range(len(new_states_list[0])):
                temp += nfa[new_states_list[0][j]][path_list[i]]  #taking the union of the states
                
                # print("\n", "check temp")
                # print(temp)

            s = ""
            s = s.join(temp)                         #creating a single string(new state) from all the elements of the list
            
            # print("\n", "check s")
            # print(s)
            
            if s not in keys_list:                   #if the state is newly created
                new_states_list.append(s)            #then append it to the new_states_list
                keys_list.append(s)                  #as well as to the keys_list which contains all the states
            dfa[new_states_list[0]][path_list[i]] = s   #assigning the new state in the DFA table
        
    new_states_list.remove(new_states_list[0])       #Removing the first element in the new_states_list

print("\n","key list final")
print(keys_list)

print("\n","path list final")
print(path_list)

print("\n","new states final")
print(new_states_list)


print("\nDFA :- \n")    
print(dfa)                                           #Printing the DFA created
print("\nPrinting DFA table :- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())