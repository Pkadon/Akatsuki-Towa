label avg10065:

play music "ED6103.ogg"
scene avg_bg_037
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
c11 '[textdict[1005009]]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('sc015_01 1', 'p693', [r_entrance(9), light], 5)
c6933 '[textdict[1005010]]'
$ update_portrait('sc015_01 1', 'p693', [r(9), light], 5)
c6933 '[textdict[1005011]]'
$ update_portrait('sc015_01 1', 'p693', [r(9), dark], 5)
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1005012]]'
hide p1
$ update_portrait('sc007_01 2', 'p15', [l(-17), light, flip], 6)
c151 '[textdict[1005018]]'
hide p693
$ update_portrait('sc007_01 2', 'p15', [l(-17), dark, flip], 6)
$ update_portrait('sc015_01 1', 'p23', [r(9), light], 5)
c233 '[textdict[1005019]]'
$ update_portrait('sc015_01 1', 'p23', [r(9), dark], 5)
$ update_portrait('sc007_01 1', 'p15', [l(-17), light, flip], 6)
c151 '[textdict[1005020]]'
hide p15
hide p23
c0 '[textdict[1005021]]'
$ update_portrait('sc015_01 2', 'p23', [r(9), light], 5)
c233 '[textdict[1005022]]'
$ update_portrait('sc015_01 1', 'p23', [r(9), light], 5)
c233 '[textdict[1005023]]'
$ update_portrait('sc015_01 1', 'p23', [r(9), light], 5)
c233 '[textdict[1005024]]'
$ update_portrait('sc015_01 1', 'p23', [r(9), dark], 5)
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na02.ogg"
c11 '[textdict[1005025]]'
hide p23
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('sc007_01 1', 'p15', [r(-17), light], 5)
c153 '[textdict[1005026]]'
hide p1
$ update_portrait('sc007_01 1', 'p15', [r(-17), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1005036]]'
hide p15
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1005037]]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc039_01 1', 'p46', [l(-13), light, flip], 6)
c461 '[textdict[1005038]]'
hide p1
$ update_portrait('sc039_01 1', 'p46', [l(-13), dark, flip], 6)
$ update_portrait('sc015_01 1', 'p23', [r(9), light], 5)
c233 '[textdict[1005039]]'
return