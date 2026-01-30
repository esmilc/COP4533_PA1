from matching import parse_input as parse_preferences

def parse_result_string(input_str):
    input_str_lines = input_str.strip().split('\n')
    
    sep_input_str = []
    for pair in input_str_lines:
        hosp, app = pair.split()
        sep_input_str.append((int(hosp), int(app)))
    return sep_input_str


    

def verifier(raw_input_pref, raw_input_toVerify):
    result_list = parse_result_string(raw_input_toVerify)
    hospitals = set()
    students = set()
    invalid = False
    blocking = False
    output = "VALID STABLE"
    for hospital, student in result_list:
        if hospital in hospitals:
            output = f"INVALID: Hospital {hospital} repeated"
            invalid = True
            break
        hospitals.add(hospital)
        if student in students:
            output = f"INVALID: Student {student} repeated"
            invalid = True
            break
        students.add(student)

    if invalid:
        return output
    
    
    hospital_prefs, student_prefs = parse_preferences(raw_input_pref)
    n = len(hospital_prefs)

    if len(result_list) != n:
        return f"INVALID: Expected numbers don't match."

    correct = set()
    for i in range(1, n+1):
        correct.add(i)
    
    if hospitals != correct:
        return "INVALID: Hospitals not from range 1..n+1"
    if students != correct:
        return "INVALID: Applicants not from range 1..n+1"
    

    def buildPrefMap(tups):
        hospToStudent, studentToHosp = {}, {}
        for hosp, student in tups:
            hospToStudent[hosp] = student
            studentToHosp[student] = hosp
        return [hospToStudent, studentToHosp]

    
    def isBetterForStudent(appPref, currMatch, possibleNew):
        for hosp in appPref:
            if hosp == currMatch:
                return False
            if hosp == possibleNew:
                return True
        return False
    
    def isBetterForHospital(hospPref, currMatch, possibleNew):
        for student in hospPref:
            if student == currMatch:
                return False
            if student == possibleNew:
                return True
        return False
    
    def preferEachOtherOverCurrAssign(currHosp, currStud, newStud, newHosp,  hospPrefs, studentPrefs):
        if currStud == newStud or currHosp == newHosp:
            return False
        if isBetterForHospital(hospPrefs, currStud, newStud) and isBetterForStudent(studentPrefs, currHosp, newHosp):
            return True
        return False
    
    #print(hospital_prefs)
    #print(student_prefs)

    hospToStudent, studentToHosp = buildPrefMap(result_list)
    for h in range(len(hospital_prefs)):
        hospital = h + 1
        for student in hospital_prefs[h]:
            if preferEachOtherOverCurrAssign(studentToHosp[student], hospToStudent[hospital], student, hospital, hospital_prefs[h], student_prefs[student-1]):
                output = f"BLOCKING PAIR: Hospital {studentToHosp[student]}, Student {hospToStudent[hospital]}"
                return output
            
    
        
    return output

if __name__ == "__main__":
    invalid_str1 = "1 2\n1 3"
    invalid_str2 = "1 3\n2 3"

    input_string1 = "3\n1 2 3\n1 2 3\n2 3 1\n2 1 3\n3 2 1\n1 2 3"
    output_string1 = "1 3\n2 1\n3 2"


    print(verifier(input_string1, invalid_str1))
    print(verifier(input_string1, invalid_str2))