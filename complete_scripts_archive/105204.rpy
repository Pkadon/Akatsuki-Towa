label avg105204:
stop music

scene placeholderbackground
show sc052_01 3 as p59 at l(-25), light, flip, zorder 6
window show
with fade_in
c591 '[textdict[1219257]]'
hide p59
show sc052_01 3 as p59 at l(-25), light, flip, zorder 6
c591 '[textdict[1219258]]'
hide p59
show sc052_01 3 as p59 at l(-25), dark, flip, zorder 6
show oc001_01 22 as p1 at r(-2), light, zorder 5
c13 '[textdict[1219259]]'
hide p59
hide p1
show oc001_01 22 as p1 at r(-2), dark, zorder 5
show sc052_01 1 as p59 at l(-25), light, flip, zorder 6
c591 '[textdict[1219260]]'
menu:
    extend ""
    "[textdict[1219261]]":
        call avg105205
    "[textdict[1219262]]":
        call avg105206
    "[textdict[1219263]]":
        call avg105207
return