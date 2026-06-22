label avg12382:

$ play_music("ed7162.ogg")
scene avg_bg_025
$ update_narrator('c0')
window show
with fade_in
play sfx2 "other_7047.ogg"
get_char('c0') '[convertstrid(1134013)]' (**arg(1, 1134013))
$ update_portrait('oc001_01 1', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1134014)]' (**arg(2, 1134014))
$ update_portrait('oc001_01 1', 'p1', [l(-2), dark, flip], 5)
get_char('c10993') '[convertstrid(1134015)]' (**arg(3, 1134015))
hide p1
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1134016)]' (**arg(4, 1134016))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
get_char('c10993') '[convertstrid(1134017)]' (**arg(5, 1134017))
hide p2
$ update_portrait('oc004_01 8', 'p4', [l(-5), light, flip], 6)
get_char('c41') '[convertstrid(1134018)]' (**arg(6, 1134018))
$ update_portrait('oc004_01 8', 'p4', [l(-5), dark, flip], 5)
get_char('c10993') '[convertstrid(1134019)]' (**arg(7, 1134019))
hide p4
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1134020)]' (**arg(8, 1134020))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
get_char('c10993') '[convertstrid(1134021)]' (**arg(9, 1134021))
$ update_portrait('oc002_01 21', 'p2', [l_midback(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch21.ogg"
get_char('c21') '[convertstrid(1134022)]' (**arg(10, 1134022))
hide p2
play sfx2 "fight_6022.ogg"
get_char('c0') '[convertstrid(1134023)]' (**arg(11, 1134023))
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1134024)]' (**arg(12, 1134024)) with shake
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
get_char('c10993') '[convertstrid(1134025)]' (**arg(13, 1134025))
hide p1
play sfx2 "fight_6025.ogg"
get_char('c0') '[convertstrid(1134026)]' (**arg(14, 1134026))
$ update_portrait('oc002_01 2', 'p2', [l(-3), light, flip], 6)
play sfxvoice "avg_vocal_ch12.ogg"
get_char('c21') '[convertstrid(1134027)]' (**arg(15, 1134027))
$ update_portrait('oc002_01 2', 'p2', [l(-3), dark, flip], 5)
get_char('c10993') '[convertstrid(1134028)]' (**arg(16, 1134028))
hide p2
$ update_portrait('oc001_01 12', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1134029)]' (**arg(17, 1134029))
$ update_portrait('oc001_01 12', 'p1', [l(-2), dark, flip], 5)
get_char('c10993') '[convertstrid(1134030)]' (**arg(18, 1134030))
hide p1
$ update_portrait('oc003_01 8', 'p3', [l(-6), light, flip], 6)
get_char('c31') '[convertstrid(1134031)]' (**arg(19, 1134031))
$ update_portrait('oc003_01 8', 'p3', [l(-6), dark, flip], 5)
get_char('c10993') '[convertstrid(1134032)]' (**arg(20, 1134032))
hide p3
$ update_portrait('oc002_01 10', 'p2', [l(-3), light, flip], 6)
get_char('c21') '[convertstrid(1134033)]' (**arg(21, 1134033))
$ update_portrait('oc002_01 10', 'p2', [l(-3), dark, flip], 5)
get_char('c10993') '[convertstrid(1134034)]' (**arg(22, 1134034))
hide p2
$ update_portrait('oc001_01 8', 'p1', [l(-2), light, flip], 6)
get_char('c11') '[convertstrid(1134035)]' (**arg(23, 1134035))
hide p1
$ update_portrait('oc004_01 16', 'p4', [l(-5), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_li10.ogg"
get_char('c41') '[convertstrid(1134036)]' (**arg(24, 1134036))
$ update_portrait('oc004_01 16', 'p4', [l(-5), dark, flip], 5)
get_char('c10993') '[convertstrid(1134037)]' (**arg(25, 1134037))
$ update_portrait('oc004_01 19', 'p4', [l(-5), l_shake, light, flip], 6)
play sfxvoice "avg_vocal_li22.ogg"
get_char('c41') '[convertstrid(1134038)]' (**arg(26, 1134038))
return