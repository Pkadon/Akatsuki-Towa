label avg102021:
stop music

scene placeholderbackground
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
window show
with fade_in
c201 '[textdict[1218685]]'
$ update_portrait('sc012_01 4', 'p20', [l(-16), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1218686]]'
hide p20
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc012_01 1', 'p20', [l(-16), light, flip], 6)
c201 '[textdict[1218687]]'
menu:
    extend ""
    "[textdict[1218688]]":
        call avg102022
    "[textdict[1218689]]":
        call avg102023
    "[textdict[1218690]]":
        call avg102024
return