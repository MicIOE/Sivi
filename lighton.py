#!/usr/bin/python

#coding: utf8

import sys

import RPi.GPIO as GPIO

PORT=31

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(PORT,GPIO.OUT)

GPIO.setup(PORT,GPIO.LOW)
