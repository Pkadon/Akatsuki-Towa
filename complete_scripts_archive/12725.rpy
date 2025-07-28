label avg12725:

play music "ED6301.ogg"
scene avg_bg_070
$ update_portrait('st061_01 4', 'p1304', [l(-2), light, flip], 6)
$ update_narrator('c13041')
window show
with fade_in
c13041 '[convertstrid(1171768)]'
$ update_portrait('st061_01 4', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1171769)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('st061_01 1', 'p1304', [l(-2), light, flip], 6)
c13041 '[convertstrid(1171770)]'
$ update_portrait('st061_01 1', 'p1304', [l(-2), dark, flip], 5)
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1171771)]'
return