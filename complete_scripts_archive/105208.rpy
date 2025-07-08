label avg105208:
stop music

scene placeholderbackground
$ update_portrait('sc052_01 3', 'p59', [l(-25), light, flip], 6)
window show
with fade_in
c591 '[textdict[1219268]]'
hide p59
$ update_portrait('sc052_01 3', 'p59', [l(-25), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1219269]]'
hide p59
hide p1
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc052_01 5', 'p59', [l(-25), light, flip], 6)
c591 '[textdict[1219270]]'
hide p1
hide p59
$ update_portrait('sc052_01 5', 'p59', [l(-25), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1219271]]'
menu:
    extend ""
    "[textdict[1219272]]":
        call avg105209
    "[textdict[1219273]]":
        call avg105210
    "[textdict[1219274]]":
        call avg105211
return