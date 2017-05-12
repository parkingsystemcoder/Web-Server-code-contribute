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
    
    all_userInServerSystem = systemInfo.objects.all()
    html = ''
    for userInServerSystem in all_userInServerSystem:
        url = '/serverSystemInfo/' + str(userInServerSystem.id) + '/'
        html += '<a href="' + url + '">' + 'user id ' + str(userInServerSystem.id) + '</a><br>'
        resetUserServerSystemInfo(userInServerSystem)
        return HttpResponse(html)

def getUser(userID,all_user):
    for user in all_user:
        if str(user.id) == userID:
            return user

def getParkingSlot(code,all_parkingslot):
    parkingslotLocated = 0
    status = 0
    for parkingslot in all_parkingslot:
        if parkingslot.code == code:
            status = 1
            parkingslotLocated = parkingslot
    return parkingslotLocated,status

def getUserInServerSystem(userID,all_userInServerSystem):
    for userInServerSystem in all_userInServerSystem:
        if str(userInServerSystem.id) == userID:
            return userInServerSystem 

def resetUserServerSystemInfo(userInServerSystem):
    userInServerSystem.userPaymentStatus = "NA"
    userInServerSystem.userCode = "NA"
    userInServerSystem.parkingslotID = "NA"
    userInServerSystem.parkingslotStatus = "NA"
    userInServerSystem.parkingslotCode = "NA"
    userInServerSystem.save()

def checkPaymentStatus(user):
    if user.paystatus == 1:
        paymentStatus = "paid"
    else:
        paymentStatus = "unpaid"
                
    return paymentStatus

def getVerificationCode(user):
    code = user.code
    return code

def putServerSystemUserInfo(user, userInServerSystem, userCodeStatus):
    userInServerSystem.userName =  user.username
    if user.paystatus == 0:
        userInServerSystem.userPaymentStatus = "unpaid"
    elif user.paystatus == 1:
        userInServerSystem.userPaymentStatus = "paid"

    if userCodeStatus == 0:
        userInServerSystem.userCode = "NA"
    elif userCodeStatus == 1:
        userInServerSystem.userCode = str(user.code)
    
    userInServerSystem.save()
    
def putServerSystemParkingSlotInfo(parkingslot, userInServerSystem):
    userInServerSystem.parkingslotID = str(parkingslot.id)
    if parkingslot.status == 0:
        userInServerSystem.parkingslotStatus = "occupied"
    elif parkingslot.status == 1:
        userInServerSystem.parkingslotStatus = "available"
    userInServerSystem.parkingslotCode = str(parkingslot.code)
    userInServerSystem.save()
    
def getServerSystemInfo(userInServerSystem, parkingslotSearchStatus):
    html_id         ="<h2> Server system info for user id : "+ str(userInServerSystem.id)+  "</h2><br>"
    html_username   ="<h2> Username : "+ userInServerSystem.userName +  "</h2><br>"
    html_paystatus  ="<h2> Payment status: "+ userInServerSystem.userPaymentStatus +    "</h2><br>"
    html_usercode   ="<h2> Verification code sent to user: "+ userInServerSystem.userCode +  "</h2><br>"
    html_parkingslotID      ="<h2> Parkingslot ID: "+ userInServerSystem.parkingslotID +    "</h2><br>"
    html_parkingslotStatus  ="<h2> Parkingslot Status: "+ userInServerSystem.parkingslotStatus +    "</h2><br>"
    html_parkingslotCode    ="<h2> Verification Code entered by user: "+ userInServerSystem.parkingslotCode +   "</h2><br>"
    html_noMatchParkingSlotFound ="<h2> No match parking slot found, user may not key in verification code correctly </h2><br>"
    if parkingslotSearchStatus == 1:
        html =  html_id + html_username + html_paystatus + html_usercode + html_parkingslotID + html_parkingslotStatus + html_parkingslotCode
    else:
        html =  html_id + html_username + html_paystatus + html_usercode + html_noMatchParkingSlotFound + html_parkingslotID + html_parkingslotStatus + html_parkingslotCode
    return html



def main(request,userID): #userID pass back is string type

    #initialization
    all_user                    = user.objects.all()
    all_parkingslot             = parkingslot.objects.all()
    all_userInServerSystem      = systemInfo.objects.all()
    currentUser                 = getUser(userID,all_user)
    currentUserInServerSystem   = getUserInServerSystem(userID,all_userInServerSystem)
    resetUserServerSystemInfo(currentUserInServerSystem)

    paymentStatus = checkPaymentStatus(currentUser)
    
    if paymentStatus == "paid":
        code = getVerificationCode(currentUser)
        
        if code != 0:
            userCodeStatus = 1
            currentParkingSlot,parkingslotSearchStatus = getParkingSlot(code, all_parkingslot)
            if parkingslotSearchStatus == 1:
                putServerSystemParkingSlotInfo(currentParkingSlot, currentUserInServerSystem)
                putServerSystemUserInfo(currentUser, currentUserInServerSystem, userCodeStatus)
                html = getServerSystemInfo(currentUserInServerSystem,parkingslotSearchStatus)
            else:
                putServerSystemUserInfo(currentUser, currentUserInServerSystem, userCodeStatus = 1)
                html = getServerSystemInfo(currentUserInServerSystem, parkingslotSearchStatus)
        else:
            userCodeStatus = 0
            putServerSystemUserInfo(currentUser, currentUserInServerSystem, userCodeStatus)
            html = getServerSystemInfo(currentUserInServerSystem,parkingslotSearchStatus = 0)
    else:
        putServerSystemUserInfo(currentUser, currentUserInServerSystem, userCodeStatus = 1)
        html = getServerSystemInfo(currentUserInServerSystem, parkingslotSearchStatus = 0)
    
    return HttpResponse(html)

