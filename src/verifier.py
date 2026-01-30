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