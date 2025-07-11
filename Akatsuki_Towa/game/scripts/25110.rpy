label avg25110:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "elc_5006.ogg"
play sfxvoice "bcv_oc001_hurt_01.ogg"
c13 '[textdict[1210326]]'
hide p1
$ update_portrait('oc002_01 14', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch06.ogg"
c23 '[textdict[1210327]]'
hide p2
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na02.ogg"
c13 '[textdict[1210328]]'
return