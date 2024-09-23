label avg102004:
stop music

stop music
scene placeholderbackground
with fade
show sc012_01 2 as c20portrait at leftside(-16), zorder 5
c201 '[textdict[1218639]]'
stop music
hide c20portrait
show sc012_01 2 as c20portrait at darkleft(-16), zorder 6
show oc001_01 4 as c1portrait at rightside(-2), zorder 5
c13 '[textdict[1218640]]'
stop music
hide c20portrait
hide c1portrait
show oc001_01 4 as c1portrait at darkright(-2), zorder 5
show sc012_01 4 as c20portrait at leftside(-16), zorder 5
c201 '[textdict[1218641]]'
menu:
    "[textdict[1218642]]":
        call avg102005
    "[textdict[1218643]]":
        call avg102006
    "[textdict[1218644]]":
        call avg102007
return