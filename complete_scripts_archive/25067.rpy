label avg25067:
stop music

scene placeholderbackground
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
window show
with fade_in
c23 '[textdict[1210202]]'
hide p2
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 5)
play sfx2 "fight_6025.ogg"
c13 '[textdict[1210203]]'
hide p1
play sfx2 "fight_6028.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
c0 '[textdict[1210204]]'
$ update_portrait('oc002_01 21', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[textdict[1210205]]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210206]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1210207]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1210208]]'
return