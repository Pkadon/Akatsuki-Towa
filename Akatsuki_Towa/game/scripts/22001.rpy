label avg22001:

play music "ed7151.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1002428)]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1007062)]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1007063)]'
hide p1
$ update_portrait('oc002_01 4', 'p2', [mid(-3), light], 6)
c23 '[convertstrid(1007064)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [mid(-2), light], 6)
play sfx2 "fight_6024.ogg"
c13 '[convertstrid(1006446)]'
return