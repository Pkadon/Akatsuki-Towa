label avg12426:

$ play_music("ed7580.ogg")
scene avg_bg_052
$ update_portrait('oc003_01 12', 'p3', [l(-6), light, flip], 6)
$ update_narrator('c31')
window show
with fade_in
c31 '[convertstrid(1142996)]'
$ update_portrait('oc003_01 12', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc004_01 21', 'p4', [r(-5), r_shake, light], 6)
c43 '[convertstrid(1142997)]'
hide p4
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1142998)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
c31 '[convertstrid(1142999)]'
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1143000)]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1143001)]'
hide p2
hide p1
c0 '[convertstrid(1143002)]'
c0 '[convertstrid(1143003)]'
return