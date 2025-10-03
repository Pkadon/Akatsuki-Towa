label avg12141:

$ play_music("ED6104.ogg")
scene avg_bg_023
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
$ update_narrator('c23')
window show
with fade_in
play sfxvoice "avg_vocal_ch12.ogg"
c23 '[convertstrid(1128284)]'
hide p2
$ update_portrait('oc004_01 2', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1128289)]'
$ update_portrait('oc004_01 2', 'p4', [r(-5), dark], 5)
$ update_portrait('st009_01 1', 'p561', [l(-22), light, flip], 6)
c5611 '[convertstrid(1128290)]'
$ update_portrait('st009_01 4', 'p561', [l(-22), light, flip], 6)
c5611 '[convertstrid(1128291)]'
$ update_portrait('st009_01 1', 'p561', [l(-22), light, flip], 6)
c5611 '[convertstrid(1128292)]'
$ update_portrait('st009_01 4', 'p561', [l(-22), light, flip], 6)
c5611 '[convertstrid(1128293)]'
hide p4
$ update_portrait('st009_01 4', 'p561', [l(-22), dark, flip], 5)
$ update_portrait('oc003_01 2', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1128294)]'
$ update_portrait('oc003_01 14', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1128295)]'
hide p561
$ update_portrait('oc003_01 14', 'p3', [r(-6), dark], 5)
$ update_portrait('oc001_01 4', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1128296)]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc004_01 1', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1128297)]'
hide p1
$ update_portrait('oc004_01 1', 'p4', [r(-5), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), light, flip], 6)
play sfx2 "common_quest.ogg"
c21 '[convertstrid(1128298)]'
return