import argparse


def generate_list(wordlist):
    names = []
    with open(wordlist) as f:
        for line in f:
            names.append(line.strip().lower())
    return names


def Namelists(names):
    for line in names:
        firstName = line.split()[0]
        secondName = line.split()[1]
        print(firstName.capitalize())
        print(secondName.capitalize())
        print(firstName.capitalize() + ' ' + secondName.capitalize())
        print(firstName[0].upper() + '.' + secondName.capitalize())
        print(firstName[0].upper() + '_' + secondName.capitalize())
        print(firstName[0].upper() + '-' + secondName.capitalize())
        print(firstName[0].upper() + secondName.capitalize())
        print(firstName.capitalize() + secondName.capitalize())
        print(secondName.capitalize() + firstName.capitalize())
        print(firstName.upper())
        print(secondName.upper())
        print (firstName.upper() + secondName.upper())
        print(line.split()[0])
        print(line.split()[1])
        print(line.split()[0] + ' ' + line.split()[1])
        print(line[0] + '.' + line.split()[1])
        print(line[0] + '-' + line.split()[1])
        print(line[0] + '_' + line.split()[1])
        print(line[0] + '+' + line.split()[1])
        print(line[0] + line.split()[1])
        print(line.split()[0]+line.split()[1])
        print(line.split()[1]+line.split()[0])
        print(line.split()[0] + '.' + line.split()[1])
        print(line.split()[1] + '.' + line.split()[0])




parser = argparse.ArgumentParser(description='Generating User list from wordlist')
parser.add_argument('-w', '--wordlist', type=str, metavar='wordlist', required=True, help="Specify path to the wordlist")

args = parser.parse_args()

names = generate_list(args.wordlist)
Namelists(names)

