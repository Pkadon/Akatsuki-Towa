label avg20103:
stop music

play music "ED6103.ogg"
scene avg_bg_037
window show
with fade_in
c6941 '[textdict[1005074]]'
c6953 '[textdict[1005075]]'
c6941 '[textdict[1005076]]'
c6953 '[textdict[1005077]]'
c6953 '[textdict[1005078]]'
c6941 '[textdict[1005079]]'
c6953 '[textdict[1005080]]'
c6941 '[textdict[1005081]]'
c6941 '[textdict[1005082]]'
$ update_portrait('oc002_01 4', 'p2', [l_entrance(-3), light, flip], 6)
c21 '[textdict[1005083]]'
hide p2
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1005084]]'
hide p2
hide p1
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c6951 '[textdict[1005085]]'
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1005086]]'
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c6941 '[textdict[1005087]]'
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c6941 '[textdict[1005088]]'
hide p1
$ update_portrait('sc007_01 5', 'p15', [r(-17), light], 5)
c153 '[textdict[1005089]]'
hide p15
$ update_portrait('sc007_01 5', 'p15', [r(-17), dark], 5)
c6941 '[textdict[1005090]]'
hide p15
$ update_portrait('sc007_01 5', 'p15', [r(-17), dark], 5)
c6951 '[textdict[1005096]]'
hide p15
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[textdict[1005097]]'
hide p1
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
c6951 '[textdict[1005098]]'
hide p1
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
c6941 '[textdict[1005099]]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 5)
c23 '[textdict[1005100]]'
hide p2
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1005101]]'
return