label avg20105:
stop music

play music "ED6103.ogg"
scene avg_bg_038
window show
with fade_in
$ update_portrait('oc002_01 2', 'p2', [l_entrance(-3), light, flip], 6)
play sfx2 "other_7047.ogg"
c21 '[textdict[1005102]]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
play sfx2 "other_7064.ogg"
c13 '[textdict[1005103]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c6961 '[textdict[1005104]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1005105]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c6961 '[textdict[1005106]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1005107]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c6971 '[textdict[1005108]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c6961 '[textdict[1005109]]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
c6961 '[textdict[1005110]]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[1005111]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
c6981 '[textdict[1005112]]'
hide p2
$ update_portrait('sc039_01 2', 'p46', [r(-13), r_shake, light], 5)
c463 '[textdict[1005113]]'
$ update_portrait('sc039_01 2', 'p46', [r(-13), dark], 5)
c6961 '[textdict[1005114]]'
hide p46
$ update_portrait('oc001_01 12', 'p1', [r_midback(-2), light], 5)
c13 '[textdict[1005115]]'
hide p1
c6973 '[textdict[1005116]]'
c6961 '[textdict[1005117]]'
c6961 '[textdict[1005118]]'
c6983 '[textdict[1005119]]'
$ update_portrait('sc039_01 4', 'p46', [r(-13), light], 5)
c463 '[textdict[1005120]]'
$ update_portrait('sc039_01 4', 'p46', [r(-13), dark], 5)
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1005121]]'
hide p46
$ update_portrait('oc001_01 8', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 10', 'p2', [r(-3), light], 5)
c23 '[textdict[1005122]]'
hide p1
hide p2
c0 '[textdict[1005123]]'
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1005124]]'
return