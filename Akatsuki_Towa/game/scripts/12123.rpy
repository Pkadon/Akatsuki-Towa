label avg12123:

play music "ED6104.ogg"
scene avg_bg_038
$ update_portrait('oc001_01 1', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "common_select.ogg"
c13 '[convertstrid(1128233)]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1128234)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
c9591 '[convertstrid(1128235)]'
hide p2
$ update_portrait('oc001_01 10', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na20.ogg"
c13 '[convertstrid(1128236)]'
$ update_portrait('oc001_01 10', 'p1', [r(-2), dark], 5)
c9591 '[convertstrid(1128237)]'
c9591 '[convertstrid(1128238)]'
c9591 '[convertstrid(1128239)]'
c9591 '[convertstrid(1128240)]'
c9591 '[convertstrid(1128241)]'
hide p1
play sfx2 "common_tag_2.ogg"
c0 '[convertstrid(1128242)]'
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1128243)]'
$ update_portrait('oc003_01 2', 'p3', [r(-6), dark], 5)
c9591 '[convertstrid(1128244)]'
c9591 '[convertstrid(1128245)]'
play sfx2 "common_quest.ogg"
c9591 '[convertstrid(1128246)]'
return