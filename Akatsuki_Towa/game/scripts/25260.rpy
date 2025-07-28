label avg25260:

stop music
scene placeholderbackground
$ update_portrait('oc002_01 2', 'p2', [mid(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
c23 '[convertstrid(1210972)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6025.ogg"
c13 '[convertstrid(1210973)]'
return