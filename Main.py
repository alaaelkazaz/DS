
import queue
from Doctor import *
from Patient import *

import random


def ClinicSim(w):  # simulation for doctor clinic
    Doctork = Doctor()  # time for patient to enter the clinic
    PatientQ =queue()  # creating anew queue
    TimeWaiting = []  # create alist
    for currentsec in range(w):  # w is the time we enter ( 4 hours = 4*60*60 )
        if random.randrange(1, 361) ==360: #checks the probability of arrival of a patient at any given second
            patient = Patient(currentsec)
            PatientQ.enqueue(patient)  # adding the patient to the queue
            if (not Doctor.busy()) and ( not PatientQ.isEmpty()):  # check if the doctor is not busy and if there is a patient
                Nextp = PatientQ.dequeue()  # delete patient from queue
                TimeWaiting.append(
                    newp.waitTime(currentsec))  # error, but we didn't solve it   # adding the time to the list
                Doctork.newp(Nextp)
                Doctork.tick()
                averagewait = sum(TimeWaiting) / len(TimeWaiting)  # calculate the average wait

    print("Average Wait is ", averagewait, "min and ", PatientQ.size(), " task remaining .")


for i in range (40):
    ClinicSim(14400)
