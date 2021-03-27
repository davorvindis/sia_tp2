
# id	Fu	Ag	Ex	Re	Vi
class Items:
    def __init__(self, id, fu, ag, ex, re, vi):
        self.id = id
        self.fu = fu
        self.ag = ag
        self.ex = ex
        self.re = re
        self.vi = vi

    def __str__(self):
        return "id= " + str(self.id) + ", Fu= " + str(self.fu) + ", Ag= " + str(self.ag) + ", Ex= " + str(self.ex) + \
               ", Re= " + str(self.re) + ", Vi= " + str(self.vi)


