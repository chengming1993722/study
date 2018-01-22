import re
def tryint(s):
    try:
        return int(s)
    except:
        return s

def alphanum_key(s):
    return [tryint(c) for c in re.split('([0-9]+)',s) ]




if __name__ =="__main__":
    a=['S31S10_new', 'S31S11_new', 'S31S12_new', 'S31S8_new', 'S31S9_new']
    a.sort(key=lambda v:alphanum_key(v))
    
