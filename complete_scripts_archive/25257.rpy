label avg25257:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 13', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "other_7086.ogg"
play sfxvoice "avg_vocal_ch05.ogg"
c23 '[textdict[1210953]]'
hide p2
c20093 '[textdict[1210954]]'
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[textdict[1210955]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch19.ogg"
c23 '[textdict[1210956]]'
hide p2
c20093 '[textdict[1210957]]'
return