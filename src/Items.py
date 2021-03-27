
# id	Fu	Ag	Ex	Re	Vi
class Items:
    def __init__(self, id, fu, ag, ex, re, vi):
        self.id = int(id)
        self.fu = float(fu)
        self.ag = float(ag)
        self.ex = float(ex)
        self.re = float(re)
        self.vi = float(vi)

    def __str__(self):
        return "id= " + str(self.id) + ", Fu= " + str(self.fu) + ", Ag= " + str(self.ag) + ", Ex= " + str(self.ex) + \
               ", Re= " + str(self.re) + ", Vi= " + str(self.vi)


