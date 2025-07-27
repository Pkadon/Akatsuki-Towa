label avg29100:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na19.ogg"
c13 '[convertstrid(1218002)]'
hide p1
$ update_portrait('sc001_01 6', 'p9', [mid(-11), light], 5)
c93 '[convertstrid(1218003)]'
$ update_portrait('sc001_01 2', 'p9', [mid(-11), light], 5)
c93 '[convertstrid(1218004)]'
$ update_portrait('sc001_01 1', 'p9', [mid(-11), light], 5)
c93 '[convertstrid(1218005)]'
hide p9
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na15.ogg"
c13 '[convertstrid(1218006)]'
return