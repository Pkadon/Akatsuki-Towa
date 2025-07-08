label avg10136:
stop music

play music "ED6505.ogg"
scene avg_bg_027
window show
with fade_in
c0 '[textdict[1007379]]'
$ update_portrait('oc002_01 6', 'p2', [l_entrance(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c21 '[textdict[1007380]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1007381]]'
hide p1
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('uc004_02 5', 'p570', [r_entrance(-9), light], 5)
play sfx2 "other_7021.ogg"
c5703 '[textdict[1007382]]'
hide p1
hide p570
$ update_portrait('uc004_02 5', 'p570', [r(-9), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
c21 '[textdict[1007383]]'
hide p570
hide p2
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 6)
$ update_portrait('uc004_02 2', 'p961', [r(-9), light], 5)
c9613 '[textdict[1007384]]'
hide p2
hide p961
$ update_portrait('uc004_02 2', 'p961', [r(-9), dark], 5)
$ update_portrait('oc001_01 22', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1007385]]'
hide p961
hide p1
$ update_portrait('oc001_01 22', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('uc004_02 1', 'p961', [r(-9), light], 5)
c9613 '[textdict[1007386]]'
hide p1
hide p961
$ update_portrait('uc004_02 1', 'p961', [r(-9), dark], 5)
$ update_portrait('oc001_01 23', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1007387]]'
hide p961
hide p1
$ update_portrait('oc001_01 23', 'p1', [l(-2), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[1007682]]'
hide p1
hide p2
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 10', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1007683]]'
return