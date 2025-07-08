label avg105921:
stop music

scene placeholderbackground
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
window show
with fade_in
c591 '[textdict[1219308]]'
hide p59
$ update_portrait('sc052_01 1', 'p59', [l(-25), light, flip], 6)
c591 '[textdict[1219309]]'
$ update_portrait('sc052_01 1', 'p59', [l(-25), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1219310]]'
hide p59
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 5', 'p59', [l(-25), light, flip], 6)
c591 '[textdict[1219311]]'
menu:
    extend ""
    "[textdict[1219312]]":
        call avg105922
    "[textdict[1219313]]":
        call avg105923
    "[textdict[1219314]]":
        call avg105924
return