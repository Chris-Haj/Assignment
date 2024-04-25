""""""
import copy

"""

TotalVotesForParty = {}
    for party in party_dict:
        TotalVotesForParty[party] = sum(party_dict[party].values())
        
        
Data structure dictionary
where key is the election year

kretser : districts
partier : political parties
Stemmer: elections of different years

5
11
12 
13 
"""

districtPath = 'Files/kretser.txt'
partiesPath = 'Files/partier.txt'
electionsPath = 'Files/stemmer'

valg = {}

districts = {}
with open(districtPath, 'r') as file:
    for line in file:
        if line[-1] == '\n':
            line = line[:-1]
        number, district = line.split(' ', 1)
        number = int(number)
        districts[district] = number

parties = {}
with open(partiesPath, 'r') as file:
    for line in file:
        if line[-1] == '\n':
            line = line[:-1]
        short, party = line.split(',')
        parties[party] = short


def lesValg(year, file, ledger=None):
    if year in valg and ledger is None:
        return valg[year]
    if ledger is None:
        ledger = {}
        with open(file, 'r') as file:
            file.readline()
            for line in file:
                if line[-1] == '\n':
                    line = line[:-1]
                district, party, votesAmount = line.split(',')
                district = int(district)
                if party not in ledger:
                    ledger[party] = {}
                ledger[party][district] = int(votesAmount)
            valg[year] = ledger
            return ledger
    else:
        with open(file, 'r') as file:
            newLedger = {}
            secondLedger = copy.deepcopy(ledger)
            file.readline()
            for line in file:
                if line[-1] == '\n':
                    line = line[:-1]
                district, party, votesAmount = line.split(',')
                district = int(district)
                if party not in newLedger:
                    newLedger[party] = {}
                newLedger[party][district] = int(votesAmount)

                if party not in secondLedger:
                    secondLedger[party] = {}
                if district not in secondLedger[party]:
                    secondLedger[party][district] = int(votesAmount)
                else:
                    secondLedger[party][district] += int(votesAmount)
        valg[year] = newLedger
        return secondLedger


v13 = lesValg(2013, 'Files/stemmer2013.txt')
v13og17 = lesValg(2017, 'Files/stemmer2017.txt', v13)
v21 = lesValg(2021, 'Files/stemmer2021.txt')


def stemmerTotalt(ledger):
    totalParty = {}
    for party in ledger:
        totalParty[party] = sum(ledger[party].values())
    totalVotes = 0
    for votes in totalParty.values():
        totalVotes += votes
    print(totalVotes)
    return totalVotes


def valgresultat(year, district, party):
    if year in valg:
        ledger = valg[year]
    else:
        ledger = lesValg(year, 'Files/stemmer' + str(year) + '.txt')

    if party in parties:
        party = parties[party]
    if district in districts:
        district = districts[district]

    if party not in ledger:
        return 'ukjent parti'
    else:
        curParty = ledger[party]
        if district in curParty:
            return curParty[district]
        else:
            return 'ukjent krets'


def kretsÅr(district, year):
    if year in valg:
        ledger = valg[year]
    else:
        return 'ukjent ar'
    if district in districts:
        district = districts[district]
    else:
        return 'ukjent krets'

    partyVotes = {}
    for party, districtVotes in ledger.items():
        if district in districtVotes:
            partyVotes[party] = districtVotes[district]

    return partyVotes

x = kretsÅr('Nordnes',2017)

def samlet(year):
    if year in valg:
        ledger = valg[year]
    else:
        return 'ukjent ar'
    partyVotes= {}
    for party, districtVotes in ledger.items():
        totalVotes = 0
        for votes in districtVotes.values():
            totalVotes+= votes
        partyVotes[party] = totalVotes
    return partyVotes



def prosentfordeling(year):
    if year in valg:
        ledger = valg[year]
    else:
        return 'ukjent ar'
    percentageDistribution = {}
    totalVotes = stemmerTotalt(ledger)
    partyVotes = samlet(year)
    for party, districtVotes in ledger.items():
        percentageDistribution[party] = partyVotes[party]/totalVotes
    return percentageDistribution

x = prosentfordeling(2021)
print(x)

def endring(start, end):
    if start not in valg or end not in valg:
        return 'ukjent ar'
    startLedgerPerc = prosentfordeling(start)
    endLedgerPerc = prosentfordeling(end)




def kretsOversikt():
    year, district = input('Please input a year and a district')

def partiOversikt():
    year, party = input('Please input a year and a district')
