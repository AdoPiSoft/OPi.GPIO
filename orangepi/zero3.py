# pin number = (position of letter in alphabet - 1) * 32 + pin number So, PD14 will be (4 - 1) * 32 + 14 = 110
# Orange Pi Zero 3 physical board pin to GPIO pin

# Source: https://github.com/rm-hull/OPi.GPIO/issues/79

"""
Usage:
.. code:: python
   from orangepi import zero3
   from OPi import GPIO
   GPIO.setmode(zero3.BOARD)
"""

BOARD = {
    3: 229, # PH5/I2C3_SDA
    5: 228, # PH4/I2C3_SCK
    7: 73, # PC9
    8: 226, # PH2/UART5_TX
    10: 227, # PH3/UART5_RX
    11: 70, # PC6
    12: 75, # PC11
    13: 69, # PC5
    15: 72, # PC8
    16: 79, # PC15
    18: 78, # PC14
    19: 231, # PH7,SPI1_MOSI
    21: 232, # PH8,SPI1_MISO
    22: 71, # PC7
    23: 230, # PH6,SPI1_CLK
    24: 233, # PH9,SPI1_CS
    26: 74, # PC10
    27: 234, # PH10/UART6_TX
    28: 235, # PH11/UART6_RX
    29: 236, # PH12/I2C4_SDA
    30: 237, # PH13/I2C4_SCK
    31: 238, # PH14/SPI2_MOSI
    33: 239, # PH15/SPI2_MISO
    34: 240, # PH16/SPI2_CLK
    35: 241, # PH17/SPI2_CS
    36: 242, # PH18/UART7_TX
    37: 243, # PH19/UART7_RX
}

# BCM mapping not identified yet, keeping it for compatibility
BCM = BOARD
