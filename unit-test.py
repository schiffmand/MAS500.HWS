# Perform unit testing on functions in Election Results
# One unit test example

from electiondata import ElectionResults


def testStateCount(self):
	self.results.load()
	state_count = self.results.state_count()
	assert state_count == 2
	