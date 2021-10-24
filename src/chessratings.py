def fide_expected_score(elo_A, elo_B):
	'''
	Args:

		elo_A (float): Elo Rating for player A.
		elo_B (float): Elo Rating for player B.

	Return:

		expected_score_A (float): Expected score of player A out of 1.0

	'''

	expected_score_A = 1/(1+pow(10,((elo_B-elo_A)/400)))
	return expected_score_A 



