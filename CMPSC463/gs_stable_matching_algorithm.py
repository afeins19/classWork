"""This program will implement the GS Stable Matching Algorithm

Data Structures:
  each proposer will be held in a dictionary as a key with
  the value being a list of proposed matches in the order
  of preference

  companies = {company1 : [candidate1, candidate2,     candidate3],...], company2: ...}

employees = {employee1 : [company1, company2, company3],...}, employee2: ...]}


---------------------------------------- ~~~ LAB QUESTION ~~~ ----------------------------------------
In the first run, set the companies as the “proposer” (one of the reasons why companies use headhunt
firms)
In the second run, set the job seeker as the “proposer” (the reason why you should apply for jobs)
Compare the two results, do you see any difference?

    This setup of the problem game some contradictory results since the algorithm returned a
    stable matching that favored the employees when the companies were the ones making propositions.
    This contradicts the idea that the Gale-Shapley Algorithm would give a higher overall score to
    those making propositions.

    The second run, where job-seekers made propositions resulted in a draw of 0-0.
"""
import copy

def gs_stable_matching(proposers, candidates):

  matches = {}  # will contain matched pairs (ADD PAIRS in ORDER {CANDIDATE : PROPOSER}
  unmatched_proposers = list(proposers.keys())  # holds unmatched proposers

  # copying arguments and operating on those internally so it doesnt affect the actual data being passed
  proposers = copy.deepcopy(proposers)
  candidates = copy.deepcopy(candidates)

  # while some proposer is unmatched...
  while unmatched_proposers:
    cur_proposer = unmatched_proposers[0]  # select a proposer
    cur_proposer_preferences = proposers[
        cur_proposer]  # get the list of proposers preferences

    # iterate over each potential candidate in the current proposers preferences...
    for candidate in cur_proposer_preferences:
      if candidate not in matches.keys():  # candidate has not yet been proposed to
        unmatched_proposers.remove(
            cur_proposer)  # drop current proposer from unmatched dict
        matches[
            candidate] = cur_proposer  # update current proposers match status

        print(f"{ cur_proposer } -> { candidate } | match")
        break

      elif candidate in matches.keys():  # the candidate already has a match
        # compare rank of current and previous proposer (from candidates perspective)
        cur_proposer_rank = candidates[candidate].index(
            cur_proposer)  # preference of current proposer
        prev_proposer_rank = candidates[candidate].index(
            matches[candidate])  # preference of current match
        prev_proposer = candidates[candidate][
            prev_proposer_rank]  # getting the name of the previous proposer

        if cur_proposer_rank < prev_proposer_rank:  # current proposer is more desirable
          unmatched_proposers.remove(
              cur_proposer)  # add prev_proposer back to unmatched dict
          unmatched_proposers.append(
              prev_proposer)  # put last proposer back in to unmatched dict
          matches[
              candidate] = cur_proposer  # append current candidate to matched dict
          print(
              f"{ cur_proposer } -> { candidate } | match | Dropped: { prev_proposer }"
          )
          break

        else:  # rejection :(
          proposers[cur_proposer].remove(candidate) # if a proposer is rejected, we wont have him try this candidate again
          print(f"{cur_proposer} -> {candidate} | rejected")

  print("\n")  # separate multiple runs
  return matches  # were done


# finds total scores for each run for the group of proposers
def calculate_proposer_score(proposers, candidates, matches):
  proposer_score = sum([proposers[p].index(c) for c, p in matches.items()])
  return proposer_score


# finds total scores for each run for the group of candidates
def calculate_candidate_score(proposers, candidates, matches):
  candidate_score = sum([candidates[c].index(p) for c, p in matches.items()])
  return candidate_score


companies = {
    'Google': ['Lisa', 'Tom', 'Sarah', 'Bob', 'Jane'],
    'Amazon': ['Sarah', 'Tom', 'Jane', 'Lisa', 'Bob'],
    'Meta': ['Jane', 'Lisa', 'Bob', 'Tom', 'Sarah'],
    'Apple': ['Jane', 'Bob', 'Tom', 'Sarah', 'Lisa'],
    'Microsoft': ['Bob', 'Tom', 'Sarah', 'Lisa', 'Jane']
}

candidates = {
    'Lisa': ['Google', 'Amazon', 'Apple', 'Meta', 'Microsoft'],
    'Sarah': ['Amazon', 'Apple', 'Meta', 'Google', 'Microsoft'],
    'Bob': ['Microsoft', 'Meta', 'Google', 'Apple', 'Amazon'],
    'Tom': ['Meta', 'Google', 'Apple', 'Amazon', 'Microsoft'],
    'Jane': ['Apple', 'Google', 'Amazon', 'Microsoft', 'Meta']
}

companies_propose = gs_stable_matching(proposers=companies,
                                       candidates=candidates)
candidates_propose = gs_stable_matching(proposers=candidates,
                                        candidates=companies)

# companies are the proposer
print("\nProposer = Companies")
print(companies_propose)
print(
    f"Proposer Score: { calculate_proposer_score(companies, candidates, companies_propose) }"
)
print(
    f"Candidate Score: { calculate_candidate_score(companies, candidates, companies_propose) }"
)

# employees are proposer
print("\nProposer = Employees")
print(candidates_propose)
print(
    f"Proposer Score: { calculate_proposer_score(candidates, companies, candidates_propose) }"
)
print(
    f"Candidate Score: { calculate_candidate_score(candidates, companies, candidates_propose) }"
)
