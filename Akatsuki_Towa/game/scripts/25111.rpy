label avg25111:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfx2 "elc_5002.ogg"
play sfxvoice "bcv_oc002_hurt_01.ogg"
c23 '[textdict[1210329]]'
hide p2
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210330]]'
hide p1
$ update_portrait('oc002_01 7', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch31.ogg"
c23 '[textdict[1210331]]'
return