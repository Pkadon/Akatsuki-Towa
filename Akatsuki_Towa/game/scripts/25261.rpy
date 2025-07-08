label avg25261:
stop music

scene placeholderbackground
$ update_portrait('oc001_01 19', 'p1', [mid(-2), light], 5)
window show
with fade_in
play sfx2 "fight_6020.ogg"
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[textdict[1210974]]'
hide p1
$ update_portrait('oc002_01 11', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch23.ogg"
c23 '[textdict[1210975]]'
return