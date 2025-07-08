label avg101525:
stop music

scene placeholderbackground
$ update_portrait('sc007_01 6', 'p15', [l(-17), light, flip], 6)
window show
with fade_in
c151 '[textdict[1221331]]'
hide p15
$ update_portrait('sc007_01 6', 'p15', [l(-17), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1221332]]'
hide p15
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
c151 '[textdict[1221333]]'
hide p1
hide p15
$ update_portrait('sc007_01 1', 'p15', [l(-17), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1221334]]'
menu:
    extend ""
    "[textdict[1221335]]":
        call avg101526
    "[textdict[1221336]]":
        call avg101527
    "[textdict[1221337]]":
        call avg101528
return