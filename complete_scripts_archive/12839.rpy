label avg12839:

play music "ED6301.ogg"
scene avg_bg_218
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with fade_in
c31 '[textdict[1186141]]'
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 5)
c23 '[textdict[1186142]]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1186143]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 5', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1186144]]'
hide p1
$ update_portrait('oc003_01 5', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1186145]]'
$ update_portrait('oc002_01 17', 'p2', [r(-3), light], 5)
c23 '[textdict[1186146]]'
$ update_portrait('oc002_01 17', 'p2', [r(-3), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1186147]]'
$ update_portrait('oc003_01 16', 'p3', [l(-6), light, flip], 6)
c31 '[textdict[1186148]]'
hide p2
$ update_portrait('oc003_01 16', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('st061_01 1', 'p1304', [r(-2), light], 5)
c13043 '[textdict[1186149]]'
hide p1304
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 5)
c23 '[textdict[1186150]]'
hide p3
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), r_shake, light, flip], 6)
c11 '[textdict[1186151]]'
hide p1
play sfx2 "other_7080.ogg"
c5001 '[textdict[1186152]]' with shake
$ update_portrait('oc003_01 1', 'p3', [l(-6), light, flip], 6)
play sfx2 "fight_6025.ogg"
c31 '[textdict[1186153]]'
hide p2
$ update_portrait('oc003_01 1', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 20', 'p1', [r(-2), r_shake, light], 5)
play sfx2 "fight_6024.ogg"
c13 '[textdict[1186154]]'
hide p3
hide p1
play sfx2 "fight_6009.ogg"
c0 '[textdict[1186155]]'
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 5)
c23 '[textdict[1186156]]'
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[textdict[1186157]]'
hide p2
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1186158]]'
return