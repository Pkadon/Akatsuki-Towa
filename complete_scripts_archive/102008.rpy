label avg102008:

stop music
scene placeholderbackground
$ update_portrait('sc012_01 4', 'p20', [l(-16), light, flip], 6)
$ update_narrator('c201')
window show
with fade_in
c201 '[convertstrid(1218649)]'
$ update_portrait('sc012_01 4', 'p20', [l(-16), dark, flip], 5)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1218650)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc012_01 1', 'p20', [l(-16), light, flip], 6)
c201 '[convertstrid(1218651)]'
menu:
    extend ""
    "[textdict[1218652]]":
        call avg102009
    "[textdict[1218653]]":
        call avg102010
    "[textdict[1218654]]":
        call avg102011
return