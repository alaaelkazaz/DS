
from Patient import *
class Doctor :
    def _init_(self ):  # defult state ( No patient & TimeRemaing ==0)
        patient1=patient(timeofarrival)
        self.Drate = patient1.patient()/5
        self.currentpatient = None
        self.timeReamaining = 0

    # THe Time which is pass through 4 hours from 12pm -4pm)
    def tick(self) :
        if self.currentpatient !=None:
            self.timeRemaining = self.timeRemaining -1
            # finally when time finish
            if self.timeRemaining == 0:
                self.currentpatient=None

    def busy(self): # Fn that makes sure if there's patient or not
        if self.currentpatient !=None:
            return True
        else:
            return False

    def Nextp(self,newp): # the Next one in queue to enter
        self.currentpatient = newp
        self.timeRemaining = newp.getpatient()*60/self.Drate