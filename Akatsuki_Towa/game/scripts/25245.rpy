label avg25245:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 2', 'p1', [mid(-2), light], 5)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1210887)]'
hide p1
$ update_portrait('oc002_01 6', 'p2', [mid(-3), light], 5)
play sfx2 "fight_6025.ogg"
c23 '[convertstrid(1210888)]'
hide p2
$ update_portrait('oc001_01 11', 'p1', [mid(-2), light], 5)
play sfxvoice "avg_vocal_na17.ogg"
c13 '[convertstrid(1210889)]'
return