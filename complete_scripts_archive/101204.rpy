label avg101204:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1220670]]'
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('sc004_01 2', 'p12', [l(-12), light, flip], 6)
c121 '[textdict[1220671]]'
hide p1
hide p12
$ update_portrait('sc004_01 2', 'p12', [l(-12), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1220672]]'
menu:
    extend ""
    "[textdict[1220673]]":
        call avg101205
    "[textdict[1220674]]":
        call avg101206
    "[textdict[1220675]]":
        call avg101207
return