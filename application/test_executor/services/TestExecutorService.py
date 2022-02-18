import pandas
from concurrent.futures import ThreadPoolExecutor

class TestExecutorService:
    @staticmethod
    def executeTest(test):
        testCasesFileUri = test['test_cases_file']
        script = test['script']
        data = pandas.read_csv(testCasesFileUri)

        with ThreadPoolExecutor(max_workers=test['threads']) as executor :
            futures = {executor.submit(executeCase, script, row): row for row in data.iterrows()}
        
        return True


def printMethod(name: str, lastName: str):
    print("hola " + name + " " + lastName + ", desde el metodo printMethod()")

def executeCase(script: str, data):
        print(script)
        (l, caseData) = data
        print(caseData)
        print(type(caseData))
        exec(script)

        return True
