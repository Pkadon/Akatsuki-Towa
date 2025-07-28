label avg12174:

play music "ed7105.ogg"
scene avg_bg_028
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
c13 '[convertstrid(1128560)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
c9651 '[convertstrid(1128561)]'
c9651 '[convertstrid(1128562)]'
c9651 '[convertstrid(1128563)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c21 '[convertstrid(1128564)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1128565)]'
$ update_portrait('oc001_01 8', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1128567)]'
return