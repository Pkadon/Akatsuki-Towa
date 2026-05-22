label avg12195:

$ play_music("ED6200.ogg")
scene avg_bg_027
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
$ update_narrator('c21')
window show
with fade_in
play sfxvoice "avg_vocal_ch10.ogg"
c21 '[convertstrid(1120785)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1120786)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1120787)]'
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
c21 '[convertstrid(1120788)]'
hide p2
hide p1
c0 '[convertstrid(1120789)]'
$ update_portrait('st017_01 5', 'p216', [r(-18), light], 6)
c2163 '[convertstrid(1120790)]'
$ update_portrait('st017_01 5', 'p216', [r(-18), dark], 5)
c9861 '[convertstrid(1120791)]'
hide p216
$ update_portrait('st018_01 4', 'p217', [r(-16), light], 6)
c2173 '[convertstrid(1120792)]'
hide p217
$ update_portrait('st019_01 2', 'p218', [r(-17), light], 6)
c2183 '[convertstrid(1120793)]'
$ update_portrait('st019_01 2', 'p218', [r(-17), dark], 5)
c9861 '[convertstrid(1120794)]'
hide p218
c9843 '[convertstrid(1120795)]'
$ update_portrait('st019_01 2', 'p218', [l(-17), light, flip], 6)
c2181 '[convertstrid(1120796)]'
hide p218
c0 '[convertstrid(1120797)]'
$ update_portrait('st018_01 2', 'p217', [l(-16), light, flip], 6)
c2171 '[convertstrid(1120798)]'
$ update_portrait('st018_01 2', 'p217', [l(-16), dark, flip], 5)
$ update_portrait('st016_01 4', 'p215', [r(-8), light], 6)
c2153 '[convertstrid(1120799)]'
hide p217
$ update_portrait('st016_01 4', 'p215', [r(-8), dark], 5)
$ update_portrait('st019_01 6', 'p218', [l(-17), light, flip], 6)
c2181 '[convertstrid(1120800)]'
hide p218
$ update_portrait('oc002_01 19', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1120801)]'
$ update_portrait('oc002_01 19', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st016_01 2', 'p215', [r(-8), light], 6)
c2153 '[convertstrid(1120802)]'
$ update_portrait('st016_01 2', 'p215', [r(-8), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c21 '[convertstrid(1120803)]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('st016_01 4', 'p215', [r(-8), light], 6)
c2153 '[convertstrid(1120804)]'
hide p215
c9833 '[convertstrid(1120805)]'
return