label avg12615:
stop music

play music "ed7105.ogg"
scene avg_bg_010
window show
with fade_in
$ update_portrait('oc002_01 8', 'p2', [l_entrance(-3), light, flip], 6)
c21 '[textdict[1161595]]'
hide p2
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc003_01 13', 'p3', [r(-6), light], 5)
c33 '[textdict[1161596]]'
hide p2
hide p3
$ update_portrait('oc003_01 13', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1161597]]'
hide p3
hide p4
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc002_01 15', 'p2', [r(-3), light], 5)
c23 '[textdict[1161598]]'
hide p2
hide p4
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r_entrance(-2), light], 5)
c13 '[textdict[1161599]]'
hide p1
hide p4
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1161600]]'
hide p4
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 1', 'p2', [l_exit(-3), light, flip], 6)
play sfx2 "other_7085.ogg"
c21 '[textdict[1161601]]'
hide p2
hide p1
$ update_portrait('oc003_01 13', 'p3', [r(-6), light], 5)
c33 '[textdict[1161602]]'
hide p3
$ update_portrait('oc003_01 13', 'p3', [r(-6), dark], 5)
$ update_portrait('oc004_01 12', 'p4', [l_entrance(-5), light, flip], 6)
c41 '[textdict[1161603]]'
hide p3
hide p4
$ update_portrait('oc004_01 12', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 16', 'p1', [r(-2), light], 5)
c13 '[textdict[1161604]]'
hide p4
hide p1
$ update_portrait('oc001_01 16', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
c31 '[textdict[1161605]]'
hide p1
hide p3
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 6)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 5)
c13 '[textdict[1161606]]'
hide p3
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1161607]]'
hide p4
hide p1
$ update_portrait('oc001_01 1', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1161608]]'
hide p1
hide p4
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 5)
c33 '[textdict[1161609]]'
play music "ed7511.ogg"
hide p4
hide p3
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 3', 'p2', [l_entrance(-3), light, flip], 6)
c21 '[textdict[1161610]]' with shake
hide p3
hide p2
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 12', 'p1', [r(-2), light], 5)
play sfx2 "other_7080.ogg"
c13 '[textdict[1161611]]'
hide p2
hide p1
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1161612]]'
hide p2
hide p1
$ update_portrait('oc001_01 12', 'p1', [r(-2), dark], 5)
$ update_portrait('oc004_01 16', 'p4', [l(-5), light, flip], 6)
play sfx2 "other_7093.ogg"
c41 '[textdict[1161613]]'
hide p1
hide p4
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 5)
play sfx2 "fight_6024.ogg"
c13 '[textdict[1161614]]'
return