label avg25036:

scene placeholderbackground
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
window show
with fade_in
play sfx2 "other_7080.ogg"
play sfxvoice "bcv_oc002_hurt_02.ogg"
c23 '[textdict[1210093]]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[textdict[1210094]]'
return