# -*- coding: utf-8 -*-
import json

class PeNumbers():
    
    def __init__(self):
        self.result = None

    def return_p_e(self, number):
        try:
          if number%3 is 0 and number%5 is 0:
            self.result = "PE"
          elif number%3 is 0:
            self.result = "P"
          elif number%5 is 0:
            self.result = "E"
          else:
            self.result = number
        except TypeError:
          print('Invalid Input')

        return self.result


    def getResult(self, number):
      output_json = { "output" : self.return_p_e(number) }
      return json.dumps(output_json)
    
