label avg10524:
stop music

play music "ED6100.ogg"
scene avg_bg_078
window show
with fade_in
c0 '[textdict[1152103]]'
c0 '[textdict[1152104]]'
c0 '[textdict[1152105]]'
c12301 '[textdict[1152106]]'
c12293 '[textdict[1152107]]' (what_size=(gui.text_size*1.2)) with shake
c12301 '[textdict[1152108]]'
$ update_portrait('oc004_01 4', 'p4', [r_entrance(-5), light], 5)
c43 '[textdict[1152109]]'
hide p4
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1152110]]'
hide p4
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
c12291 '[textdict[1152111]]'
hide p4
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1152112]]'
hide p4
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
c12301 '[textdict[1152113]]'
hide p4
$ update_portrait('oc004_01 11', 'p4', [r(-5), light], 5)
c43 '[textdict[1152114]]'
hide p4
$ update_portrait('oc004_01 11', 'p4', [r(-5), dark], 5)
c12311 '[textdict[1152115]]'
hide p4
c12293 '[textdict[1152116]]'
c12311 '[textdict[1152117]]'
c12293 '[textdict[1152118]]'
c12301 '[textdict[1152119]]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 5)
c43 '[textdict[1152120]]'
hide p4
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
c12301 '[textdict[1152121]]'
hide p4
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[1152122]]'
hide p4
hide p2
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1152123]]'
return