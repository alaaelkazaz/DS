import random

class Patient:
   def _init_(self,arrival):
     self.arrival = arrival
     self.patient = random.randrange(1,41)

   def getArrival(self):
     return self.arrival

   def getPatient(self):
      return self.patient

   def waitTime(self, currenttime):
      return currenttime - self.arrival