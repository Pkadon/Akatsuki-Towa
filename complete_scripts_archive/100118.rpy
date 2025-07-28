label avg100118:

stop music
scene placeholderbackground
$ update_portrait('sc001_01 5', 'p9', [mid(-11), light], 6)
$ update_narrator('c93')
window show
with fade_in
c93 '[convertstrid(1218054)]'
$ update_portrait('sc001_01 6', 'p9', [mid(-11), light], 6)
c93 '[convertstrid(1218055)]'
hide p9
$ update_portrait('oc001_01 12', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc002_c05_01.ogg"
c13 '[convertstrid(1218056)]'
hide p1
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 6)
c93 '[convertstrid(1218057)]'
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 6)
c93 '[convertstrid(1218058)]'
hide p9
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
c13 '[convertstrid(1218059)]'
return