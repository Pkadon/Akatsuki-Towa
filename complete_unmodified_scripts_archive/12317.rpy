label avg12317:

$ play_music("ed7302.ogg")
scene avg_bg_052
$ update_narrator('c5631')
window show
with fade_in
play sfx2 "other_7087.ogg"
c5631 '[convertstrid(1133300)]'
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1133301)]'
hide p1
$ update_portrait('oc002_01 12', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1133302)]'
hide p2
$ update_portrait('oc001_01 20', 'p1', [r(-2), r_shake, light], 6)
c13 '[convertstrid(1133303)]'
$ update_portrait('oc001_01 20', 'p1', [r(-2), dark], 5)
c5631 '[convertstrid(1133304)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1133305)]'
hide p1
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro13.ogg"
c33 '[convertstrid(1133306)]'
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
c5631 '[convertstrid(1133307)]'
c5631 '[convertstrid(1133308)]'
c5631 '[convertstrid(1133309)]'
c5631 '[convertstrid(1133310)]'
$ update_portrait('oc003_01 21', 'p3', [r(-6), r_shake, light], 6)
play sfxvoice "avg_vocal_ro16.ogg"
c33 '[convertstrid(1133311)]'
hide p3
$ update_portrait('oc002_01 9', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1133312)]'
hide p2
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
play sfxvoice "avg_vocal_na05.ogg"
c13 '[convertstrid(1133313)]'
hide p1
$ update_portrait('oc002_01 7', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1133314)]'
$ update_portrait('oc002_01 7', 'p2', [r(-3), dark], 5)
c5631 '[convertstrid(1133315)]'
c5631 '[convertstrid(1133316)]'
hide p2
$ update_portrait('sc050_01 4', 'p57', [r(-19), light], 6)
c573 '[convertstrid(1133317)]'
hide p57
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1133318)]'
$ update_portrait('oc001_01 2', 'p1', [r(-2), light], 6)
play sfx2 "common_tag_2.ogg"
c13 '[convertstrid(1133319)]'
$ play_music("ed7511.ogg")
$ update_portrait('oc001_01 2', 'p1', [r(-2), dark], 5)
play sfx2 "other_7079.ogg"
c10871 '[convertstrid(1133320)]' with shake
hide p1
$ update_portrait('oc003_01 12', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro09.ogg"
c33 '[convertstrid(1133321)]'
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
c5631 '[convertstrid(1133322)]'
$ update_portrait('oc003_01 9', 'p3', [r(-6), r_shake, light], 6)
play sfx2 "other_7080.ogg"
c33 '[convertstrid(1133323)]'
$ update_portrait('oc003_01 9', 'p3', [r(-6), dark], 5)
$ update_portrait('sc051_01 4', 'p58', [l(-32), light, flip], 6)
c581 '[convertstrid(1133324)]'
return