label avg20049:

play music "ED6505.ogg"
scene avg_bg_027
$ update_narrator('c5963')
window show
with fade_in
c5963 '[convertstrid(1002767)]'
c5963 '[convertstrid(1002768)]'
c5963 '[convertstrid(1002769)]'
c5963 '[convertstrid(1002770)]'
c5971 '[convertstrid(1002771)]'
c5971 '[convertstrid(1002772)]'
c5981 '[convertstrid(1002773)]'
c5963 '[convertstrid(1002774)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch08.ogg"
c21 '[convertstrid(1002775)]'
$ update_portrait('oc002_01 6', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1002776)]'
return