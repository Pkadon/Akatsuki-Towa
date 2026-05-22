label avg12372:

$ play_music("ed9999.ogg")
scene avg_bg_050
$ update_narrator('c10743')
window show
with fade_in
c10743 '[convertstrid(1133912)]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1133913)]'
$ update_portrait('oc002_01 12', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc003_01 8', 'p3', [r(-6), light], 6)
c33 '[convertstrid(1133914)]'
hide p3
$ update_portrait('oc001_01 4', 'p1', [r(-2), light], 6)
c13 '[convertstrid(1133915)]'
$ update_portrait('oc001_01 4', 'p1', [r(-2), dark], 5)
$ update_portrait('oc002_01 9', 'p2', [l(-3), l_shake, light, flip], 6)
c21 '[convertstrid(1133916)]'
hide p1
$ update_portrait('oc002_01 9', 'p2', [l(-3), dark, flip], 5)
$ update_portrait('oc004_01 14', 'p4', [r(-5), light], 6)
play sfxvoice "avg_vocal_li28.ogg"
c43 '[convertstrid(1133917)]'
hide p2
$ update_portrait('oc004_01 14', 'p4', [r(-5), dark], 5)
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
play sfx2 "common_tag_2.ogg"
c11 '[convertstrid(1133918)]'
hide p4
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
c10743 '[convertstrid(1133919)]'
$ update_portrait('oc001_01 2', 'p1', [l(-2), light, flip], 6)
play sfx2 "dun_obj005_01_01.ogg"
c11 '[convertstrid(1133920)]'
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
c31 '[convertstrid(1133921)]'
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
play sfx2 "other_7088.ogg"
c10743 '[convertstrid(1133922)]'
hide p3
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1133923)]'
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
play sfx2 "fight_6025.ogg"
c10743 '[convertstrid(1133924)]'
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
c11 '[convertstrid(1133925)]'
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
c10743 '[convertstrid(1133926)]'
$ update_portrait('oc001_01 7', 'p1', [l(-2), light, flip], 6)
play sfxvoice "avg_vocal_na22.ogg"
c11 '[convertstrid(1133927)]'
$ update_portrait('oc001_01 7', 'p1', [l(-2), dark, flip], 5)
c10743 '[convertstrid(1133928)]'
c10743 '[convertstrid(1133929)]'
c10743 '[convertstrid(1133930)]'
hide p1
$ update_portrait('oc004_01 21', 'p4', [l(-5), l_shake, light, flip], 6)
c41 '[convertstrid(1133931)]'
$ update_portrait('oc004_01 21', 'p4', [l(-5), dark, flip], 5)
$ update_portrait('oc003_01 12', 'p3', [r(-6), r_shake, light], 6)
play sfxvoice "avg_vocal_ro09.ogg"
c33 '[convertstrid(1133932)]'
hide p4
$ update_portrait('oc003_01 12', 'p3', [r(-6), dark], 5)
$ update_portrait('oc002_01 12', 'p2', [l(-3), light, flip], 6)
c21 '[convertstrid(1133933)]'
return