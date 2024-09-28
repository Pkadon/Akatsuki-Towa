label avg1002:
stop music

play music "ed7106.ogg"
scene avg_bg_023
with fade
c0 '[textdict[2100030]]'
show sc049_01 1 as c56portrait at leftside(-8), zorder 5
c561 '[textdict[2100031]]'
hide c56portrait
show sc049_01 1 as c56portrait at leftside(-8), zorder 5
c561 '[textdict[2100032]]'
hide c56portrait
show sc049_01 1 as c56portrait at leftside(-8), zorder 5
c561 '[textdict[2100033]]'
menu:
    "[textdict[2100034]]":
        call avg1003
    "[textdict[2100035]]":
        call avg1004
    "[textdict[2100036]]":
        call avg1005
return