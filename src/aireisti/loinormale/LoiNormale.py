# -*- coding: utf-8 -*-

import math
import pyerf
import numbers

class LoiNormale():
    def __init__(self, a, b, p=None):
        if p is None:
            self.mu = a
            self.sigma = b
        else: 
            self.mu = (a+b)/2
            self.sigma = (a-self.mu)/LoiNormale.fractile((1-p)/2)

    def proba(self, a, b=None):
        if b is None:
            return 0.5*(1+math.erf((a-self.mu)/(self.sigma*math.sqrt(2))))
        else:
            pa = self.proba(a)
            pb = self.proba(b)
            return pb-pa
    
    @staticmethod
    def fractile(p):
        return math.sqrt(2) * pyerf.erfinv(2*p-1)

    def __repr__(self):
        return "<%s N(%.2f, %.2f²)>" % (
            self.__class__.__name__, self.mu, self.sigma)


    def __add__(self, other):
        if isinstance(other, LoiNormale):
            return LoiNormale(self.mu + other.mu, 
                              math.sqrt(self.sigma**2 + other.sigma**2))
        elif isinstance(other, numbers.Number):
            return LoiNormale(self.mu + other, self.sigma)
        else:
            raise TypeError("Addition impossible entre '%s' et '%s'" % 
                            (self.__class__.__name__,
                             other.__class__.__name__))
    def __mul__(self, cste):
        if isinstance(cste, numbers.Number):
            return LoiNormale(self.mu*cste, self.sigma*cste)
        else:
            raise TypeError("Multiplication impossible entre '%s' et '%s'" % 
                            (self.__class__.__name__,
                             other.__class__.__name__)) 
        
    def __truediv__(self, cste):
        if isinstance(cste, numbers.Number):
            return LoiNormale(self.mu/cste, self.sigma/cste)
        else:
            raise TypeError("Division impossible entre '%s' et '%s'" % 
                            (self.__class__.__name__,
                             other.__class__.__name__)) 

# vim:set et sts=4 ts=4 tw=80:
