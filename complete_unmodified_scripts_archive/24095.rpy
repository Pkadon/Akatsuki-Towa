label avg24095:

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
c21 '[convertstrid(1200337)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
c50133 '[convertstrid(1200338)]'
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1200339)]'
return