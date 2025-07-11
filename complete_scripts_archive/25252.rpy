label avg25252:

scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_na04.ogg"
c13 '[textdict[1210927]]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
c23 '[textdict[1210928]]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[textdict[1210929]]'
hide p1
play sfx2 "fight_6003.ogg"
c20193 '[textdict[1210930]]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfx2 "other_7080.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1210931]]'
return