label avg25305:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7080.ogg"
c0 '[textdict[1211175]]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_hurt_02.ogg"
c23 '[textdict[1211176]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1211177]]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_arts_03.ogg"
c23 '[textdict[1211178]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1211179]]'
return