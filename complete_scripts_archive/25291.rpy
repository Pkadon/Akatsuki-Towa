label avg25291:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 3', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "fight_6024.ogg"
play sfxvoice "bcv_oc001_hurt_02.ogg"
c13 '[convertstrid(1211106)]'
hide p1
$ update_portrait('oc002_01 3', 'p2', [mid(-3), light], 6)
play sfxvoice "avg_vocal_ch22.ogg"
c23 '[convertstrid(1211107)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na03.ogg"
c13 '[convertstrid(1211108)]'
return