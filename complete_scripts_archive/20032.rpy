label avg20032:

play music "ed7104.ogg"
scene avg_bg_001
$ update_portrait('oc001_01 7', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
play sfxvoice "avg_vocal_na02.ogg"
c13 '[convertstrid(1002165)]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch11.ogg"
c23 '[convertstrid(1002166)]'
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 5)
c23 '[convertstrid(1002167)]'
return