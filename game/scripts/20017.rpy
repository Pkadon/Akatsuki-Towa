label avg20017:
stop music

play music "ED6101.ogg"
scene placeholderbackground
with fade
play sfx2 "other_7017.ogg"
show oc001_01 11 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1001028)]]'
play sfx2 "other_7064.ogg"
hide c1portrait
show oc001_01 1 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1001029)]]'
hide c1portrait
show oc001_01 10 as c1portrait at centerpos(-2), zorder 5
c12 '[textdict[str(1001030)]]'
hide c1portrait
show oc002_01 1 as c2portrait at centerpos(-3), zorder 5
c22 '[textdict[str(1001031)]]'
return