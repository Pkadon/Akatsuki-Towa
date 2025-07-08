label avg102725:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1219507]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc019_01 1', 'p27', [l(-18), light, flip], 6)
c271 '[textdict[1219508]]'
hide p27
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc019_01 4', 'p27', [l(-18), light, flip], 6)
c271 '[textdict[1219509]]'
menu:
    extend ""
    "[textdict[1219510]]":
        call avg102726
    "[textdict[1219511]]":
        call avg102727
    "[textdict[1219512]]":
        call avg102728
return