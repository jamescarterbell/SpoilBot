import random

class rule:

    '''
    def __new__(self, replace, withText):
        self.typeR = replace
        self.replacement = withText
        return self
    '''
    
    def __init__(self, replace, withText):
        self.typeR = replace
        self.replacement = withText
        
    def replace(self):
        return self.replacement[random.randrange(0,len(self.replacement))]

class rulecollection:

    def __init__(self, _rule):
        if isinstance(_rule, rule):
            self.rules = list()
            self.rules.append(_rule)
        else:
            self.rules = _rule

    def addRules(self, _rule):
        if isinstance(_rule, list()):
            for r in _rule:
                self.rules.append(r)
        else:
            self.rules.append(_rule)

    def applyRules(self, string):
        words = string.split(" ")
        if len(words) <= 1:
            return string
        returnText = ""
        for word in words:
            ruleWorked = False
            for r in self.rules:
                if r.typeR in word:
                    newText = str(r.replace())
                    if ".s" in word:
                        newText = newText + "s"
                    if ".cap" in word:
                        newText = newText[0].upper() + newText[1:]
                    if ".as" in word:
                        newText = newText + "'s"
                    newText = self.applyRules(newText)
                    returnText = returnText + newText + " "
                    ruleWorked = True
                    break
            if not ruleWorked:
                returnText = returnText + word + " "
        return returnText

