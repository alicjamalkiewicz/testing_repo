# Vulnerable method that will trigger code scanning alerts
def get_user_from_db(user_id):
    """
    This method has a SQL injection vulnerability.
    User input is directly concatenated into the SQL query.
    """
    import sqlite3
    
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # VULNERABLE: Direct string concatenation with user input
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    
    result = cursor.fetchone()
    conn.close()
    return result


def execute_command(user_input):
    """
    This method has a code injection vulnerability.
    User input is directly passed to eval() which is dangerous.
    """
    # VULNERABLE: Using eval() with untrusted input
    result = eval(user_input)
    return result


def process_password(password):
    """
    This method has a hardcoded secret vulnerability.
    """
    # VULNERABLE: Hardcoded credentials
    api_key = "sk-1234567890abcdefghijklmnop"
    secret = "mySecretPassword123"
    
    # Use credentials with user input
    return f"Processing with key: {api_key}"

