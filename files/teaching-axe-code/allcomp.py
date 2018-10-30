import comp
import checkcheaters

companies = ["AMGN", "ABT", "ABBV"]
totalGains = 0

checkcheaters.check()

for company in companies:
    totalGains += comp.runCompetition(company)
    print("")
    print("")
    print("")

comp.printResult(totalGains)
