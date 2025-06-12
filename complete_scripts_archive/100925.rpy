label avg100925:
stop music

stop music
scene placeholderbackground
with fade
show sc001_01 2 as c9portrait at centerpos(-11), zorder 5
c93 '[textdict[1218088]]'
stop music
play sfxvoice "bcv_oc002_win_02.ogg"
show oc001_01 1 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1218089]]'
stop music
hide c1portrait
show oc001_01 1 as c1portrait at darkright(-2), zorder 5
show sc001_01 1 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218090]]'
stop music
hide c9portrait
hide c1portrait
show oc001_01 1 as c1portrait at darkright(-2), zorder 5
show sc001_01 5 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218091]]'
stop music
play sfxvoice "bcv_oc002_win_02.ogg"
hide c1portrait
hide c9portrait
show sc001_01 5 as c9portrait at darkleft(-11), zorder 6
show oc001_01 1 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1218092]]'
menu:
    extend ""
    "[textdict[1218093]]":
        call avg100926
    "[textdict[1218094]]":
        call avg100927
    "[textdict[1218095]]":
        call avg100928
return