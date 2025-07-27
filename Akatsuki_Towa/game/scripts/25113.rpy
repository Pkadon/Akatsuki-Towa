label avg25113:

stop music
scene placeholderbackground
$ update_narrator('c0')
window show
with fade_in
play sfx2 "common_tag_2.ogg"
c0 '[convertstrid(1210338)]'
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "bcv_oc002_hurt_02.ogg"
c23 '[convertstrid(1210339)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 5)
c13 '[convertstrid(1210340)]'
return