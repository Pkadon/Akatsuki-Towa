label avg1024:

play music "ed7113.ogg"
scene avg_bg_024
$ update_narrator('c23')
window show
with fade_in
$ update_portrait('oc002_01 5', 'p2', [r_entrance(-3), light], 5)
c23 '[textdict[2100462]]'
$ update_portrait('oc002_01 5', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[textdict[2100463]]'
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 6)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 5)
c23 '[textdict[2100464]]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[textdict[2100465]]'
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 6)
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 5)
c23 '[textdict[2100466]]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[textdict[2100467]]'
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 6)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 5)
c23 '[textdict[2100468]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[2100469]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 5)
c13 '[textdict[2100470]]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[textdict[2100471]]'
hide p1
$ update_portrait('sc015_01 1', 'p23', [l(9), dark, flip], 6)
$ update_portrait('oc002_01 14', 'p2', [r(-3), r_shake, light], 5)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[textdict[2100472]]'
$ update_portrait('oc002_01 14', 'p2', [r(-3), dark], 5)
$ update_portrait('sc015_01 1', 'p23', [l(9), light, flip], 6)
c231 '[textdict[2100473]]'
return