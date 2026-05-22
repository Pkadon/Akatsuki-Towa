label avg12576:

$ play_music("ED6200.ogg")
scene avg_bg_080
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
$ update_narrator('c43')
window show
with fade_in
c43 '[convertstrid(1155326)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro09.ogg"
c31 '[convertstrid(1155327)]'
hide p4
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1155328)]'
hide p3
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l_entrance(-17), light, flip], 6)
c291 '[convertstrid(1155329)]'
$ update_portrait('sc021_01 1', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 6', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1155330)]'
hide p2
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1155331)]'
hide p1
$ update_portrait('oc004_01 4', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1155332)]'
$ update_portrait('oc004_01 4', 'p4', [r(-5), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[convertstrid(1155333)]'
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[convertstrid(1155334)]'
$ update_portrait('sc021_01 1', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc004_01 17', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1155335)]'
$ update_portrait('oc004_01 17', 'p4', [r(-5), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[convertstrid(1155336)]'
hide p4
$ update_portrait('sc021_01 1', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc003_01 17', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1155337)]'
$ update_portrait('oc003_01 17', 'p3', [r(-6), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[convertstrid(1155338)]'
hide p3
$ update_portrait('sc021_01 1', 'p29', [l(-17), dark, flip], 5)
$ update_portrait('oc002_01 2', 'p2', [r(-3), r_shake, light], 6)
c23 '[convertstrid(1155339)]'
$ update_portrait('oc002_01 2', 'p2', [r(-3), dark], 5)
$ update_portrait('sc021_01 1', 'p29', [l(-17), light, flip], 6)
c291 '[convertstrid(1155340)]'
hide p29
hide p2
$ update_portrait('oc003_01 17', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
with fade
c31 '[convertstrid(1155341)]'
$ update_portrait('oc003_01 17', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 8', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1155342)]'
$ play_music("ED6523.ogg")
hide p3
hide p1
$ update_narrator('c12611')
with fade
c12611 '[convertstrid(1155343)]'
$ update_portrait('sc021_01 1', 'p29', [r(-17), light], 6)
c293 '[convertstrid(1155344)]'
$ update_portrait('sc021_01 1', 'p29', [r(-17), dark], 5)
c12611 '[convertstrid(1155345)]'
hide p29
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1155346)]'
hide p1
$ update_portrait('oc002_01 8', 'p2', [r(-3), light], 6)
c23 '[convertstrid(1155347)]'
$ update_portrait('oc002_01 8', 'p2', [r(-3), dark], 5)
$ update_portrait('sc021_01 4', 'p29', [l(-17), light, flip], 6)
c291 '[convertstrid(1155348)]'
return