label avg20090:

play music "ed7117.ogg"
scene avg_bg_021
$ update_narrator('c6781')
window show
with fade_in
c6781 '[convertstrid(1004506)]'
play sfx2 "other_7004.ogg"
c6793 '[convertstrid(1004507)]'
c6801 '[convertstrid(1004508)]'
c6793 '[convertstrid(1004509)]'
c6801 '[convertstrid(1004510)]'
c6783 '[convertstrid(1004511)]'
c6783 '[convertstrid(1004513)]'
c6801 '[convertstrid(1004514)]'
c6801 '[convertstrid(1004515)]'
$ update_portrait('oc001_01 2', 'p1', [l_entrance(-2), light, flip], 6)
c11 '[convertstrid(1004516)]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
play sfxvoice "avg_vocal_ro13.ogg"
c33 '[convertstrid(1004517)]'
hide p1
$ update_portrait('oc003_01 8', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 5', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch07.ogg"
c21 '[convertstrid(1004518)]'
hide p3
$ update_portrait('oc002_01 5', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 8', 'p4', [r(-5), light], 6)
c43 '[convertstrid(1123027)]'
return