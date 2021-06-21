#Create a function that counts each base 
# in DNA Molecule, denotes as string,
#For example 'ATGACGTGGA'
#Contoh:
#A = 3
#T = 2
#G = 4
#C = 1

# a = 'ATGACGTGGA'

#def hitungDNA(DNA):
    # A = DNA.count('A')
    # T = DNA.count('T')
    # G = DNA.count('G')
    # C = DNA.count('C')
    # U = DNA.count('U')

#   print ('A = {}'.format(A))
#   print ('T = {}'.format(T))
#   print ('G = {}'.format(G)) 
#   print ('C = {}'.format(C))
#   print ('U = {}'.format(U))

#hitungDNA(a)


#Create a Lift, that is able to:
#- Move up (to the specific floor)
#- Move down (to the specific floor)
#- Has capacity (maximum number of people)
#- Open the lift door
#- Close the lift door


class Lift:
    def __init__(self, maxfloor= 10, maxperson= 8):
        self.maxfloor = maxfloor
        self.maxperson = maxperson
        self.currentfloor = 1


#to move up/down, must state current floor, 
#if entered floor > current floor = move up, else = move down
# 
    
    def move_updown(self, angka: int, person):
        if  not self.person_inthelift(person):
            return
        
        if (angka>=1 and angka<=self.maxfloor):
            print("Going from {} floor to {}".format(self.currentfloor, angka))
            self.currentfloor=angka
        else:
            print("Floor doesn't exist")

    def person_inthelift(self, person:int):
        if (person<self.maxperson):
            print ("Door is closing!")
            return True
        else: 
            print ("Lift has reached max capacity. Door is still open!")
            return False
    
LiftEmmerich= Lift()
angka = int(input("Input destination floor: "))
person = int(input("How many person: "))
LiftEmmerich.move_updown(angka,person)







