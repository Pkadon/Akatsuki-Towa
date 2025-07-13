label avg25119:

stop music
scene placeholderbackground
$ update_narrator('c6123')
window show
with fade_in
play sfx2 "fight_6030.ogg"
c6123 '[textdict[1210349]]'
$ update_portrait('oc002_01 9', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_arts_03.ogg"
c23 '[textdict[1210350]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210351]]'
return