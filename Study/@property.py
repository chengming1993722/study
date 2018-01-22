##class Student(object):
##
##    @property
##    def score(self):
##        return self._score
##
##    @score.setter
##    def score(self, value):
##        if not isinstance(value, int):
##            raise ValueError('score must be an integer!')
##        if value < 0 or value > 100:
##            raise ValueError('score must between 0 ~ 100!')
##        self._score = value5

class Screen(object):
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        self._width = value
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height = value
    
    @property
    def resolution(self):
        if self._width * self._height == 786432:
            print("OK!")
        else:
            print("NO!!!")
        return "yes"


    
        
    













    
