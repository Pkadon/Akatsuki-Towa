label avg10603:

play music "ED6102.ogg"
scene avg_bg_105
$ update_narrator('c0')
window show
with fade_in
c0 '[textdict[1160143]]'
c12321 '[textdict[1160144]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1160145]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
c12321 '[textdict[1160146]]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1160147]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
c12321 '[textdict[1160148]]'
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 5)
c23 '[textdict[1160149]]'
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
c12321 '[textdict[1160150]]'
$ update_portrait('oc002_01 6', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[1160151]]'
hide p2
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 5)
c43 '[textdict[1160152]]'
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l_entrance(-6), light, flip], 6)
c31 '[textdict[1160153]]'
hide p4
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 22', 'p1', [r(-2), light], 5)
c13 '[textdict[1160154]]'
hide p3
$ update_portrait('oc001_01 22', 'p1', [r(-2), dark], 5)
c12321 '[textdict[1160155]]'
return