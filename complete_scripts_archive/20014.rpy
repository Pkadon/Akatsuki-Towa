label avg20014:
stop music

play music "ED6518.ogg"
scene avg_bg_014
with fade
show oc001_01 8 as c1portrait at centerpos(-2), zorder 5
c13 '[textdict[1000941]]'
hide c1portrait
show oc002_01 8 as c2portrait at centerpos(-3), zorder 5
c23 '[textdict[1000942]]'
hide c2portrait
c5173 '[textdict[1000943]]'
c5173 '[textdict[1000944]]'
c5173 '[textdict[1000945]]'
menu:
    extend ""
    "[textdict[1000946]]":
        call avg20015
    "[textdict[1000947]]":
        call avg20016
return