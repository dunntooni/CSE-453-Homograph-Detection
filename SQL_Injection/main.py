def genQuery(username, password):
    sql = f"SELECT * FROM table WHERE 'user = {username}' AND 'userPassword = {password}'"
    return sql

def genQueryWeak(username, password):
    sql = ""
    return sql

def genQueryStrong(username, password):
    sql = ""
    return sql

def testValid(queryGenerator):
    print("TESTING VALID INPUTS")
    print("********************")

    test_cases = [("ValidUsername", "Valid_Password")]
    for test in test_cases:
        print(f"Username: {test[0]}  Password: {test[1]}")
        sql = queryGenerator(test[0], test[1])
        print(f"SQL statement is:    {sql}")

def testTautology():
    pass

def testUnion():
    pass

def testAddState():
    pass

def testComment():
    pass

if __name__ == '__main__':
    testValid(genQuery)