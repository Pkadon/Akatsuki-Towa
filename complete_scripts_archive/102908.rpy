label avg102908:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
window show
with fade_in
c13 '[textdict[1219917]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[textdict[1219918]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[textdict[1219919]]'
menu:
    extend ""
    "[textdict[1219920]]":
        call avg102909
    "[textdict[1219921]]":
        call avg102910
    "[textdict[1219922]]":
        call avg102911
return