label avg10536:

play music "ED6105.ogg"
scene avg_bg_102
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
$ update_narrator('c41')
window show
with fade_in
c41 '[textdict[1152560]]'
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 18', 'p2', [r(-3), light], 5)
c23 '[textdict[1152561]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[1152562]]'
hide p4
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
play sfx2 "other_7085.ogg"
c12381 '[textdict[1152563]]'
hide p2
$ update_portrait('sc021_01 4', 'p29', [r(-17), light], 5)
c293 '[textdict[1152564]]'
$ update_portrait('sc021_01 4', 'p29', [r(-17), dark], 5)
c12381 '[textdict[1152565]]'
hide p29
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1152566]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c12381 '[textdict[1152567]]'
hide p1
$ update_portrait('sc021_01 4', 'p29', [r(-17), light], 5)
c293 '[textdict[1152568]]'
$ update_portrait('sc021_01 4', 'p29', [r(-17), dark], 5)
c12381 '[textdict[1152569]]'
hide p29
$ update_portrait('oc003_01 4', 'p3', [r(-6), light], 5)
c33 '[textdict[1152570]]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1152571]]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
c291 '[textdict[1152572]]'
return