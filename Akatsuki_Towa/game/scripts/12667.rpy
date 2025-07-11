label avg12667:

play music "ed7150.ogg"
scene avg_bg_015
window show
with fade_in
c0 '[textdict[1166645]]'
$ update_portrait('oc002_01 23', 'p2', [r(-3), light], 5)
c23 '[textdict[1166646]]'
$ update_portrait('oc002_01 23', 'p2', [r(-3), dark], 5)
$ update_portrait('oc004_01 17', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1166647]]'
$ update_portrait('oc004_01 1', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1166648]]'
hide p2
$ update_portrait('oc004_01 1', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
play sfx2 "fight_6021.ogg"
c13 '[textdict[1166649]]'
play music "ed7511.ogg"
$ update_portrait('oc001_01 9', 'p1', [r_midback(-2), light], 5)
play sfx2 "other_7087.ogg"
c13 '[textdict[1166650]]' (what_size=(gui.text_size*1.2))
hide p4
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
play sfx2 "other_7007.ogg"
c13671 '[textdict[1166651]]' with shake
hide p1
play sfx2 "fight_6022.ogg"
c0 '[textdict[1166652]]'
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 5)
c13 '[textdict[1166653]]'
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
c13671 '[textdict[1166654]]'
hide p1
c0 '[textdict[1166655]]'
$ update_portrait('oc004_01 4', 'p4', [l(-5), light, flip], 6)
c41 '[textdict[1166656]]'
$ update_portrait('oc004_01 4', 'p4', [l(-5), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
play sfx2 "fight_6024.ogg"
c13 '[textdict[1166657]]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
c13661 '[textdict[1166658]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 5)
c23 '[textdict[1166659]]'
return