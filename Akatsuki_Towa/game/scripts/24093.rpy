label avg24093:

play music "ed7105.ogg"
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
c11 '[convertstrid(1200333)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 6)
c7603 '[convertstrid(1200334)]'
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1200335)]'
return