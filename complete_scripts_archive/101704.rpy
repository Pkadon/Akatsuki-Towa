label avg101704:
stop music

scene placeholderbackground
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
window show
with fade_in
c171 '[textdict[1221883]]'
hide p17
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1221884]]'
hide p17
hide p1
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('sc009_01 1', 'p17', [l(-13), light, flip], 6)
c171 '[textdict[1221885]]'
hide p1
hide p17
$ update_portrait('sc009_01 1', 'p17', [l(-13), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
c13 '[textdict[1221886]]'
menu:
    extend ""
    "[textdict[1221887]]":
        call avg101705
    "[textdict[1221888]]":
        call avg101706
    "[textdict[1221889]]":
        call avg101707
return