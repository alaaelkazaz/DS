import queue 
import random

class Doctor :
    def init(self,):
        self.D_rate = random.randrange(20,61)//5
        self.currentpatient = None
        self.timeReamain = 0
    def tick(self) :
        if self.currentpatient !=None:
            self.timeRemaing = self.timeRemain -1
            if self.timeRemaining == 0:
                self.currentpatient=None
    def busy(self):
        if self.currentpatient !=None:
            return True
        else:
            return False
    def Nextp(self,newp):
        self.currentpatient = newp
        self.timeRemaining = newp.getpatient()*60/self.Drate

class Patient :
    def patient (self, arrival):
        self.times= arrival
        self.ages= random.randrange(20, 61)

    def getarrival (self):
        return  self.times

    def getages (self):
        return self.ages

    def  waittime(self):
        return currenttime - self.times

def ClinicSim(w,):
    Doctor0 =Doctor ()
    patientQ= Queue()
    TimeWaiting=[]
    for currentsec in range(w):
        if random.randrange(1,361)== 360 :
            patient=Patient(currentsec)
            patientQ.enqueue(patient)

        if not Doctor0.busy() and not patientQ.isEmpty() :
            nextp=patientQ.dequeue()
            TimeWaiting . append (nextp.waittime(currentsec))
            Doctor0.newp(nextp)

        Doctor0.tick()
        averagewait=sum(TimeWaiting)/len(TimeWaiting)
        print ("Average Wait " , averagewait ," secs" , patientQ.size() , " tasks remaining.")


for i in range (40):
 ClinicSim(14400)
