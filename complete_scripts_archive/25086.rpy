label avg25086:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 5', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1210249)]'
hide p2
$ update_portrait('oc001_01 22', 'p1', [mid(-2), light], 6)
play sfxvoice "avg_vocal_na17.ogg"
c13 '[convertstrid(1210250)]'
return