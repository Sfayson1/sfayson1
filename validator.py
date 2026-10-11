import json

required_fields = [
    "headline",
    "summary",
    "links",
    "featured_projects",
    "education",
    "currently_learning",
    "skills",
]

expected_types = {
    "headline": str,
    "summary": str,
    "links": dict,
    "featured_projects": list,
    "education": list,
    "currently_learning": list,
    "skills": dict,
    "profile_section": dict,
}




def validate_profile(profile):
    is_valid = True

    for field in required_fields:
        if field not in profile:
            print(f"Missing required field: {field}")
            is_valid = False

        elif not profile[field]:
            print(f"Required field is empty: {field}")
            is_valid = False

        elif not isinstance(profile[field], expected_types[field]):
            print(f"Invalid type for field: {field}")
            is_valid = False


    profile_required_fields = [
    "title",
    "role",
    "focus",
    "location",
    "status"
]

    for field in profile_required_fields:
        if field not in profile["profile_section"]:
            print(f"Missing profile section field: {field}")
            is_valid = False

        elif not profile['profile_section'][field]:
            print(f"Profile section field is empty: {field}")
            is_valid = False

    return is_valid



with open("profile_data.json", "r") as file:
    test_profile = json.load(file)


result = validate_profile(test_profile)
print(result)
