label avg20098:
stop music

play music "ed7104.ogg"
scene avg_bg_027
with fade
play sfx2 "other_7043.ogg"
show oc001_01 2 as c1portrait at leftsideentrance(-2), zorder 5
c11 '[textdict[str(1004834)]]'
hide c1portrait
show oc001_01 2 as c1portrait at darkleft(-2), zorder 6
show oc002_01 10 as c2portrait at rightside(-3), zorder 5
c23 '[textdict[str(1004835)]]'
play sfxvoice "avg_vocal_na06.ogg"
hide c1portrait
hide c2portrait
show oc002_01 10 as c2portrait at darkright(-3), zorder 5
show oc001_01 8 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[str(1004836)]]'
return