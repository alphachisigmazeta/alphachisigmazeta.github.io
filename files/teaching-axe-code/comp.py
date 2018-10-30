import csv
import random
import algorithm
from time import sleep

def getPrices(ticker):
    closeIdx = 0
    firstRow = True
    firstDate = True
    prices = []
    dates = []
    
    with open('individual_stocks_5yr/' + ticker + '_data.csv', newline='\n') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for row in spamreader:
            if(firstRow):
                for i, col in enumerate(row):
                    if(col == 'close'):
                        closeIdx = i
                        firstRow = False
                        continue;
            else:
                dates.append(row[0])
                prices.append(float(row[closeIdx]))
    return dates, prices

def runCompetition(stockName):
    printStart(stockName)
    
    dates, amgnPrices = getPrices(stockName)
    
    stocks = 0
    money = 0
    endDate = -random.randint(5,250)
    continuousErrorCt = 0
    maxErrorCt = 3
    currYear = getYear(dates[0])
    
    for i, price in enumerate(amgnPrices[:endDate]):
        
        decision = algorithm.decideToBuyOrSell(price)
        
        if(decision.lower() == 'buy'):
            if(stocks == 1):
                if(continuousErrorCt < maxErrorCt):
                    print("You can't buy, you are already holding")
                elif (continuousErrorCt == maxErrorCt):
                    print("You have continued to make invalid purchases, muted until valid transcation made")
                continuousErrorCt += 1
            else:
                print("You bought " + stockName + " stock priced at " + str(price) + " on " + dates[i] + ".")
                stocks += 1
                money -= price
                continuousErrorCt = 0
                sleep(0.1)
            
        elif(decision.lower() == 'sell'):
            if(stocks == -1):
                if(continuousErrorCt < maxErrorCt):
                    print("You can't sell, you are already shorting")
                elif (continuousErrorCt == maxErrorCt):
                    print("You have continued to make invalid purchases, muted until valid transcation made")
                continuousErrorCt += 1
            else:
                print("You sold " + stockName + " stock priced at " + str(price) + " on " + dates[i] + ".")
                stocks -= 1
                money += price
                continuousErrorCt = 0
                sleep(0.01)
        else:
            # print("Nothing done")
            pass
        
        '''
        nextYear = getYear(dates[i+1])
        if(currYear != nextYear):
            for i in range(5):
                print('.', end ='', flush=True)
                sleep(0.5)
            print("... It is now the year " + nextYear)
            currYear = nextYear
        '''
    
    return money + (stocks * amgnPrices[endDate])

def printStart(stockName):
    print("================================================================================")
    print("================================================================================")
    print("=======                                                                 ========")
    print("===== Welcoming to the Coding Competition. Your trading will commence now! =====")
    print("===== Good luck!! You will start with $0 and 0 stocks of " + stockName + ". Make money! =====", end='')
    if(len(stockName) == 3):
        print("=")
    else: print("")
    print("=======                                                                 ========")
    print("================================================================================")
    print("================================================================================")
    print()
    sleep(5)

def printResult(gains):
    print("You ended with $" + str(round(gains * 100) / 100.0))
    
def getYear(date):
    return date[:4]
    
def main():
    totalGains = runCompetition("AMGN")
    printResult(totalGains)

if __name__ == '__main__':
    main()
