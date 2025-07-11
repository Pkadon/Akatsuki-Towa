label avg25194:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 6', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "fight_6025.ogg"
c13 '[textdict[1210652]]'
hide p1
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[textdict[1210653]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1210654]]'
return