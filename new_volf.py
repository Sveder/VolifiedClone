################################################################################
#                   Michael Sverdlin        2/2010                             #
#           A volified clone - working name "Volified new gen"                 #
#                                                                              #
# TODO : Version 0.1:                                                          #
#       Make the ship run when pressing a long key                           V #
#       Make the ship turn to whatever direction needed                      V #
#       Ship moves on the line                                               V #
#       Faster fill rects algorithm                                            #
#       Statistical choosing from a dictionary of background pictures          #
#       Make an enemy class                                                    #
#       Make the eating of hte surface work                                    #
#       Pretty evrything up and make it FASTER!                                #
#                                                                              #
################################################################################

#-------------------------------------------------------------------------------
#IMPORTS
#-------------------------------------------------------------------------------

import os
import sys
import logging
import traceback
import configparser

import Image
import pygame
from pygame.locals import *
pygame.init()                               #Initialize all of the pygame parts

#-------------------------------------------------------------------------------
#GLOBALS
#-------------------------------------------------------------------------------

#Debug level:
DEBUG = True
MAIN_INI_FILE = "game.ini"
SETTINGS = Settings()

#-------------------------------------------------------------------------------
#FUNCTIONS
#-------------------------------------------------------------------------------

def log(message, trace=False):
    """
    Write the message to all the log devices.
    """


#-------------------------------------------------------------------------------
#CLASSES
#-------------------------------------------------------------------------------

#Just a settings class for everything we need to check:
class Settings: pass


#-------------------------------------------------------------------------------
#MAIN
#-------------------------------------------------------------------------------

def main():
    try:
        pass
    except:
        log("Main failed WOOT:\n%s" % traceback.format_exc())
        raise

if __name__ == "__main__":
    main()