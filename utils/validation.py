import re

def validate_and_clean_entities(parsed_data: dict) -> dict:
    """Validate and clean extracted entities"""
    
    # Email validation
    if parsed_data.get('email'):
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, parsed_data['email']):
            parsed_data['email'] = ''
    
    # Phone validation
    if parsed_data.get('phone'):
        phone_pattern = r'^[\+]?[1-9][\d]{0,15}$'
        cleaned_phone = re.sub(r'[^\d+]', '', parsed_data['phone'])
        if not re.match(phone_pattern, cleaned_phone):
            parsed_data['phone'] = ''
        else:
            parsed_data['phone'] = cleaned_phone
    
    # Name validation (should not contain skills, companies, etc.)
    if parsed_data.get('name'):
        invalid_terms = ['resume', 'cv', 'linkedin', 'github', 'http']
        name_lower = parsed_data['name'].lower()
        if any(term in name_lower for term in invalid_terms) or len(parsed_data['name'].split()) > 4:
            parsed_data['name'] = ''
    
    return parsed_data