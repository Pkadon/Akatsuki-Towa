label avg20112:
stop music

play music "ed7150.ogg"
scene avg_bg_038
with fade
show oc002_01 2 as c2portrait at rightside(-3), zorder 5
c23 '[textdict[1005447]]'
hide c2portrait
show oc002_01 2 as c2portrait at darkright(-3), zorder 5
show oc001_01 8 as c1portrait at leftside(-2), zorder 5
c11 '[textdict[1001032]]'
menu:
    "[textdict[1005449]]":
        call avg10092
    "[textdict[1005450]]":
        call avg10094
return