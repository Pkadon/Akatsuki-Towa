label avg25295:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7088.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
c13 '[textdict[1211125]]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_com_01.ogg"
c23 '[textdict[1211126]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
play sfx2 "elc_5002.ogg"
c13 '[textdict[1211127]]'
return