import operator
class Election(object):
    """Election of Borda votes"""
    def __init__(self, candidates=[]):
    	self.candidates = candidates


    def set_candidates(self, candidates):
        self.candidates = candidates
        self.votes = {}

    def add_candidate(self, candidate):
        self.candidates.append(candidate)

    def get_winner(self):
        sorted_votes = sorted(self.votes.iteritems(),
                              key=operator.itemgetter(1),
                              reverse=True)
        return sorted_votes
    def give_points(self, chosen, points):
        for candidate in self.candidates:
            if candidate == chosen:
                self.votes.setdefault(chosen, 0)
                self.votes[chosen] += points
                
    def get_candidates(self):
    	return self.candidates



class Voter(object):
    """Voter is a participant in a Borda voting"""

    def __init__(self, election, name):
        self.election = election
        self.name = name

    def votes(self, candidates):
        total = len(candidates)
        for pos, candidate in enumerate(candidates):
            points = total - pos
            print candidate, points
            self.election.give_points(candidate, points)
        print "========"
        



class Candidate(object):
    """Candidate is a candidate to be a winner in a Borda voting"""
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
    	return self.name

if __name__ == "__main__":
	gene_rank = Election()
	gene1 = Candidate('gene1')
	gene2 = Candidate('gene2')
	gene3 = Candidate('gene3')
	geney = Candidate('geney')

	

	gene_rank.set_candidates([gene1, gene2, gene3])
	gene_rank.add_candidate(geney)

	tool1 = Voter(gene_rank, 'tool1')
	tool2 = Voter(gene_rank, 'tool2')
	tool3 = Voter(gene_rank, 'tool3')


	tool1.votes([gene3, gene2, gene1, geney])
	tool2.votes([gene2, gene3, gene1, geney])
	tool3.votes([gene1, geney, gene2, gene3])


	print gene_rank.get_candidates()

	print gene_rank.get_winner()
