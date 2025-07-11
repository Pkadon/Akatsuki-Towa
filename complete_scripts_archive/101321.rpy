label avg101321:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1221012]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1221013]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 1', 'p13', [l(-17), light, flip], 6)
c131 '[textdict[1221014]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc005_01 2', 'p13', [l(-17), light, flip], 6)
c131 '[textdict[1221015]]'
$ update_portrait('sc005_01 2', 'p13', [l(-17), dark, flip], 6)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
c13 '[textdict[1221016]]'
menu:
    extend ""
    "[textdict[1221017]]":
        call avg101322
    "[textdict[1221018]]":
        call avg101323
    "[textdict[1221019]]":
        call avg101324
return