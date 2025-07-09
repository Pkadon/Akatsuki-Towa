label avg103008:
stop music

scene placeholderbackground
$ update_portrait('sc022_01 1', 'p30', [l(-9), light, flip], 6)
window show
with fade_in
c301 '[textdict[1222432]]'
$ update_portrait('sc022_01 1', 'p30', [l(-9), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1222433]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc022_01 1', 'p30', [l(-9), light, flip], 6)
c301 '[textdict[1222434]]'
$ update_portrait('sc022_01 1', 'p30', [l(-9), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1222435]]'
menu:
    extend ""
    "[textdict[1222436]]":
        call avg103009
    "[textdict[1222437]]":
        call avg103010
    "[textdict[1222438]]":
        call avg103011
return