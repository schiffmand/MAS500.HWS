# Election Results module
# Coded in the "object-oriented" style
from electiondata import ElectionResults
state_arr[], obama_tot=0, romney_tot=0, 
filename = '2012_US_election_state.csv'
results = ElectionResults(filename)
results.load()

function state_names() {
	state_arr[]=results.states()
	return state_arr
}
print "done ("+str(results.state_count())+" lines)"

# print total votes per candidate
