label avg10403:
stop music

play music "ED6518.ogg"
scene avg_bg_001
with fade
show oc001_01 4 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1140280]]'
hide c1portrait
show oc001_01 4 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1140282]]'
menu:
    extend ""
    "[textdict[1140283]]":
        call avg10404
    "[textdict[1140284]]":
        call avg10405
return