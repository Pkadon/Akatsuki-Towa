label avg1006:
stop music

play music "ed7106.ogg"
scene avg_bg_023
with fade
show sc049_01 1 as c56portrait at leftside(-8), zorder 5
c561 '[textdict[str(2100084)]]'
hide c56portrait
show sc049_01 1 as c56portrait at leftside(-8), zorder 5
c561 '[textdict[str(2100085)]]'
hide c56portrait
show sc049_01 1 as c56portrait at leftside(-8), zorder 5
c561 '[textdict[str(2100086)]]'
hide c56portrait
show sc049_01 1 as c56portrait at darkleft(-8), zorder 6
show oc001_01 17 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[str(2100087)]]'
hide c56portrait
hide c1portrait
show oc001_01 17 as c1portrait at darkright(-2), zorder 5
show sc049_01 4 as c56portrait at leftside(-8), zorder 5
c561 '[textdict[str(2100088)]]'
hide c56portrait
hide c1portrait
show oc001_01 17 as c1portrait at darkright(-2), zorder 5
show sc049_01 1 as c56portrait at leftside(-8), zorder 5
c561 '[textdict[str(2100089)]]'
menu:
    "[textdict[str(2100091)]]":
        call avg1007
    "[textdict[str(2100092)]]":
        call avg1008
    "[textdict[str(2100093)]]":
        call avg1009
return