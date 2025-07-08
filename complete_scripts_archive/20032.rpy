label avg20032:
stop music

play music "ed7104.ogg"
scene avg_bg_001
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1002165]]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1002166]]'
hide p2
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
c23 '[textdict[1002167]]'
return