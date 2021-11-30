# The data we need to retrieve
# 1 The total number of votes cast
# 2 A complete list of candidates who received votes
# 3 The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote



file_to_load = 'C:/Users/Will/Desktop/Analysis/Election_Results/election_results.csv'

#Open the election results and read the file
with open(file_to_load) as election_data:

    #To do: perform analysis.
    print(election_data)

#close the file.
election_data.close()








