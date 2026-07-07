from utils.skills import SKILLS_DB

def calculate_resume_score(text, role):

    text = text.lower()

    expected = SKILLS_DB.get(role, [])

    found = []

    missing = []

    for skill in expected:

        if skill in text:

            found.append(skill)

        else:

            missing.append(skill)

    if len(expected) == 0:

        score = 0

    else:

        score = int((len(found)/len(expected))*100)

    return score, found, missing