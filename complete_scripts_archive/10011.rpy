label avg10011:

play music "ED6516.ogg"
scene avg_bg_010
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
$ update_narrator('c13')
window show
with fade_in
play sfx2 "other_7088.ogg"
play sfxvoice "avg_vocal_na10.ogg"
c13 '[convertstrid(1001074)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 4', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1001075)]'
$ update_portrait('oc002_01 4', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 18', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1001076)]'
$ update_portrait('oc001_01 19', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1001077)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1001078)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_ch11.ogg"
c21 '[convertstrid(1001079)]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1001080)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
play sfx2 "fight_6024.ogg"
c13 '[convertstrid(1001081)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1001082)]'
$ update_portrait('oc002_01 19', 'p2', [l_midback(-3), light, flip], 6)
play sfx2 "fight_6020.ogg"
c21 '[convertstrid(1001083)]'
hide p2
$ update_portrait('oc003_01 12', 'p719', [l(-6), l_shake, light, flip], 6)
c7191 '[convertstrid(1001084)]'
$ update_portrait('oc003_01 12', 'p719', [l(-6), dark, flip], 5)
$ update_portrait('oc001_01 20', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1001085)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1001086)]'
$ update_portrait('oc001_01 9', 'p1', [r(-2), dark], 5)
$ update_portrait('oc003_01 8', 'p719', [l(-6), light, flip], 6)
play sfxvoice "avg_vocal_ro13.ogg"
c7191 '[convertstrid(1001087)]'
$ update_portrait('oc003_01 5', 'p719', [l(-6), light, flip], 6)
play sfx2 "fight_6024.ogg"
c7191 '[convertstrid(1001088)]'
return