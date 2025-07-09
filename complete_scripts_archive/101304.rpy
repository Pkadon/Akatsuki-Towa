label avg101304:
stop music

scene placeholderbackground
$ update_portrait('sc005_01 2', 'p13', [l(-17), light, flip], 6)
window show
with fade_in
c131 '[textdict[1220959]]'
$ update_portrait('sc005_01 2', 'p13', [l(-17), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
c13 '[textdict[1220960]]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
c131 '[textdict[1220961]]'
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
c131 '[textdict[1220962]]'
menu:
    extend ""
    "[textdict[1220963]]":
        call avg101305
    "[textdict[1220964]]":
        call avg101306
    "[textdict[1220965]]":
        call avg101307
return