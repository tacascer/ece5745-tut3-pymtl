#=========================================================================
# MinMaxUnit
#=========================================================================
# This module takes two inputs, compares them, and outputs the larger
# via the "max" output port and the smaller via the "min" output port.

from pymtl3 import *

class MinMaxUnit( Component ):

  # Constructor

  def construct( s, nbits ):

    s.in0     = InPort ( nbits )
    s.in1     = InPort ( nbits )
    s.out_min = OutPort( nbits )
    s.out_max = OutPort( nbits )

    # ''' TUTORIAL TASK ''''''''''''''''''''''''''''''''''''''''''''''''''
    # This model is incomplete. As part of the tutorial you will insert
    # logic here to implement the min/max unit. You should also write a
    # unit test from scratch named MinMaxUnit_test.py.
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    @update
    def block():
      if s.in0 >= s.in1:
        s.out_max @= s.in0
        s.out_min @= s.in1
      else:
        s.out_max @= s.in1
        s.out_min @= s.in0

