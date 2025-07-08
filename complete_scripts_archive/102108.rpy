label avg102108:
stop music

scene placeholderbackground
$ update_portrait('sc013_01 5', 'p21', [l(-12), light, flip], 6)
window show
with fade_in
c211 '[textdict[1218830]]'
$ update_portrait('sc013_01 5', 'p21', [l(-12), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1218831]]'
hide p21
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc013_01 1', 'p21', [l(-12), light, flip], 6)
c211 '[textdict[1218832]]'
menu:
    extend ""
    "[textdict[1218833]]":
        call avg102109
    "[textdict[1218834]]":
        call avg102110
    "[textdict[1218835]]":
        call avg102111
return