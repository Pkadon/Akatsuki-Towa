label avg24085:

$ play_music("ed7105.ogg")
scene placeholderbackground
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
c11 '[convertstrid(1200314)]'
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('st044_01 1', 'p243', [r(10), light], 6)
c2433 '[convertstrid(1200315)]'
$ update_portrait('st044_01 1', 'p243', [r(10), dark], 5)
$ update_portrait('oc001_01 11', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1200316)]'
return