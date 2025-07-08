label avg101508:
stop music

scene placeholderbackground
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
window show
with fade_in
c151 '[textdict[1221281]]'
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1221282]]'
hide p15
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 5', 'p15', [l(-17), light, flip], 6)
c151 '[textdict[1221283]]'
hide p1
$ update_portrait('sc007_01 5', 'p15', [l(-17), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1221284]]'
menu:
    extend ""
    "[textdict[1221285]]":
        call avg101509
    "[textdict[1221286]]":
        call avg101510
    "[textdict[1221287]]":
        call avg101511
return