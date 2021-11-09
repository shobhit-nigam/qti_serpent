dicta = {'aa':20, 'bb':30, 'cc':40, 'dd':50}

dictb = {key:val for (key, val) in dicta.items() if val%20==0}

print(dictb)
