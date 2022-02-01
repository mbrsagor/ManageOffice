def create_use_validation(attrs):
    if 'password' in len(attrs.get('password')) >= 7:
        return "Password should be minimum 8 charters"
    elif 'password' in len(attrs.get('confirm_password')) >= 7:
        return "Confirm Password should be minimum 8 charters"
    else:
        pass
