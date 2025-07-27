label avg20038:

play music "ed7104.ogg"
scene placeholderbackground
$ update_narrator('c5693')
window show
with fade_in
c5693 '[convertstrid(1002313)]'
c5693 '[convertstrid(1002314)]'
c5693 '[convertstrid(1002315)]'
$ update_portrait('oc002_01 10', 'p2', [mid(-3), light], 5)
play sfxvoice "avg_vocal_ch25.ogg"
c23 '[convertstrid(1002316)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1002317)]'
return