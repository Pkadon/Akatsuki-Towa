label avg22142:

stop music
scene placeholderbackground
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
$ update_narrator('c11')
window show
with fade_in
c11 '[convertstrid(1128299)]'
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1128300)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('oc001_01 18', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1128301)]'
hide p2
$ update_portrait('oc001_01 18', 'p1', [l(-2), dark, flip], 5)
c5003 '[convertstrid(1128302)]' with shake
play music "ed7511.ogg"
$ update_portrait('oc001_01 9', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1128303)]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
play sfx2 "other_7080.ogg"
c21 '[convertstrid(1128304)]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1128305)]'
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc007_01 2', 'p7', [r(-24), light], 6)
play sfxvoice "avg_vocal_ar11.ogg"
c73 '[convertstrid(1128306)]' (what_size=(gui.text_size*1.2)) with shake
$ update_portrait('oc007_01 3', 'p7', [r(-24), r_shake, light], 6)
c73 '[convertstrid(1128307)]'
$ update_portrait('oc007_01 3', 'p7', [r(-24), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1128308)]'
hide p2
$ update_portrait('oc001_01 20', 'p1', [l(-2), light, flip], 6)
play sfx2 "fight_6024.ogg"
c11 '[convertstrid(1128309)]'
return