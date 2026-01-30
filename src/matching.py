from collections import deque
'''
Task A: Matching Engine: Implement the hospital-proposing deferred acceptance algorithm

Initially, all hospitals are unmatched and have not proposed to anyone.
While there exists an unmatched hospital that still has students left to propose to:
The hospital proposes to the next student on its preference list that it has not yet proposed to.
The student tentatively accepts the best hospital (according to the student's preferences) among its current tentative match (if any) and the new proposer, rejecting the other.
Your program must output the final matching and (optionally) the number of proposals made.  See the pseudocode given in class for specific detail.

Input/Output Specification
    Input Format: The input describes preferences for a one-to-one market with complete strict rankings.

    First line: integer n.
    Next n lines: hospital preference lists.
    Next n lines: student preference lists.
    Hence, each preference line contains n integers, a permutation of 1..n.

Pseudocode:

Initialize each person and hospital to be free.
while (some hospital is free and hasn't been matched/assigned to every applicant):
    choose such a hospital H
    a = 1st applicant on h's list to whom H has not been matched

    if (a is free):
        (H, a) become matched
    else if (a prefers H to its current match H'):
        (H, a) become matched
        H' becomes free
    else:
        (H, a) remain unmatched

'''


# takes the input and makes it into two lists w
def parse_input(input_string):
    if not input_string:
        return None
    
    hospital_prefs, student_prefs = [], []
    split_by_lines = input_string.strip().split('\n') #.strip bc we wanna remove the trailing and starting whatevers
    n = int(split_by_lines[0])
    for i in range(1, n + 1):
        students = split_by_lines[i].split()
        hospital_prefs.append([int(num) for num in students])

    for i in range(n + 1, len(split_by_lines)):
        hospitals = split_by_lines[i].split()
        student_prefs.append([int(num) for num in hospitals])
    
    return (hospital_prefs, student_prefs)
    
                

#print(parse_input(input_string1))

def matching(raw_input):

    def isBetter(appPref, currMatch, possibleNew):
        for hosp in appPref:
            if hosp == currMatch:
                return False
            if hosp == possibleNew:
                return True
    #print(raw_input)
    
    parsed_input_tup = parse_input(raw_input)

    debug_mode = False

    hospital_prefs, student_prefs = parsed_input_tup
    n = len(hospital_prefs)
    matchedApplicants = {} # applicant -> hospital
    hospital_match = [[None] for __ in range(n)]
    q = deque([(i + 1) for i in range(n)])
    
    while q:
        curr_hospital = q.popleft()
        curr_prefs = hospital_prefs[curr_hospital - 1]

        if debug_mode: print("\nLooking at hospital: ", curr_hospital)

        for applicant in curr_prefs:
            if debug_mode: print("\tLooking at applicant: ", applicant)
            if (applicant not in matchedApplicants):
                if debug_mode: print("\t\tWasn't matched...so we added")
                hospital_match[curr_hospital - 1] = applicant
                matchedApplicants[applicant] = curr_hospital
                break
            elif (isBetter(student_prefs[applicant - 1], matchedApplicants[applicant], curr_hospital)):
                if debug_mode: print("\t\tFound a better match..so we added")
                hospital_match[curr_hospital - 1] = applicant
                q.append(matchedApplicants[applicant]) #add old hospital to the queue
                matchedApplicants[applicant] = curr_hospital
                break
            else:
                if debug_mode: print("\t\tApplicant rejects hospital")
                None #for now
                
    if debug_mode: print("This is the hospital match: ")
    if debug_mode: print(hospital_match)

    output = ""
    for i in range(n):
        hospital = str(i + 1)
        applicant = str(hospital_match[i])
        output += hospital + " " + applicant + "\n"

    return output

if __name__ == '__main__':
    input_string1 = "3\n1 2 3\n1 2 3\n2 3 1\n2 1 3\n3 2 1\n1 2 3"
    output_string1 = "1 3\n2 1\n3 2"
    
    print(matching((input_string1)))





