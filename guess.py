#!/usr/bin/env python
from string import digits
from random import randint, choice
class GuessNumber(object) :
    def __init__(self) :
        self.count = 0     
        self.usrNums = []
        self.sysNum = '' 
        self.results = []
        self.isWinner = False
    def printRules(self) :
        print "guess"
    def randNumGen(self) :
        numStr = '0123456789'
        randNum = ''
        for i in range(4) :
            n = choice(numStr)
            randNum += n
            numStr = numStr.replace(n, '')
        self.sysNum = randNum
    def numInput(self) :
        self.count += 1
        while True:
            num = raw_input('input number')
            print 'Debug >> num::',num
            if len(num) < 4 :
                print 'error: number < 4'
                continue
            elif len(num) > 4:
                print 'error: number >4'
                continue
            if not self.isAllNumber(num) :
                print 'error: please input number'
                continue
            elif self.hasSameDigit(num) :
                print 'error: duplicate number'
                continue
            else :
                self.usrNums.append(num)
                return num
    def isAllNumber(self, num) :
        for ch in num :
            if ch not in digits :
                return False
        return True
        
    def hasSameDigit(self, num) :
        for i in range(len(num)) :
            pos = num[i + 1 :].find(num[i])
            if pos >= 0 :
                return True
        return False
    def numJudge(self, sysNum, usrNum) :
        countA = 0
        countB = 0
        for i in range(4) :
            if usrNum[i] in sysNum :
                if i == sysNum.find(usrNum[i]) :
                    countA += 1
                else :
                    countB += 1
        result = '%dA%dB' % (countA, countB)
        self.results.append(result)
        if countA == 4 :
            self.isWinner = True
    def showResults(self, usrNums, results) :
        print '-' * 20
        for i in range(self.count) :
            print '(%d)/t%s/t%s' % (i + 1, usrNums[i], results[i])
        print '-' * 20
        if self.isWinner :
            print 'Total: %d times' % self.count
            print 'Congratulations! winner'
    def run(self) :
        self.printRules()
        self.randNumGen()
        while not self.isWinner:
            num = self.numInput()
            self.numJudge(self.sysNum, num)
            self.showResults(self.usrNums, self.results)
def main() :
    guessNumber = GuessNumber()
    guessNumber.run()
if __name__ == '__main__' :
    main()
