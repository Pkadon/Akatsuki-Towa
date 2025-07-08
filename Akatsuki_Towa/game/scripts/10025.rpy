label avg10025:
stop music

play music "ED6505.ogg"
scene avg_bg_001
window show
with fade_in
play sfx2 "other_7018.ogg"
c0 '[textdict[1002140]]'
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
play sfxvoice "avg_vocal_li07.ogg"
c41 '[textdict[1002141]]'
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 5)
play sfxvoice "avg_vocal_ro10.ogg"
c33 '[textdict[1002142]]'
hide p3
$ update_portrait('oc004_01 9', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1002143]]'
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 9', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1002144]]'
hide p4
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 5', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1002145]]'
hide p1
$ update_portrait('oc004_01 5', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 1', 'p3', [r(-6), light], 5)
c33 '[textdict[1002146]]'
hide p4
$ update_portrait('oc003_01 1', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1002147]]'
hide p3
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1002148]]'
hide p4
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 1', 'p4', [l_exit(-5), light, flip], 6)
c41 '[textdict[1002149]]'
hide p4
hide p1
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 5)
c33 '[textdict[1002150]]'
hide p3
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1002151]]'
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 4', 'p5', [l_entrance(-6), light, flip], 6)
c51 '[textdict[1002152]]'
hide p1
$ update_portrait('oc005_01 4', 'p5', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1002153]]'
hide p5
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[1002154]]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1002155]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1002156]]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), light], 5)
c13 '[textdict[1002157]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 7', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[textdict[1002158]]'
hide p1
$ update_portrait('oc002_01 7', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 5)
c33 '[textdict[1002159]]'
hide p2
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1002160]]'
hide p3
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
c13 '[textdict[1002161]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc005_01 12', 'p5', [l(-6), light, flip], 6)
c51 '[textdict[1002162]]'
hide p1
$ update_portrait('oc005_01 12', 'p5', [l(-6), dark, flip], 6)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 5)
c33 '[textdict[1002163]]'
hide p5
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('oc005_01 8', 'p5', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ji16.ogg"
c51 '[textdict[1002164]]'
return