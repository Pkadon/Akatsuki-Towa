label avg105904:
stop music

scene placeholderbackground
show sc052_01 3 as p59 at l(-25), light, zorder 6
with fade
c591 '[textdict[1219257]]'
hide p59
show sc052_01 3 as p59 at l(-25), light, zorder 6
c591 '[textdict[1219258]]'
hide p59
show sc052_01 3 as p59 at l(-25), dark, zorder 6
show oc001_01 22 as p1 at r(-2), light, zorder 5
c13 '[textdict[1219259]]'
hide p59
hide p1
show oc001_01 22 as p1 at r(-2), dark, zorder 5
show sc052_01 1 as p59 at l(-25), light, zorder 6
c591 '[textdict[1219260]]'
menu:
    extend ""
    "[textdict[1219261]]":
        call avg105905
    "[textdict[1219262]]":
        call avg105906
    "[textdict[1219263]]":
        call avg105907
return