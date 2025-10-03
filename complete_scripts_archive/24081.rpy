label avg24081:

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [mid(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1200104)]'
hide p1
c9573 '[convertstrid(1200105)]'
$ update_portrait('oc001_01 10', 'p1', [mid(-2), light], 6)
c13 '[convertstrid(1200106)]'
return