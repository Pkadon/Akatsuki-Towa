label avg25164:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
$ update_narrator('c23')
window show
with fade_in
play sfx2 "fight_6019.ogg"
play sfxvoice "bcv_oc002_atk_01.ogg"
c23 '[textdict[1210537]]'
hide p2
$ update_portrait('oc001_01 20', 'p1', [mid(-2), light], 5)
play sfxvoice "bcv_oc001_com_01.ogg"
c13 '[textdict[1210538]]'
return