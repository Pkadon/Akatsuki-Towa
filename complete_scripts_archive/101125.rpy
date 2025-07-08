label avg101125:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1220456]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc003_01 2', 'p11', [l(-4), light, flip], 6)
c111 '[textdict[1220457]]'
hide p1
$ update_portrait('sc003_01 2', 'p11', [l(-4), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1220458]]'
menu:
    extend ""
    "[textdict[1220459]]":
        call avg101126
    "[textdict[1220460]]":
        call avg101127
    "[textdict[1220461]]":
        call avg101128
return