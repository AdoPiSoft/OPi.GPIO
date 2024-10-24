# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI 5 Pro

Usage:

.. code:: python
   from orangepi import pi5plus
   from OPi import GPIO

   GPIO.setmode(pi5plus.BOARD) or GPIO.setmode(pi5plus.BCM)
"""

# Orange Pi 5 Plus physical board pin to GPIO pin
# GPIO formula is: GPIO num * 32 + (pin letter index) * 8 + pin
# Example: GPIO0_C0 = (0 * 32) + (2 * 8) + 0 = 16, thus board pin 3 : 16

BOARD = {
    3: 16,   # 'GPIO0_C0'  = (0 * 32) + (2 * 8) + 0 = 16
    5: 15,   # 'GPIO0_B7'  = (0 * 32) + (1 * 8) + 7 = 15
    7: 62,   # 'GPIO1_D6'  = (1 * 32) + (3 * 8) + 6 = 62
    11: 36,  # 'GPIO1_A4'  = (1 * 32) + (0 * 8) + 4 = 36
    13: 39,  # 'GPIO1_A7'  = (1 * 32) + (0 * 8) + 7 = 39
    15: 40,  # 'GPIO1_B0'  = (1 * 32) + (1 * 8) + 0 = 40
    19: 42,  # 'GPIO1_B2'  = (1 * 32) + (1 * 8) + 2 = 42
    21: 41,  # 'GPIO1_B1'  = (1 * 32) + (1 * 8) + 1 = 41
    23: 43,  # 'GPIO1_B3'  = (1 * 32) + (1 * 8) + 3 = 43
    27: 47,  # 'GPIO1_B7'  = (1 * 32) + (1 * 8) + 7 = 47
    29: 63,  # 'GPIO1_D7'  = (1 * 32) + (3 * 8) + 7 = 63
    31: 96,  # 'GPIO3_A0'  = (3 * 32) + (0 * 8) + 0 = 96
    33: 106, # 'GPIO3_C2'  = (3 * 32) + (2 * 8) + 2 = 106
    35: 98,  # 'GPIO3_A2'  = (3 * 32) + (0 * 8) + 2 = 98
    37: 105, # 'GPIO3_C1'  = (3 * 32) + (2 * 8) + 1 = 105

    # 2nd line of pins
    8: 33,   # 'GPIO1_A1'  = (1 * 32) + (0 * 8) + 1 = 33
    10: 32,  # 'GPIO1_A0'  = (1 * 32) + (0 * 8) + 0 = 32
    12: 97,  # 'GPIO3_A1'  = (3 * 32) + (0 * 8) + 1 = 97
    16: 93,  # 'GPIO3_B5'  = (3 * 32) + (1 * 8) + 5 = 93
    18: 92,  # 'GPIO3_B6'  = (3 * 32) + (1 * 8) + 6 = 92
    22: 34,  # 'GPIO1_A2'  = (1 * 32) + (0 * 8) + 2 = 34
    24: 44,  # 'GPIO1_B4'  = (1 * 32) + (1 * 8) + 4 = 44
    26: 45,  # 'GPIO1_B5'  = (1 * 32) + (1 * 8) + 5 = 45
    28: 46,  # 'GPIO1_B6'  = (1 * 32) + (1 * 8) + 6 = 46
    32: 35,  # 'GPIO1_A3'  = (1 * 32) + (0 * 8) + 3 = 35
    36: 101, # 'GPIO3_A5'  = (3 * 32) + (0 * 8) + 5 = 101
    38: 100, # 'GPIO3_A4'  = (3 * 32) + (0 * 8) + 4 = 100
    40: 99,  # 'GPIO3_A3'  = (3 * 32) + (0 * 8) + 3 = 99
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
