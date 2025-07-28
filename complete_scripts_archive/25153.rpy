label avg25153:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "fight_6022.ogg"
play sfxvoice "avg_vocal_na03.ogg"
c13 '[convertstrid(1210483)]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1210484)]'
hide p2
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1210485)]'
return