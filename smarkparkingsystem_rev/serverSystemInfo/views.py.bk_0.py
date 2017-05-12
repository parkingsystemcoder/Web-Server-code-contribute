#Server System Info

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from django.db import models

#import classes from database
from carParkSlot.models import parkingslot #note parkingslot is from another apps, so <appsname>.models
from userInfo.models import user
from .models import systemInfo 

# Create your views here.

def index(request):
    
    all_systemInfo = systemInfo.objects.all()
    html = ''
    for userSystemInfo in all_systemInfo:
        url = '/serverSystemInfo/' + str(userSystemInfo.userID) + '/'
        html += '<a href="' + url + '">' + 'user id ' + str(userSystemInfo.userID) + '</a><br>'
    return HttpResponse(html)

def getUser(userID,all_user):
    for user in all_user:
        if str(user.userID) == userID:
            return user

def getParkingSlot(parkingslotID,all_parkingslot):
    for parkingslot in all_parkingslot:
        if parkingslot.parkingslotID == parkingslotID:
            return parkingslot

def getUserInServerSystem(userID,all_userInServerSystem):
    for userInServerSystem in all_userInServerSystem:
        if str(userInServerSystem.userID) == userID:
            return userInServerSystem 

def checkPaymentStatus(userID,all_user):
    for user in all_user:
        if str(user.userID) == userID:
            if user.userPaymentStatus == 'paid':
                paymentStatus = 1
            else:
                paymentStatus = 0
                
    return paymentStatus

def getVerificationCode(userID, all_user):
    for user in all_user:
        if str(user.userID) == userID:
            code = user.userCode
            return code
        else:
            return 0

def getParkingSlotID(code,all_parkingslot):
    for parkingslot in all_parkingslot:
        if parkingslot.parkingslotCode == code:
            parkingslotID = parkingslot.parkingslotID
    return parkingslotID

def putUserServerSystemInfo(user, parkingslot, userInServerSystem):
    userInServerSystem.userPaymentStatus = user.userPaymentStatus
    userInServerSystem.userCode = user.userCode
    userInServerSystem.parkingslotID = parkingslot.parkingslotID
    userInServerSystem.parkingslotStatus = parkingslot.parkingslotStatus
    userInServerSystem.parkingslotCode = parkingslot.parkingslotCode

def getUserServerSystemInfo(userInServerSystem):
    html = "<h2>Server system info for user id: "+ str(userInServerSystem.userID)+ "</h2><br> <h2> Payment status: "+ userInServerSystem.userPaymentStatus +"</h2><br> <h2> Verification code sent to user: "+ str(userInServerSystem.userCode) + "</h2><br> <h2> Parkingslot ID: "+ str(userInServerSystem.parkingslotID)+ "</h2><br> <h2> Parkingslot Status: "+ userInServerSystem.parkingslotStatus+ "</h2><br><h2> Verification Code entered by user: "+ str(userInServerSystem.parkingslotCode) +"</h2><br>"
    return html

def updateUserServerSystemInfo(userID, parkingslotID, all_user, all_parkingslot, all_userInServerSystem):
    user = getUser(userID,all_user)
    parkingslot = getParkingSlot(parkingslotID,all_parkingslot)
    """
    if parkingslot == 0:
        html ="<h2> can't find parking slot object <h2><br>"
    else:
        html ="<h2> parking slot id: "+ str(parkingslot.parkingslotID) + "<h2><br>"
    """
    userInServerSystem = getUserInServerSystem(userID,all_userInServerSystem)
    putUserServerSystemInfo(user, parkingslot,userInServerSystem)
    html = getUserServerSystemInfo(userInServerSystem)
    return html


def main(request,userID):
    all_user = user.objects.all()
    all_parkingslot = parkingslot.objects.all()
    all_userInServerSystem = systemInfo.objects.all()    
    paymentStatus = checkPaymentStatus(userID, all_user)
    if paymentStatus == 1:
        code = getVerificationCode(userID,all_user)
        if code != 0:
            parkingslotID = getParkingSlotID(code, all_parkingslot)
            html = updateUserServerSystemInfo(userID, parkingslotID, all_user, all_parkingslot, all_userInServerSystem)

        #html ="<h2> Test main loop <h2><br> <h2> paymentStatus : "+ str(paymentStatus)+"<h2><br> <h2> code : "+ str(code)+"<h2><br> <h2> parkingslotID : "+ str(parkingslotID)+"<h2><br>"
        return HttpResponse(html)
    else:
        html ="<h2> Test main loop <h2><br>"
        return HttpResponse(html)

