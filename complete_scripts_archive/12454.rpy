label avg12454:

play music "ed7515.ogg"
scene avg_bg_036
$ update_narrator('c0')
window show
with fade_in
c0 '[convertstrid(1143545)]'
c0 '[convertstrid(1143546)]'
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 5)
c43 '[convertstrid(1143547)]'
hide p4
play sfx2 "other_7088.ogg"
c0 '[convertstrid(1143548)]'
stop music
$ update_portrait('oc004_01 12', 'p4', [r(-5), r_shake, light], 5)
c43 '[convertstrid(1143549)]'
$ update_portrait('oc004_01 12', 'p4', [r(-5), dark], 5)
play sfx2 "other_7080.ogg"
c10531 '[convertstrid(1143550)]'
play music "ed7511.ogg"
hide p4
c0 '[convertstrid(1143551)]'
$ update_portrait('oc004_01 16', 'p4', [r(-5), light], 5)
c43 '[convertstrid(1143552)]'
return