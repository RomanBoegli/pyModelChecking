#!/usr/bin/env python

from pyModelChecking import Kripke
from pyModelChecking.CTL import *
#from pyModelChecking.CTLS import *

import unittest

__author__ = "Alberto Casagrande"
__copyright__ = "Copyright 2015"
__credits__ = ["Alberto Casagrande"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Alberto Casagrande"
__email__ = "acasagrande@units.it"
__status__ = "Development"

class TestCTLModelChecking(unittest.TestCase):
    def setUp(self):
        self.problems=[(Kripke(R=[(0,0),(0,1),(1,2),(2,2)],
                               L={0:set([]),
                                  1:set(['p']),
                                  2:set(['q'])}),
                          [ (Bool(True),set([0,1,2])),
                            (Bool(False),set([])),
                            (Not(True),set([])),
                            (E(G('p')),set([]))]
                        ),
                        (Kripke(S=[0,1,2,3],
                          R=[(0,1),(1,2),(2,2),(1,3),(3,3)],
                          L={0:set(['p','q']),
                             1:set(['q']),
                             2:set(['p']),
                             3:set(['q'])}),
                          [(EG(And(Or(Not('p'),'q'),EF(And('q',Not('p'))))),
                            set([0,1,3]))]),
                       (Kripke(R=[(0,1),(0,2),(1,4),(4,1),(4,2),(2,0),
                                  (3,2),(3,0),(3,3),(6,3),(2,5),(5,6)],
                               L={0:set(),
                                  1:set(['Start','Error']),
                                  2:set(['Close']),
                                  3:set(['Close','Heat']),
                                  4:set(['Start','Close','Error']),
                                  5:set(['Start','Close']),
                                  6:set(['Start','Close','Heat'])}),
                           [(AG(Imply('Start',AF('Heat'))),set([]))])]

    def test_modelchecking(self):
        for kripke,instances in self.problems:
            for formula,solution in instances:
                S=modelcheck(kripke,formula)

                self.assertEquals(S,solution)

if __name__ == '__main__':
    unittest.main()