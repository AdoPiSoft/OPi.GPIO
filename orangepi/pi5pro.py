# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Orange PI 5 Pro

Usage:

.. code:: python
   from orangepi import pi5pro
   from OPi import GPIO

   GPIO.setmode(pi5pro.BOARD) or GPIO.setmode(pi5pro.BCM)
"""

# Orange Pi 5 Pro physical board pin to GPIO pin
# GPIO formula is: (pin letter index) * 8 + pin

BOARD = {
    3: 59,  # 'GPIO1_D3',
    5: 58,  # 'GPIO1_D2',
    7: 47,  # 'GPIO1_B7',
    11: 138,  # 'GPIO4_B2',
    13: 139,  # 'GPIO4_B3',
    15: 46,  # 'GPIO1_B6',
    19: 42,  # 'GPIO1_B2',
    21: 41,  # 'GPIO1_B1',
    23: 43,  # 'GPIO1_B3',
    27: 34,  # 'GPIO1_A2',
    29: 36,  # 'GPIO1_A4',
    31: 38,  # 'GPIO1_A6',
    33: 63,  # 'GPIO1_D7',
    35: 135,  # 'GPIO4_A7',
    37: 134,  # 'GPIO4_A6',

    # 2nd line of pins
    8: 13,  # 'GPIO0_B5',
    10: 14,  # 'GPIO0_B6',
    12: 39,  # 'GPIO1_A7',
    16: 33,  # 'GPIO1_A1',
    18: 32,  # 'GPIO1_A0',
    22: 40,  # 'GPIO1_B0',
    24: 44,  # 'GPIO1_B4',
    26: 45,  # 'GPIO1_B5',
    28: 35,  # 'GPIO1_A3',
    32: 62,  # 'GPIO1_D6',
    36: 131,  # 'GPIO4_A3',
    38: 132,  # 'GPIO4_A4',
    40: 133,  # 'GPIO4_A5'
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
