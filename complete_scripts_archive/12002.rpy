label avg12002:
stop music

play music "ed7300.ogg"
scene placeholderbackground
$ update_portrait('oc002_01 3', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
$ update_portrait('oc002_01 3', 'p2', [l(-3), l_shake, light, flip], 6)
play sfx2 "fight_6019.ogg"
play sfxvoice "avg_vocal_ch15.ogg"
c21 '[textdict[1007066]]'
hide p2
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 5)
c13 '[textdict[1007067]]'
hide p1
hide p2
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 5)
c13 '[textdict[1007068]]'
hide p1
hide p2
$ update_portrait('oc002_01 3', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[textdict[1007069]]'
hide p2
hide p1
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 8', 'p2', [l(-3), l_shake, light, flip], 6)
play sfx2 "other_7092.ogg"
c21 '[textdict[1007070]]'
hide p1
hide p2
$ update_portrait('oc002_01 8', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 5)
c13 '[textdict[1007071]]'
hide p2
hide p1
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1007072]]'
hide p1
hide p2
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[1007073]]'
hide p2
hide p1
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1007074]]'
hide p1
hide p2
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('oc001_01 7', 'p1', [r(-2), r_shake, light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1007075]]'
return