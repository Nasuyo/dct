#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 10:26:43 2022

@author: nasuyo
"""

## Imports --------------------------------------------------------------------
import astropy.constants as const

## Constants ------------------------------------------------------------------
c = const.c.value  # speed of light [m/s]
G = const.G.value  # gravitational constant [m³/s²/kg]
M = const.M_earth.value  # mass of the Earth [kg]
R = const.R_earth.value  # radius of the Earth [m]

## Options --------------------------------------------------------------------
h_diff = 2  # height difference between two clocks [m]

## Calculations ---------------------------------------------------------------
ff = h_diff / c**2 * G * M / R**2  # fractional frequency difference [-]
print('A height difference of ' + '{0:.1f}'.format(h_diff) + ' meters between' +
      ' two clocks results in a fractional frequency difference of ' + 
      '{:.2e}'.format(ff) + '.')

