label avg25314:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 16', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7027.ogg"
play sfxvoice "avg_vocal_na03.ogg"
c13 '[convertstrid(1211206)]'
hide p1
c20153 '[convertstrid(1211207)]'
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1211208)]'
hide p1
$ update_portrait('oc002_01 1', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1211209)]'
return