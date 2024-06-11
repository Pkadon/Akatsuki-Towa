label avg100904:
stop music

stop music
scene placeholderbackground
with fade
show sc001_01 4 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218021]]'
stop music
hide c9portrait
show sc001_01 2 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218022]]'
stop music
play sfxvoice "avg_vocal_na02.ogg"
hide c9portrait
show sc001_01 2 as c9portrait at darkleft(-11), zorder 6
show oc001_01 2 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1218023]]'
stop music
hide c9portrait
hide c1portrait
show oc001_01 2 as c1portrait at darkright(-2), zorder 5
show sc001_01 1 as c9portrait at leftside(-11), zorder 5
c91 '[textdict[1218024]]'
menu:
    "[textdict[1218025]]":
        call avg100905
    "[textdict[1218026]]":
        call avg100906
    "[textdict[1218026]]":
        call avg100907
return