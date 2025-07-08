label avg20014:
stop music

play music "ED6518.ogg"
scene avg_bg_014
show oc001_01 8 as p1 at mid(-2), light, zorder 5
window show
with fade_in
c13 '[textdict[1000941]]'
hide p1
show oc002_01 8 as p2 at mid(-3), light, zorder 5
c23 '[textdict[1000942]]'
hide p2
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