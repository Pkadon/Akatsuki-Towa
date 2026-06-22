label avg24093:

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
get_char('c11') '[convertstrid(1200333)]' (**arg(1, 1200333))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c7603') '[convertstrid(1200334)]' (**arg(2, 1200334))
$ update_portrait('oc001_01 5', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1200335)]' (**arg(3, 1200335))
return