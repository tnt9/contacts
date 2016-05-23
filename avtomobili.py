import random
class Cars:
    def __init__(self, znamka, ime, power):
        self.znamka = znamka
        self.ime = ime
        self.power = power

    def polno_ime(self):
        return self.znamka, self.ime, self.power


cx3 = Cars("mazda", "cx-3", 86)
beattle = Cars("volkswagen","beattle", 78)
panda = Cars("fiat", "panda", 56)
A3 = Cars("audi", "a3", 100)

vsi_avti = [cx3, beattle, panda, A3]

answer = raw_input("Would you to guess a company which makes certain cars?(y/n) ")
if answer.lower() == "y":
    for i in range(0, len(vsi_avti)):
        izbira = vsi_avti[i]
        print "Selected car data: %s, %s kW" % (izbira.ime, izbira.power)
        znamka = raw_input("The production company is:")
        if znamka.lower() == izbira.znamka:
            print "The answer is correct"
        else:
            print "No, this is not the correct answer. It's produced by %s" %izbira.znamka
            print "We were looking for %s %s %s. " %izbira.polno_ime()
if answer.lower() == "n":
     print "Too bad!"

