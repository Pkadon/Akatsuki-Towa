label avg12187:

play music "ED6200.ogg"
scene avg_bg_027
$ update_portrait('oc002_01 1', 'p2', [l(-3), light, flip], 6)
window show
with fade_in
c21 '[textdict[1120700]]'
$ update_portrait('oc002_01 1', 'p2', [l(-3), dark, flip], 6)
c9803 '[textdict[1120701]]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
c11 '[textdict[1120702]]'
hide p1
$ update_portrait('oc002_01 13', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch05.ogg"
c21 '[textdict[1120703]]'
$ update_portrait('oc002_01 13', 'p2', [l(-3), dark, flip], 6)
c9803 '[textdict[1120704]]'
$ update_portrait('oc002_01 13', 'p2', [l(-3), dark, flip], 6)
c9803 '[textdict[1120705]]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na21.ogg"
c11 '[textdict[1120706]]'
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 6)
c9803 '[textdict[1120707]]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c21 '[textdict[1120708]]'
return