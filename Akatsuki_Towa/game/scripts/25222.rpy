label avg25222:

stop music
scene placeholderbackground
window show
with fade_in
play sfx2 "other_7079.ogg"
c20183 '[textdict[1210772]]'
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1210773]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfx2 "fight_6003.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1210774]]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na21.ogg"
c13 '[textdict[1210775]]'
hide p1
play sfx2 "other_7031.ogg"
c20183 '[textdict[1210776]]'
play sfx2 "other_7080.ogg"
c20163 '[textdict[1210777]]'
play sfx2 "other_7079.ogg"
c20183 '[textdict[1210778]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[textdict[1210779]]'
return