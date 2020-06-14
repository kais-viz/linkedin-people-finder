# Helper functions to declutter jupyter notebook
import re

# Extracts digits from string and return the first set found                
def get_id_from_str(exp):
    return re.findall(r'\d+', exp.get("geoUrn"))[0] if exp.get("geoUrn", None) else None
    
# Main filtering function, prints/extracts matches:
# Returns last experience in the profile, set verbose to True to print output
def chk_match(experiences, verbose=False, MAX_COMPANY_SIZE =  450):
    # see regexr.com/4khjo
    # check the job title containing any of (machine learn, data sci or data anal) AND (intern, junior, train)
    regex = r"(?=.*(ml|machine learn|data sci|data anal))(?=.*\b(intern|junior|train)).*"
    
    for exp in experiences:
        matches = re.search(regex, exp["title"], re.IGNORECASE)
        
        companySize = (
            int(exp['company']['employeeCountRange']['start'])
            if ("company" in exp and "employeeCountRange" in exp["company"])
            else 0
        )
        
        if matches and companySize <= MAX_COMPANY_SIZE:            
            companyName = exp.get("companyName", "unknown")            
            industries = (
                ", ".join(exp["company"]["industries"]) 
                if "company" in exp and "industries" in exp['company'] 
                else "?"
            )
            locationName = exp.get("locationName", "unknown")
            companyId = exp.get('companyUrn', None)
            startDate = (
                exp["timePeriod"].get("startDate", "?")
                if "timePeriod" in exp
                else "unknown"
            )
            endDate = (
                exp["timePeriod"].get("endDate", "?")
                if "timePeriod" in exp
                else "unknown"
            )
            
            if verbose:
                print(
                    "\n---\n{} @ {} ({})\n{}, size {}\nfrom {} to {}\nid: {}".format(
                        exp["title"],
                        companyName,
                        companyId,
                        industries,
                        locationName,
                        companySize,
                        startDate,
                        endDate
                    )
                )
                
                if "description" in exp:
                    print(f"\nDescription: {exp['description']}")
                print("---\n")

            return exp
        
    return None
