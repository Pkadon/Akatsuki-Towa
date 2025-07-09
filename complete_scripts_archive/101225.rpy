label avg101225:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1220730]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc004_01 1', 'p12', [l(-12), light, flip], 6)
c121 '[textdict[1220731]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc004_01 1', 'p12', [l(-12), light, flip], 6)
c121 '[textdict[1220732]]'
menu:
    extend ""
    "[textdict[1220733]]":
        call avg101226
    "[textdict[1220734]]":
        call avg101227
    "[textdict[1220735]]":
        call avg101228
return