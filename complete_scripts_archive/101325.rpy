label avg101325:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 17', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1221024]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1221025]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 2', 'p13', [l(-17), light, flip], 6)
c131 '[textdict[1221026]]'
$ update_portrait('sc005_01 5', 'p13', [l(-17), light, flip], 6)
c131 '[textdict[1221027]]'
menu:
    extend ""
    "[textdict[1221028]]":
        call avg101326
    "[textdict[1221029]]":
        call avg101327
    "[textdict[1221030]]":
        call avg101328
return