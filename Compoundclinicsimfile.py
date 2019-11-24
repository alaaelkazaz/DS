class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


import random
randage=random.randrange(20, 61)
class Doctor :
    def __init__(self): #doctor class constructor
        self.D_rate = randage/5
        self.currentpatient = None
        self.timeRemaining = 0

    def tick(self) :  # a method to calculate the time remaining for the patient at the doctor's
        if self.currentpatient !=None:
            self.timeRemaining = self.timeRemaining -1
            if self.timeRemaining == 0:
                self.currentpatient=None

    def busy(self):  #a method to check if the doctor is free  or not
        if self.currentpatient !=None:
            return True
        else:
            return False

    def Nextp(self,newp): # method to let the  next patient be the current patient and calculates the time he would take at the doctor's
        self.currentpatient = newp
        self.timeRemaining = newp.getages()/self.D_rate

class Patient :
    def __init__ (self, arrival):  #patient constructor with arrival time argument
        self.times= arrival
        self.ages= randage

    def getarrival (self):
        return  self.times

    def getages (self):
        return self.ages

    def  waittime(self,currenttime):
        return currenttime - self.times

def ClinicSim(w):  # simulation for doctor clinic
    Doctor0 =Doctor ()
    patientQ= Queue() # creating The queue
    TimeWaiting=[]      # create  the waiting times alist
    for currentsec in range(w):  # w is the time we enter ( 4 hours = 4*60*60 second)
        if random.randrange(1,7)== 6 :                  #checks the probability of arrival of a patient at any given second
            patient=Patient(currentsec)                     #creating a file for the patient
            patientQ.enqueue(patient)                       # adding the patient to the queue

        if not Doctor0.busy() and not patientQ.isEmpty() :  # check if the doctor is not busy and if there is a patient
            nextp=patientQ.dequeue()                        # delete patient from queue
            TimeWaiting.append(nextp.waittime(currentsec))  #calculate the waiting time then add it to the list of waiting times
            Doctor0.Nextp(nextp)                             #let the patient  enter to the doctor

        Doctor0.tick()                                      #checks for patients still at the doctor
    averagewait=sum(TimeWaiting)/len(TimeWaiting)       # calculate the average wait
    print ("Average Wait " , averagewait ," Min" , patientQ.size() , " tasks remaining.")

#the simulation (Error generated)
for i in range (40):
    ClinicSim(240)



