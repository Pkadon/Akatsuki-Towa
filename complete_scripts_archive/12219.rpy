label avg12219:

play music "ed7569.ogg"
scene avg_bg_010
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7018.ogg"
c0 '[textdict[1121486]]'
$ update_portrait('oc002_01 6', 'p2', [r_entrance(-3), light], 5)
c23 '[textdict[1120938]]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1120939]]'
hide p1
hide p2
$ update_portrait('uc004_02 1', 'p993', [r(-6), light], 5)
$ update_narrator('c9933')
with fade
c9933 '[textdict[1120940]]'
$ update_portrait('uc004_02 1', 'p993', [r(-6), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l_entrance(-5), light, flip], 6)
c41 '[textdict[1120941]]'
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('uc004_02 1', 'p993', [r(-6), light], 5)
c9933 '[textdict[1120942]]'
hide p4
$ update_portrait('uc004_02 1', 'p993', [r(-6), dark], 5)
$ update_portrait('sc039_01 5', 'p46', [l(-13), light, flip], 6)
c461 '[textdict[1120943]]'
$ update_portrait('sc039_01 8', 'p46', [l(-13), light, flip], 6)
c461 '[textdict[1120944]]'
$ update_portrait('sc039_01 8', 'p46', [l(-13), dark, flip], 6)
$ update_portrait('uc004_02 1', 'p993', [r(-6), light], 5)
c9933 '[textdict[1120945]]'
$ update_portrait('uc004_02 1', 'p993', [r(-6), dark], 5)
$ update_portrait('sc039_01 5', 'p46', [l(-13), light, flip], 6)
c461 '[textdict[1120946]]'
hide p993
$ update_portrait('sc039_01 5', 'p46', [l(-13), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1121570]]'
return