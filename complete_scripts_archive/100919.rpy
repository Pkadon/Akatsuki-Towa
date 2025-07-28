label avg100919:

stop music
scene placeholderbackground
$ update_portrait('sc001_01 4', 'p9', [mid(-11), light], 6)
$ update_narrator('c93')
window show
with fade_in
c93 '[convertstrid(1218061)]'
hide p9
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc002_get_02.ogg"
c13 '[convertstrid(1218062)]'
hide p1
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 6)
c93 '[convertstrid(1218063)]'
hide p9
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "bcv_oc002_atk_01.ogg"
c13 '[convertstrid(1218064)]'
hide p1
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 6)
c93 '[convertstrid(1218065)]'
hide p9
c0 '[convertstrid(1218066)]'
return