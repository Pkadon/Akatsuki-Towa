label avg25152:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7086.ogg"
play sfxvoice "avg_vocal_na15.ogg"
c13 '[convertstrid(1210481)]'
hide p1
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1210482)]'
return